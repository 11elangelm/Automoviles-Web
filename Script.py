script utilizado:

from Automoviles.models import Marca
from Automoviles.models import Auto
import random
marca_1 = Marca(nombre="toyota",creador="Kiichiro Toyoda")
marca_1.save()
marca_2 = Marca(nombre="Mazda",creador="Jujiro Matzuda")
marca_2.save()
tipos = ["Sedan","Camioneta","Hashback","Pick-Up","Trailer"]
colores = ["rojo","verde","azul","amarillo","morado","naranja","blanco","negro"]
for i in range(100):
	a = Auto(color=random.choice(colores),modelo=random.randint(1996,2017),tipo=random.choice(tipos))
	a.marca_id = 1
	a.save()
for i in range(900):
	a = Auto(color=random.choice(colores),modelo=random.randint(1996,2017),tipo=random.choice(tipos))
	a.marca_id = 2
	a.save()
