class student():
    def __init__(self,name,age,height,username,password):
        self.name=name
        self.age=age
        self.height=height
        self.username=username
        self.password=password
    def display(self):
        print(self.name+"\n"+str(self.age)+"\n"+self.height)
    def ageUp(self):
        self.age+=1
    def loginInfo(self):
        x=input("enter your username: ")
        if x==self.username:
            y=input("enter your password: ")
            if y==self.password:
                print("yup\n"+self.username+"\n"+self.password)
            else:
                print("noper")
        else:
            print("noper")
dave=student("dave",99,"5'11","davie1234","davethebest")
dave.display()
cthulu=student("cthulu",213578,"300'11","squid78","ocean")
print(cthulu.age)
dave.ageUp()
dave.display()
dave.loginInfo()