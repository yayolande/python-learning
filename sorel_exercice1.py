# CREATION DES CLASSES

class plat:
   def __init__(self,nom_plat, sauce, complement, viande, poisson, crustace, fruit, legume):
    	self.nom_plat = nom_plat
    	self.sauce = sauce
    	self.complement = complement
    	self.viande = viande
    	self.poisson = poisson
    	self.crustace = crustace
    	self.fruit = fruit
    	self.legume = legume
    
   def show(self):
      print("nom:", self.nom_plat)
      print("sauce:", self.sauce)
      print("complement:", self.complement)
      if self.viande != None:
         print("viande:", self.viande)
      if self.poisson != None:
         print("poisson:", self.poisson)
         print("crustace:", self.crustace)
         print("fruit:", self.fruit)
         print("legume:", self.legume)

class sauce:
   def __init__(self, nom_sauce, couleur):
      self.nom_sauce = nom_sauce
      self.couleur_sauce = couleur

class complement:
   def __init__(self, nom_complement):
      self.nom_complement = nom_complement
      

class viande:
   def __init__(self, nom_viande):
      self.nom_viande = nom_viande

class poisson:
   def __init__(self, nom_poisson):
      self.nom_poisson = nom_poisson

class crustace:
   def __init__(self, nom_crustace):
      self.nom_crustace = nom_crustace

class fruit:
   def __init__(self, nom_fruit):
      self.nom_fruit = nom_fruit

class legume:
   def __init__(self, nom_legume):
      self.nom_legume = nom_legume
        
# INSTACIATION DES CLASSES DONC CREATIONS DES OBJETS
    
sauce1 = sauce(sauce de dja ou m'gbagba)
sauce2 = sauce(sauce d'epinard a la viande)
sauce3 = sauce(sauce Ademe)
sauce4 = sauce(sauce gboma dessi)
sauce5 = sauce(sauce d'arachide, marron)
sauce6 = sauce(sauce fontêtê)
sauce7 = sauce(sauce tomate, rouge)
sauce8 = sauce(sauce au poisson frais)
sauce9 = sauce(sauce de boeuf au curry)
sauce10 = sauce(sauce Ayimolou)

complement1 = complement(frite d'igname)
complement2 = complement(patate douce)
complement3 = complement(riz)
complement4 = complement(foufou)
complement5 = complement(plantain mur)
complement6 = complement(tubercule de manioc)
complement7 = complement(couscous)

viande1 = viande(poulet)
viande2 = viande(viande de boeuf)
viande3 = viande(viande de veau)
viande4 = viande(viande de l'agneau)
viande5 = viande(pintade)
viande6 = viande(viande de porc)

poisson1 = poisson(crevette)
poisson2 = poisson(thon)
poisson3 = poisson(poisson fume)
poisson4 = poisson(maquereau)

crustace1 = crustace(crabe)

legume1 = legume(feuille d'aubergine)
legume2 = legume(salade a la togolaise)
legume3 = legume(poivron)
legume4 = legume(tomate achee)
legume5 = legume(epinard)
legume6 = legume(courgette)
    
plat = []
p1 = plat(crevette aux poivrons, none, none, none, poisson1, none, poivrons)
P1.show()
p2 = plat(salade de poulet marine au gingembre et au citron, none, complement4, viande1, none, none, none)
p2.show()
p3 = plat(frite d'igname, none, complement1, none, none, none, none)
p3.show()
p4 = plat(sauce de dja ou m'gbagba, sauce1, complement3, none, none, none, none, legume4)
p4.show()
p5 = plat(sauce d'epinard a la viande, sauce2, complement4, viande2, none, none, legume5)
p5.show()
p6 = plat(veloute de patate douce au arachide, sauce5, complement2, none, none, none, none)
p6.show()
p7 = plat(pintade djenkoume, sauce7, complement4, viande5, none, none, none)
p7.show()
p8 = plat(thon marine au courgette, none, complement3, none, poisson2, none, legume6)
p8.show()
p9 = plat(sauce ademe, sauce3, complement7, none, poisson1, crustace1, none)
p9.show()
p10 = plat(gboma dessi, sauce7, complement4, viande2, poisson3, crustace1, legume4)
p10.show()
p11 = plat(pinon, sauce7, complement3, viande6, none, none, legume4)
p11.show()
p12 = plat(foufou sauce d'arachide, sauce5, complement4, viande2, none, none, none)
p12.show()
p13 = plat(ayimolou, sauce10, complement3, none, none, none, none)
p13.show()
p14 = plat(kom, none, complement4, none, poisson4, none,none)
p14.show()
plat.append(p10)
i=0
while i < len(plat):
   plat[i].show()
   print()
   print()
   i+=1,
    
    
