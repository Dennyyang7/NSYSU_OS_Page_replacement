import random

times = 300000  #執行幾次
Max_Page = 1200  # Reference string

class Generate(object):
    
    def __init__(self):
        
        self.times = 300000
        self.Max_Page = 1200

    def GenerateRandomPage(self):
        '''
        亂數產生References

        Return:
            - PageInput
        '''
        startnum = 0 # 隨機起始數字
        continum = 0 # 連續取幾個數字
        Randsize = 0 # 共已經取多少數字
        
        PageInput = []
        print(f'產生{self.times}個亂數中, 每個亂數介於1~{self.Max_Page}, 並有1~20個連續數字')
        
        while Randsize<self.times: # 產生300000次後停止
            startnum = random.randint(1, self.Max_Page-20)
            continum = random.randint(1, 20)
            Randsize += continum
            
            for i in range(continum): # 連續的個數在[1,20]之間
                PageInput.append(startnum) # 每次 + 1  就會是連續的數字
                startnum += 1

                
        print('亂數產生完成')
        
        PageInput = PageInput[:self.times]  # 最多只保留100000個數
        return PageInput

    def GenerateLocalityPage(self):
        '''
        產生Locality references, 模擬function call, 每次產生4~10個(1/300~1/120), 直到300000個

        Return:
            - PageInput
        '''
        PageInput = []
        size = 0 # 已產生多少數字
        Functiontimes =0
        print(f'產生{self.times}個Locality references中')
        while size<self.times: # 產生300000次後停止
            Functiontimes += 1 # 函數呼叫次數
            ReferenceSize = random.randint(4,10)# 決定抽取4~10之間"個"數字
            ReferenceStart = random.randint(1,500-ReferenceSize)# 設定開始數字
            ReferenceEnd = ReferenceStart+ReferenceSize# 設定結束數字
            size += ReferenceSize
            # 在start和end間取size個數字
            for i in range(ReferenceSize):
                PageInput.append(random.randint(ReferenceStart, ReferenceEnd))
                
        PageInput = PageInput[:self.times]  # 最多只保留300000個數

        print('產生完成, 共發生 {} 次Function call'.format(Functiontimes))

        return PageInput

    def GenerateMyWayPage(self):
        '''
        一樣是法2的作法，只是重複2次，增強Locality之效果。Page Fault 大大降低。

        Return:
            - PageInput
        '''
        PageInput = []
        size = 0
        Functiontimes =0
        
        print(f'產生{self.times}個Temporal Locality & Spatial Locality references中, 每個亂數介於1~{self.Max_Page}')
        while size<self.times:
            Functiontimes += 1
            ReferenceSize = random.randint(4,10)
            ReferenceStart = random.randint(1,500-ReferenceSize)
            ReferenceEnd = ReferenceStart+ReferenceSize
            size += 2 * ReferenceSize
            generatePage = []
            
            for i in range(ReferenceSize):
                generatePage.append(random.randint(ReferenceStart, ReferenceEnd))
            for i in range(2): # 執行2次讓PageInput寫入4次
                for j in range(len(generatePage)):
                    PageInput.append(generatePage[i])
        
        PageInput = PageInput[:self.times] 

        print(f'產生完成, 共發生 {Functiontimes} 次Function call')

        return PageInput
    

    def GenerateRandomModify(self):
        '''
        亂數產生被Modify Page

        Return:
            -list: Modify Pages
        '''
        ModifyPage = []
        for i in range(self.times):
            ModifyPage.append(random.randint(0,1))
        print('隨機 Modify Page 使用中')

        return ModifyPage
