class Employee:
    
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)
    
    def details(self):
        print("Name is : ",self.name)
        print("Idnumber is : ",self.idnumber)

class Person(Employee):
    
    def __init__(self,name,idnumber,post,salary):
        self.post = post
        self.salary = salary
        #super().__init__(name,idnumber)
        Employee.__init__(self,name,idnumber)
   
    def details(self):
        print("my name is :",self.name)
        print("my id is : ",self.idnumber)
        print("my post is:  ",self.post)
        print("my salary is ",self.salary)

obj = Person("Bharathi",123,"Software Developer",700000)


obj.display()

obj.details()