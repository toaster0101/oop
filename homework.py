camList=["bad","ok","decent","good","great","incredible"]
x=0
class phone():
    def __init__(self,model,dateMade,cameraQuality):
        self.model=model
        self.dateMade=dateMade
        self.cameraQuality=cameraQuality
    def display(self):
        print(self.model+"\n"+self.dateMade+"\n"+self.cameraQuality)
    def upgradeCam(self):
        global x
        if x<5:
            x+=1
    def degradeCam(self):
        global x
        if x>0:
            x-=1
henry=phone("Iphone 11","10/9/2019",camList[x])
henry.display()
henry.upgradeCam()
henry=phone("Iphone 11","10/9/2019",camList[x])
henry.display()
henry.degradeCam()
henry=phone("Iphone 11","10/9/2019",camList[x])
henry.display()