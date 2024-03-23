def MyWay(PageFrameSize, PageInput, ModifyPage):
    '''
    My page replacement
        我們先取得PageID之後 在 [Start ,PageID, End], Start、End 差距皆為 PageFramesize,
        與我們 PageID 且不再 PageFramesize裡, 差距最大的(及 spatial locality 最無相關的)為犧牲page 
        如果都在[Start ,PageID, End] 裡, 則退化為FIFO
    Return:
        - int: Page fault
        - int: Interrupts
        - int: DiskIO
    '''  
    PageQ = []
    PageQModify = []
    PageFaults = 0
    DiskIO = 0
    interrupts = 0

    for indx, PageID in enumerate(PageInput):
        if PageID not in PageQ:
            PageFaults += 1
            interrupts += 1
            if len(PageQ) < PageFrameSize:
                PageQ.append(PageID)
                PageQModify.append(ModifyPage[indx])
            else:
                victim_indx = None
                MaxDistance = 0 # 需挑Victim
                # 求目前要插入之page ± PageFrameSize
                PageEnd = PageID + PageFrameSize
                PageStart = PageID - PageFrameSize
                
                if PageStart < 1:
                    PageStart = 1
                for rep_indx, rep in enumerate(PageQ):
                    if rep < PageStart or rep > PageEnd: # 如果frame中page的值不在input附近
                        if abs(PageID - rep) > MaxDistance: # 找出離input(PageID)最遠的
                            MaxDistance = abs(PageID - rep)
                            victim_indx = rep_indx
    
                if victim_indx == None:  # 皆在範圍內，就退化成FIFO
                    victim_indx = 0
                    for i in range(len(PageQ)-1):
                        PageQ[i] = PageQ[i+1]
                        PageQ[PageFrameSize-1] = PageID
                
                if PageQModify[victim_indx] == 1:
                    DiskIO += 1
                    interrupts += 1

                PageQ[victim_indx] = PageID
                PageQModify[victim_indx] = ModifyPage[indx]
                
        else:
            pass
    
    return PageFaults, interrupts, DiskIO