import matplotlib.pyplot as plt

class Drawer(object):

    def __init__(self, AlgoType, FrameSize):
        '''
        Args:
            - AlgoType: List
            - FrameSize: List
        '''
        self.AlgoType = AlgoType
        self.FrameSize = FrameSize
        

    def FaultFig(self, GenerateType, Pagefaults):
        '''
        Args:
            - GenerateType: String (Reference Strings 產生方式)
            - Pagefaults: List (this Algo. page faults number)
        '''

        styles = ['r-*','b-.^','g-.o', 'k:+'] # 線條呈現
        plt.title('Reference strings type: '+GenerateType) 
        plt.xlabel('Frame Size')
        plt.ylabel('Number of page faults')
        for indx, faults in enumerate(Pagefaults):
            plt.plot(self.FrameSize, faults, styles[indx], label=self.AlgoType[indx])
        
        plt.xticks(self.FrameSize)
        plt.legend(loc='upper right')
        plt.tight_layout(pad=3)
        plt.savefig('M103040070/Images/'+GenerateType+'_PageFault')
        plt.close()

    def DiskFig(self, GenerateType, diskIO):
        '''
        Args:
            - GenerateType: String (Reference Strings 產生方式)
            - diskIO: List
        '''
        styles = ['r-*','b-.^','g-.o', 'k:+']
        plt.title('Reference strings type: '+GenerateType)
        plt.xlabel('Frame Size')
        plt.ylabel('Number of DiskIO')

        for indx, faults in enumerate(diskIO):
            plt.plot(self.FrameSize, faults, styles[indx], label=self.AlgoType[indx])
        
        plt.xticks(self.FrameSize)
        plt.legend(loc='upper right')
        plt.tight_layout(pad=3)
        plt.savefig('M103040070/Images/'+ GenerateType+ '_DiskIO')
        plt.close()

    def InterrFig(self, GenerateType, interrupts):
        '''
        Args:
            - GenerateType: String (Reference Strings 產生方式)
            - interrupts: List
        '''
        styles = ['r-*','b-.^','g-.o', 'k:+']
        plt.title('Reference strings type: '+GenerateType)
        plt.xlabel('Frame Size')
        plt.ylabel('Number of Interrupts')

        for indx, faults in enumerate(interrupts):
            plt.plot(self.FrameSize, faults, styles[indx], label=self.AlgoType[indx])
        
        plt.xticks(self.FrameSize)
        plt.legend(loc='upper right')
        plt.tight_layout(pad=3)
        plt.savefig('M103040070/Images/'+ GenerateType+ '_Interrupts')
        plt.close()


    # def ARBFig(self, Interrupts):
    #     '''
    #     additional-reference-bits replacement之reference input對其的變化
    #     Args:
    #         - Interrupts: List
    #     '''
    #     # pdf = PdfPages('ARBinterrupts_' + GenerateType +'.pdf')
    #     Generate = ['Random', 'Locality', 'MyWay']
    #     styles = ['r-^','b-.*','c-.o', 'k:+']
    #     plt.title('Number of ARB interrupt')
    #     plt.xlabel('Frame Size')
    #     plt.ylabel('Number of interrupts')

    #     for indx, interr in enumerate(Interrupts):
    #         plt.plot(self.PageFrameSize, interr, styles[indx], label=Generate[indx])
        
    #     plt.legend(loc='upper left',bbox_to_anchor=(1,1))
    #     plt.tight_layout(pad=3)
    #     plt.savefig('Images/ARBinterrupts')
    #     plt.close()