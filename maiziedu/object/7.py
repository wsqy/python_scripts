class Box:
    def __init__(self,length=6,width=4,height=3):
        self.length = length
        self.width = width
        self.height = height
        self.__status = False
        self._color = 'red'
 
 
    def getArge(self):
        self.__arge = self.height*self.length*self.width
        print(self.__arge)
        
    def setColor(self,color):
        self._color = color
    
    def getColor(self):
        print("Box's color is:",self._color)
    
    def openBox(self):
        if self.__status:
            print("Box is opening...can't open")
        else:
            print("Box has been open...")
            self.__status = True
            
    def closeBox(self):
        if self.__status:
            print("Box has been close...") 
            self.__status = False
            
        else:
            print("Box is closing...can't lose")


if __name__ == "__main__":
    b = Box()
    b.getColor()
    b.openBox()
    b.openBox()
    b.closeBox()
    b.closeBox()
    b.openBox()
    
    