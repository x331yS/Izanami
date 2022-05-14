class PixelColors(object):
    def __init__(self,length):
        self.length = length
        self.pix = []
        self.highlow=[]
        self.start()
    
    def start(self):
        for i in range(self.length):
            self.pix.append((0,0,0))
            self.highlow.append(True)
    def fillAll(self,color):
        for i in range(self.length):
            self.pix[i] = color
    def setColor(self, i, color):
        self.pix[i] = color
    def setHighLow(self, i, hl):
        self.highlow[i] = hl
    def getColor(self,i):
        return self.pix[i]
    def getHighLow(self,i):
        return self.highlow[i]
