import g2d,random
from ClassiMetodi import *
import time

GuardaDestra,GuardaIndietro,GuardaSinistra=False,False,False

#Creo oggetti

oggRana=object.__new__(Frog)
oggRana=Frog(int(CanvasL/2),(CanvasA-altezzaRana),0,0,20)
oggRana.CreaRanaAvanti()#rana al punto di partenza 

oggMacchinaRossa=object.__new__(macchinaRossa)
oggMacchinaRossa=macchinaRossa(640,370,0,0,random.randint(6,15))

oggMacchinaViola=object.__new__(macchinaViola)
oggMacchinaViola=macchinaViola(0,336,0,0,random.randint(3,10))

oggTrattore=object.__new__(trattore)
oggTrattore=trattore(0,405,0,0,random.randint(2,5))

oggCamion=object.__new__(camion)
oggCamion=camion(640,310,0,0,random.randint(2,8))

oggMacchinaGialla=object.__new__(macchinaGialla)
oggMacchinaGialla=macchinaGialla(640,275,0,0,random.randint(6,18))

oggZatteraLunga=object.__new__(zatteraLunga)
oggZatteraLunga=zatteraLunga(-60,220,0,0,random.randint(1,3))

oggZatteraMedia=object.__new__(zatteraMedia)
oggZatteraMedia=zatteraMedia(-60,200,0,0,random.randint(2,4))

oggZatteraPiccola=object.__new__(zatteraPiccola)
oggZatteraPiccola=zatteraPiccola(670,180,0,0,random.randint(1,3))

oggZatteraLunga1=object.__new__(zatteraLunga)
oggZatteraLunga1=zatteraLunga(670,160,0,0,random.randint(2,4))

oggZatteraMedia1=object.__new__(zatteraMedia)
oggZatteraMedia1=zatteraMedia(-60,140,0,0,random.randint(1,2))

oggZatteraPiccola1=object.__new__(zatteraPiccola)
oggZatteraPiccola1=zatteraPiccola(670,120,0,0,random.randint(1,4))

oggZatteraLunga2=object.__new__(zatteraLunga)
oggZatteraLunga2=zatteraLunga(670,100,0,0,random.randint(1,3))

oggZatteraMedia2=object.__new__(zatteraMedia)
oggZatteraMedia2=zatteraMedia(-60,80,0,0,random.randint(2,4))

#Collisioni
def collisionStrada(Ogg:object):
  global vite

  x1,y1=oggRana.position()
  x2,y2=Ogg.position()
  if x1>x2 and x1<(x2+30) and y1>y2 and y1<(y2+18):
    oggRana.Partenza()
    MenoVita()

def collisionMare(Ogg:object,Cost:int):
    global vite

    x1,y1=oggRana.position()
    x2,y2,velocità=Ogg.position()
    if y1<=(y2+10)and y1>=(y2-10):
      if (x1<=(x2+Cost) and x1>=x2):  
       oggRana._dx+=velocità
      else:
       oggRana.Partenza()
       MenoVita()  

def collisionMareIndietro(Ogg:object,Cost:int):
    global vite 

    x1,y1=oggRana.position()
    x2,y2,velocità=Ogg.position()
    if y1<=(y2+10)and y1>=(y2-10):
      if (x1<=(x2+Cost) and x1>=x2):  
       oggRana._dx-=velocità
      else:
       oggRana.Partenza()
       MenoVita()     

#Gestione eventi da tastiera
def keydown(code:str):
 global oggRana,GuardaDestra,GuardaSinistra,GuardaIndietro

 if code == "ArrowUp":
  oggRana.MovAvanti()
 elif code=="ArrowDown":
  oggRana.MovIndietro()
  GuardaIndietro=True
 elif code=="ArrowLeft":
  oggRana.MovSinistra()
  GuardaSinistra=True
 elif code=="ArrowRight":
  oggRana.MovDestra()
  GuardaDestra=True
 else:
  oggRana.Fermo()

def keyup(code):
 global oggRana,GuardaDestra,GuardaSinistra,GuardaIndietro
 oggRana.Fermo()
 GuardaDestra,GuardaSinistra,GuardaIndietro=False,False,False
 
#Animazione
def Update():
 global oggRana,vite,punteggio,contatore
 
 contatore +=1
 
 #grafica inizale
 g2d.handle_keyboard(keydown,keyup)
 g2d.draw_image(backgroud,(0,0))
 g2d.draw_image(titolo,(230,0))
 g2d.draw_text("Vite Rimanenti: ",(0,244,150),(450,0),25)
 g2d.draw_text(str(vite),(0,244,150),(585,0),25)
 g2d.draw_text("Score: ",(0,244,150),(10,0),25)
 g2d.draw_text(str(punteggio),(0,244,150),(80,0),25)

 #veicoli
 oggMacchinaRossa.Muovi()
 oggMacchinaRossa.Controllo()
 oggMacchinaRossa.CreaMacchinaRossa()
 collisionStrada(oggMacchinaRossa)

 oggMacchinaViola.Muovi()
 oggMacchinaViola.Controllo()
 oggMacchinaViola.CreaMacchinaViola()
 collisionStrada(oggMacchinaViola)

 oggMacchinaGialla.MuoviIndietro()
 oggMacchinaGialla.Controllo()
 oggMacchinaGialla.CreaMacchinaGialla()
 collisionStrada(oggMacchinaGialla)

 oggTrattore.Muovi()
 oggTrattore.Controllo()
 oggTrattore.CreaTrattore()
 collisionStrada(oggTrattore)

 oggCamion.MuoviIndietro()
 oggCamion.Controllo()
 oggCamion.CreaCamion()
 collisionStrada(oggCamion)

#Zattere
 oggZatteraLunga.Muovi()
 oggZatteraLunga.Controllo()
 oggZatteraLunga.CreaZatteraLunga()
 collisionMare(oggZatteraLunga,150)

 oggZatteraMedia.Muovi()
 oggZatteraMedia.Controllo()
 oggZatteraMedia.CreaZatteraMedia()
 collisionMare(oggZatteraMedia,90)

 oggZatteraPiccola.MuoviIndietro()
 oggZatteraPiccola.Controllo()
 oggZatteraPiccola.CreaZatteraPiccola()
 collisionMareIndietro(oggZatteraPiccola,60)

 oggZatteraLunga1.MuoviIndietro()
 oggZatteraLunga1.Controllo()
 oggZatteraLunga1.CreaZatteraLunga()
 collisionMareIndietro(oggZatteraLunga1,150)

 oggZatteraMedia1.Muovi()
 oggZatteraMedia1.Controllo()
 oggZatteraMedia1.CreaZatteraMedia()
 collisionMare(oggZatteraMedia1,90)

 oggZatteraPiccola1.MuoviIndietro()
 oggZatteraPiccola1.Controllo()
 oggZatteraPiccola1.CreaZatteraPiccola()
 collisionMareIndietro(oggZatteraPiccola1,60)
 
 oggZatteraLunga2.MuoviIndietro()
 oggZatteraLunga2.Controllo()
 oggZatteraLunga2.CreaZatteraLunga()
 collisionMareIndietro(oggZatteraLunga2,150)

 oggZatteraMedia2.Muovi()
 oggZatteraMedia2.Controllo()
 oggZatteraMedia2.CreaZatteraMedia()
 collisionMare(oggZatteraMedia2,90)

 #movimento rana
 oggRana.Muovi()
 oggRana.ControlloArena()
 if GuardaDestra==True:
  oggRana.CreaRanaDestra()
 elif GuardaIndietro==True:
  oggRana.CreaRanaIndietro()
 elif GuardaSinistra==True:
  oggRana.CreaRanaSinistra()
 else:
  oggRana.CreaRanaAvanti()
 
 oggRana.Fermo()

 #Richiamo metodi 
 vite=Vita()
 punteggio=Punteggio()

#Gestione Vite Finite
 if vite<=0:
  GameOver=g2d.load_image("gameover.png") 
  g2d.draw_image(GameOver,(0,0))
  time.sleep(1)