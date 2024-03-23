from Matcher.FIFOreplacement import FIFO
from Matcher.ARBreplacement import ARB
from Matcher.OPTreplacement import OPT
from Matcher.MyWayreplacement import MyWay

class AlgoMatcher(object):

    def __init__(self, PageInput, ModifyPage):
        self.PageInput = PageInput
        self.ModifyPage = ModifyPage
    
    def match(self, AlgoType, PageFrameSize):
        if AlgoType == 'FIFO':
            return FIFO(PageFrameSize, self.PageInput, self.ModifyPage)
        elif AlgoType == 'OPT':
            return OPT(PageFrameSize, self.PageInput, self.ModifyPage)
        elif AlgoType == 'ARB':
            return ARB(PageFrameSize, self.PageInput)
        elif AlgoType == 'MyWay':
            return MyWay(PageFrameSize, self.PageInput, self.ModifyPage)
