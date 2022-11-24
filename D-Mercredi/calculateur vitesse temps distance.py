import numpy
import json

question = 'Que voulez-vous calculer ?'

demande = input(question)
if demande == 'vitesse':
    distance = float(input("quelle est la distance?(en km)"))
    temps = float(input("Combien de temps s'est écoulé?(en heure)"))
    speed = distance/temps
    print(speed)
    if speed>100:
        print('wow, you are speeding !')
    else:...
if demande == 'temps':
    distance = float(input("quelle est la distance?(en km)"))
    speed = float(input("Quelle est la vitesse?(en km/h)"))
    temps = distance/speed
    print(temps)
    if temps>3:
        print("That's too long...")
    else:...
if demande == 'distance':
    temps = float(input("Combien de temps s'est écoulé ?(en heure)"))
    speed = float(input("Quelle est la vitesse?(en km/h)"))
    distance = temps*speed
    print(distance)
    if distance>100:
        print("taht's so far...")
    else:...
else:
    print("veuillez demander la distance le temps ou la vitesse.")