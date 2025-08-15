class Dragon:
    def __init__(self, name, power, Defense, Attac):
        self.name = name
        self.power = power
        self.Defense = Defense
        self.Attac = Attac

    def introduce(self):
        print ("Hi, My name is",self.name + " and my power is" + str(self.power))

    def recib_Attac(self, damage):
        # self.Defense -= damage
        self.Defense=self.Defense-damage

    def alive(self):
        return self.Defense > 0

Thairn = Dragon("Thairn", "Manipular el rayo", 100, 25)
Andarna = Dragon("Andarna", "Detener el tiempo", 100, 20)

Andarna.introduce()
Thairn.introduce()

Thairn.recib_Attac(Andarna.Attac)
# Andarna.recib_Attac(Thairn.Attac)

while Thairn.alive():
    print("Sigo vivo")
    Thairn.recib_Attac(Andarna.Attac)

if not Thairn.alive():
    print("He muerto")