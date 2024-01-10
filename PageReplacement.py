from GenerateReferences import Generate # 導入 Reference string
from Matcher.match import AlgoMatcher # 匹配 Algo
from Drawer.Draw import Drawer # 畫圖
import random 

GenerateReferences = ['Random', 'Locality', 'MyWay'] 
Algo = ['FIFO', 'OPT', 'ARB','MyWay']
PageFrameSize = [30,60,90,120,150]

generateRef = Generate()# 呼叫 GenerateReferences.py 
drawer = Drawer(Algo, PageFrameSize)# 呼叫 Drawer/Draw.py

def GenerateMatcher(match):
    '''
    Reference strings產生方式
    Return:
        - PageInput(Referstring的值)
    '''
    global generateRef

    if match == 'Random':
        PageInput = generateRef.GenerateRandomPage()
    elif match == 'Locality':
        PageInput = generateRef.GenerateLocalityPage()
    elif match == 'MyWay':
        PageInput = generateRef.GenerateMyWayPage()

    return PageInput

def AlgoMatch(GenerateType, PageInput, ModifyPage):
    '''
    Args:
        - Generate Type(產生Referstring的方式)
        - PageInput(Referstring的值)
        - ModifyPage(Modify bit的值)
    '''
    global Algo, PageFrameSize, generateRef, drawer
     
    # 將Referstring,Modify傳入Matcher/match.py 並以matcher代表其
    matcher = AlgoMatcher(PageInput, ModifyPage)
    
    pagefaults = []
    diskList = []
    InterruptsList = []
    esc_interrupts = []

    for algo in Algo:
        eachAlgoFaults = []
        eachIO = []
        eachinterr = []
        print(f'This is {algo}. replacement:')
        
        ######開始進行模擬######
        for size in PageFrameSize:
            # 傳入方法名稱和Frame size to AlgoMatcher
            faults, interr, diskIO = matcher.match(algo, size)
            # 將結果分別傳入串列中
            eachAlgoFaults.append(faults)
            eachIO.append(diskIO)
            eachinterr.append(interr)
                
                
            print(f'---Frame Size: {size}, Page Faults: {faults}, DiskIO: {diskIO}, Interrupts: {interr}')
        print('---------------------------------------------------------------')
     
        pagefaults.append(eachAlgoFaults)
        diskList.append(eachIO)
        InterruptsList.append(eachinterr)
        
    drawer.FaultFig(GenerateType, pagefaults)
    drawer.DiskFig(GenerateType, diskList)
    drawer.InterrFig(GenerateType, InterruptsList)
 
 
def AutoTest():
    '''
     自動測試
    '''
    global GenerateReferences, Algo, PageFrameSize, drawer

    interrupts = []
    
    '''
    分別執行各References
    '''
    for generate in GenerateReferences:
        print('References 產生方式: {}'.format(generate))
        PageInput = GenerateMatcher(generate) # 產生Referstring
        ModifyPage = generateRef.GenerateRandomModify()# 產生 Modify bit
        interr = AlgoMatch(generate, PageInput, ModifyPage)
        interrupts.append(interr)


def main():
    AutoTest()

if __name__ == '__main__':
    main()


# def ManualTest():
#     '''
#     手動測試模式
#     '''
#     Algo = ['FIFO','OPT']
#     FrameSize = int(input('Frame的數量:'))
#     ReferenceSize = int(input('Reference string 的數量:'))
#     StringInput = input('Reference string 的編號:')
#     StringInput = [int(page) for page in StringInput.split(' ')]
#     matcher = AlgoMatcher(StringInput, StringInput)
#     for a in Algo:
#         faults = matcher.match(a, FrameSize)
#         print('{} page replacement, Frame Size:{}, Page Faults:{}'.format(a, FrameSize, faults))
            
