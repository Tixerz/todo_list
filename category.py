
class category:
    
    def __init__(self,name,color):
        self.color =color 
        self.name = name
        self.data = []
        self.minuts = 0
        self.hours = 0
        
        
    def edit_name(self,new_name):
        self.name = new_name
        
    def delete(self , index):
        self.data.pop(index)
        
    def add_item(self,item):
        self.data.append(item)
    def spent_time(self,min):
        
        if min >=60 :
            self.hours += min/60
            min = min%60
        self.minuts = min
            
            


