class index():
    def __init__(self,name,sex,character,favorite_food):
        self.name = name
        self.sex=sex
        self.character=character
        self.favorite_food=favorite_food
    def display(self):
        print(self.name+' is a '+self.sex+' people '+'is '+self.character+' likes '+self.favorite_food,end='')

alex=index('alex','female','kind','apple')
alex.display()
