import os
import math

def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
		
#Parte grafica		

def banner():
    clr()
    logo =             """
           ________
      /______  |
     |       | |      _
     | ===== | |     | |
     | ===== | |    o o
     |       | |         |~
     |  .-.  | |       o    o o
     | ' . ' | |   |~       |_|
  ..'| '._.' | |  o
.'   |_______|/ ks

    """
    print(logo)
    print("\n")
    print("Script valido solo con apparati da 3-10 W")
    print("")
    print("Banda da 2 metri e 70 centimetri")
    print("")
    print("Inserire l'altezza in metri")
    print("")
    print("")   
        
banner()

#Algoritmo

#Formula D = 3,57 x (√H1 + √H2)

Antenna1 = int (input("Altezza Rtx: "))
Antenna2 = int (input("Altezza Antenna: "))
Radice1 = math.sqrt(Antenna1)
Radice2 = math.sqrt(Antenna2)
I = Radice1 + Radice2
Risultato = int(I*3.57)
print("")
print("Distanza percorribile senza ostacoli: ",Risultato,"Km")
