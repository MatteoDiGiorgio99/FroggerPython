import g2d

#Dichiarazione Variabili
CanvasL,CanvasA=640,480
altezzaRana=40
#vecchiaPos,vecchiaPos1,oldPos2,oldPos3=0,0,0,0
punteggio=0
contatore=0
vite=3

#Carico oggetti
titolo=g2d.load_image("TITLE.png")
backgroud=g2d.load_image("BG.png")
RanaAvanti,RanaIndietro,RanaDestra,RanaSinistra=g2d.load_image("RanaAvanti.png"),g2d.load_image("RanaIndietro.png"),g2d.load_image("RanaDestra.png"),g2d.load_image("RanaSinistra.png")
Trattore,Camion=g2d.load_image("Trattore.png"),g2d.load_image("Camion.png")
MacchinaRossa,MacchinaGialla,MacchinaViola=g2d.load_image("MacchinaRossa.png"),g2d.load_image("MacchinaGialla.png"),g2d.load_image("MacchinaViola.png")
ZatteraLunga,ZatteraMedia,ZatteraPiccola=g2d.load_image("LegnoLungo.png"),g2d.load_image("LegnoMedio.png"),g2d.load_image("LegnoPiccolo.png")

#Disegno il canvas 
g2d.init_canvas((CanvasL,CanvasA))

#Creo classi Actor
class Frog():

 def __init__(self,x:int,y:int,dx:int,dy:int,speed:int):
  self._x,self._y,self._dx,self._dy,self._speed=x,y,dx,dy,speed
 def CreaRanaAvanti(self): 
  g2d.draw_image(RanaAvanti,(self._x,self._y))
 def CreaRanaIndietro(self): 
  g2d.draw_image(RanaIndietro,(self._x,self._y))
 def CreaRanaSinistra(self): 
  g2d.draw_image(RanaSinistra,(self._x,self._y))
 def CreaRanaDestra(self): 
  g2d.draw_image(RanaDestra,(self._x,self._y))
    
 #Inizio
 def Partenza(self):

  self._x=int(CanvasL/2) 
  self._y=CanvasA-altezzaRana
  g2d.draw_image(RanaAvanti,(self._x,self._y))


 def ControlloArena(self):
  global vite

  if self._x>CanvasL or self._x < 0:

   vite-=1
   self._x=int(CanvasL/2) 
   self._y=CanvasA-altezzaRana

  if self._y>CanvasA:

   vite-=1
   self._x=int(CanvasL/2) 
   self._y=CanvasA-altezzaRana  

  if self._y<20:

   global punteggio
   vite+=1
   punteggio+=500
   self._x=int(CanvasL/2) 
   self._y=CanvasA-altezzaRana

  if self._y>30 and self._y<80 and self._x>30 and self._x<80:

   vite-=1
   self._x=int(CanvasL/2) 
   self._y=CanvasA-altezzaRana  

  if self._y>30 and self._y<80 and self._x>150 and self._x<210:

   vite-=1
   self._x=int(CanvasL/2) 
   self._y=CanvasA-altezzaRana 

  if self._y>30 and self._y<80 and self._x>280 and self._x<340:

   vite-=1
   self._x=int(CanvasL/2) 
   self._y=CanvasA-altezzaRana  

  if self._y>30 and self._y<80 and self._x>410 and self._x<470:

   vite-=1
   self._x=int(CanvasL/2) 
   self._y=CanvasA-altezzaRana  

  if self._y>30 and self._y<80 and self._x>540 and self._x<600:

   vite-=1
   self._x=int(CanvasL/2) 
   self._y=CanvasA-altezzaRana 

 def Muovi(self):
  self._x+=self._dx
  self._y+=self._dy

 def MovAvanti(self):
  self._dy-=self._speed
 def MovIndietro(self):
  self._dy+=self._speed
 def MovSinistra(self):
  self._dx-=self._speed
 def MovDestra(self):
  self._dx+=self._speed
 def Fermo(self):
  self._dx,self._dy=0,0

 def position(self)->(int,int):
  return self._x,self._y

class Vehicle():
 def __init__(self,x:int,y:int,dx:int,dy:int,speed:int):
  self._x,self._y,self._speed=x,y,speed

 def Muovi(self):
  self._x+=self._speed

 def MuoviIndietro(self):
  self._x-=self._speed

 def Controllo(self):
  if self._x>CanvasL:
   self._x=0
  if self._x<-20:
   self._x=CanvasL

 def position(self)->(int,int):
  return self._x,self._y
 
class macchinaRossa(Vehicle):
 def __init__(self,x,y,dx,dy,speed):
  Vehicle.__init__(self,x,y,dx,dy,speed)

 def CreaMacchinaRossa(self):
  g2d.draw_image(MacchinaRossa,(self._x,self._y))

class macchinaViola(Vehicle):
 def __init__(self,x,y,dx,dy,speed):
  Vehicle.__init__(self,x,y,dx,dy,speed)

 def CreaMacchinaViola(self):
  g2d.draw_image(MacchinaViola,(self._x,self._y))

class macchinaGialla(Vehicle):
 def __init__(self,x,y,dx,dy,speed):
  Vehicle.__init__(self,x,y,dx,dy,speed)

 def CreaMacchinaGialla(self):
  g2d.draw_image(MacchinaGialla,(self._x,self._y))

class trattore(Vehicle):
 def __init__(self,x,y,dx,dy,speed):
  Vehicle.__init__(self,x,y,dx,dy,speed)

 def CreaTrattore(self):
  g2d.draw_image(Trattore,(self._x,self._y))

class camion(Vehicle):
 def __init__(self,x,y,dx,dy,speed):
  Vehicle.__init__(self,x,y,dx,dy,speed)

 def CreaCamion(self):
  g2d.draw_image(Camion,(self._x,self._y))

class Raft():
 def __init__(self,x:int,y:int,dx:int,dy:int,speed:int):
  self._x,self._y,self._speed=x,y,speed

 def Muovi(self):
  self._x+=self._speed

 def MuoviIndietro(self):
  self._x-=self._speed

 def Controllo(self):
  if self._x>CanvasL:
   self._x=0
  if self._x<-150:
   self._x=CanvasL
   
 def position(self)->(int,int,int):
  return self._x,self._y,self._speed

class zatteraLunga(Raft):
 def __init__(self,x,y,dx,dy,speed):
  Raft.__init__(self,x,y,dx,dy,speed)

 def CreaZatteraLunga(self):
  g2d.draw_image(ZatteraLunga,(self._x,self._y))

class zatteraMedia(Raft):
 def __init__(self,x,y,dx,dy,speed):
  Raft.__init__(self,x,y,dx,dy,speed)

 def CreaZatteraMedia(self):
  g2d.draw_image(ZatteraMedia,(self._x,self._y))

class zatteraPiccola(Raft):
 def __init__(self,x,y,dx,dy,speed):
  Raft.__init__(self,x,y,dx,dy,speed)

 def CreaZatteraPiccola(self):
  g2d.draw_image(ZatteraPiccola,(self._x,self._y))

#Medoti 
def MenoVita():
  global vite 
  vite-=1

def Vita()->(int):
  return vite

def Punteggio()->(int):
  return punteggio




