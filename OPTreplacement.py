def OPT(PageFrameSize, PageInput, ModifyPage):
    '''
    Optimal replacement
    interrupt = page faults + DiskIO

    Args:
        - Frame Size
        - PageInput

    Return:
        - int : Page Faults Numbers
        - int : Interrupts
        - int : DiskIO
    '''
    PageQ = []
    PageFaults = 0
    DiskIO = 0
    interrupts = 0
    PageQModify = []    # 紀錄Page是否會被修改
    
    for index, PageID in enumerate(PageInput):
        if PageID not in PageQ:
            PageFaults += 1
            interrupts += 1
            if len(PageQ) < PageFrameSize:
                PageQ.append(PageID)
                PageQModify.append(ModifyPage[index])      # 存modify紀錄  0:不會被修改  1:會修改
            else:                          # Need replace
                visited = []
                FeaturePage = PageInput[index+1:] # 現在的+1到end
                for rep_indx, rep in enumerate(PageQ):  
                    if rep not in FeaturePage:          # 未來不會再有
                        PageQ[rep_indx] = PageID
                        break
                    else:
                        distance = FeaturePage.index(rep)  # 未來會出現，計算出現的距離
                        visited.append(distance)
                        
                if len(visited) >= PageFrameSize:          # 挑距離最遠的為Victim
                    victim_indx = visited.index(max(visited))
                    victim = PageQ[victim_indx]
                    
                    if PageQModify[victim_indx] == 1:
                        DiskIO += 1
                        interrupts += 1
                    
                    PageQ[victim_indx] = PageID  # 犧牲Page被置換
                    PageQModify[victim_indx] = ModifyPage[index] 
                    
        else:
            pass

    return PageFaults, interrupts, DiskIO