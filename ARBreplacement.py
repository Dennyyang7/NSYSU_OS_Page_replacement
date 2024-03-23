import random
def ARB(PageFrameSize, PageInput):
    '''
    additional reference bits replacement
    interrupt = page faults + DiskIO

    Args:
        - Frame Size
        - PageInput
	    - ModifyPage

    Return:
        - int : Page Faults Number
        - int : Interrupts
        - int : DiskIO
    '''
    PageQ = []       # frame page quere
    PageFaults = 0
    DiskIO = 0
    victim = 0 # 犧牲 page
    refQ_8b = [] #8-bits
    interrupts = 0
    times = 0 # 每存取PageframeSize大小 reference bit往右移一次
    recent_list = [] # 最近存取的 Page
    for index, PageID in enumerate(PageInput):
        times += 1
        if PageID not in PageQ :
            PageFaults += 1
            interrupts += 1
            if len(PageQ) < PageFrameSize:# 如果 Frame 還有空位,直接放入
                PageQ.append(PageID)
                refQ_8b.append(128)
                recent_list.append(PageID)
            else: # Frame 沒有空位了
                if(PageID not in recent_list):
                    recent_list.append(PageID)
                victim_index = refQ_8b.index(min(refQ_8b)) # 犧牲 page 為 reference bit最小 bit (如果有兩個以上 則 index最小值被取代)
                # 50 % DiskIO 
                if(random.randint(1, 10) < 6): 
                    DiskIO += 1
                    interrupts += 1
                refQ_8b[victim_index] = 0 # 被置換所以歸零
                PageQ[victim_index] = PageID # 在frame之victim page插入
                refQ_8b[victim_index] = 128
            # 經過一段 Time 實施右移, recent_list 清空
            if times % PageFrameSize == 0:
                for i in range(0, len(refQ_8b)):
                    refQ_8b[i] = refQ_8b[i] // 2  # binary right shift =>  decimal divided by 2 
                for j in range(0,len(recent_list)): # 有被最近參考到的 + 128
                    if(recent_list[j] in PageQ):
                        refQ_8b[PageQ.index(recent_list[j])] += 128
                recent_list = []
        else: # PageID in PageQ
            if(PageID not in recent_list):
                recent_list.append(PageID)
            
    


    return PageFaults, interrupts, DiskIO
