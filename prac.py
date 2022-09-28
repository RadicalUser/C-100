class Cars :
    def __init__(self):
        self.Class = input("Enter class :")
        self.type = input("Enter type :")
        self.color = input("Enter color :")
        self.rarity = input("Enter rarity :")
        self.prize = int(input("Enter prize : "))

    def display(self):
        print(self.Class , self.type , self.color, self.rarity , self.prize)

MercedesSClass =  Cars()

MercedesSClass.display()

Buggahti = Cars()

Buggahti.display()