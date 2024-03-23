def FIFO(PageFrameSize, PageInput, ModifyPage):
    '''
    First-in-first-out replacement
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
    PageQModify = [] # frame page 的 Modify bit
    interrupts = 0

    for index, PageID in enumerate(PageInput): # enumerate : 給PageID賦予index
        if PageID not in PageQ:
            PageFaults += 1
            interrupts += 1
            if len(PageQ) < PageFrameSize:#如果Frame還有空位,直接放入
                PageQ.append(PageID)
                PageQModify.append(ModifyPage[index])# 存modify紀錄  0:不會被修改  1:會修改
            else:
                if PageQModify[0] == 1:
                    DiskIO += 1
                    interrupts += 1
                # 每次都向左移一格
                for i in range(len(PageQ)-1):
                    PageQ[i] = PageQ[i+1]
                    PageQModify[i] = PageQModify[i+1]
                PageQ[PageFrameSize-1] = PageID# 在frame之最後元素插入frame
                PageQModify[PageFrameSize-1] = ModifyPage[index]# 在Modify之最後元素插入Modify

        else:
            pass

    return PageFaults, interrupts, DiskIO
