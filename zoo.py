


from turtle import color


class Animal:

    def __init__(self , name , age , healthLevel=0 , happiness=0):
        self.name = name
        self.age = age
        self.healthLevel = healthLevel
        self.happiness = happiness
    
    def display_info(self):
        print(f"The animal Name is {self.name} and the health level is {self.healthLevel}, and the happiness level is {self.happiness}")

    def feed (self):
        self.healthLevel += 10
        self.happiness += 10



class Lion(Animal):

    def __init__(self, name, age=5, type="female" ,healthLevel=5, happiness=5):
        super().__init__(name, age)
        self.healthLevel = healthLevel
        self.happiness = happiness
        self.type = type

    def display_info(self):
        print(f"The animal Name is {self.name} and the health level is {self.healthLevel}, and the happiness level is {self.happiness} and the type is: {self.type}")

    def feed (self):
        self.heealthLevel += 15
        self.happiness += 15


class Tiger(Animal):
    def __init__(self, name, age=5, healthLevel=9, happiness=9):
        super().__init__(name, age)
        self.healthLevel = healthLevel
        self.happiness = happiness

    def feed (self):
        self.healthLevel += 5
        self.happiness += 5

class Bear(Animal):
    def __init__(self, name, age=5, color="White", healthLevel=10, happiness=10):
        super().__init__(name, age)
        self.healthLevel = healthLevel
        self.happiness = happiness
        self.color = color

    def display_info(self):
        print(f"The animal Name is {self.name} and the health level is {self.healthLevel}, and the happiness level is {self.happiness} and the color is: {self.color} the age is:{self.age}")
        

    def feed (self):
        self.healthLevel += 20
        self.happiness += 20



lion1 = Lion("Semba" , 5 , "Male" , 300 , 600 )
tiger1 = Tiger("Tige" , 4 )
bear1 = Bear("The boo" , 3 , "Yellow")

lion1.display_info()
tiger1.display_info()
bear1.display_info()

print(lion1.type)
print(bear1.color)


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append( Lion(name) )
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()
