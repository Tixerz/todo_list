class category:
    
    def __init__(self,name,color):
        self.color =color 
        self.name = name
        self.data = []
        

a = category("sex" , "red")
a.data.append("b")
b= category("lol" , "q")
b.data.append("lolllll")


print(a.data )
print(b.data )