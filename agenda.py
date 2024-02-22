def agenda():
  contactes={
    "Nom":"Numero",
    }
  sortir = True
  while(sortir):
      print("MENU AGENDA")
      print("1.Afegir contacte")
      print("2.Veure contactes")
      print("3.Cerca de contactes")
      print("4.Eliminar contacte")
      print("5.Desar contactes")
      print("6.Carregar contactes")
      print("7.Sortir")
      
      eleccion = input("Escoge una de estas opciones")
      
      """
      No especificamosel input de numero como integro porque esperamos que introduzcan el prefijo
      """
      
      if eleccion == "1":
        print("Menu afegir contacte")
        Nom=input("Nom: ")
        if Nom in contactes:
          print("Problema al dessar un conctacte ya existent")
          continue
        Numero=input("Numero: ")
        contactes[(Nom)] = Numero
      elif eleccion == "2":
        print("Menu veure contactes")
        for contacte in contactes:
          for Numero in contactes:
            print("contacte / numero")
            print(Numero,contactes[contacte])
      elif eleccion == "3":
        print("Menu cerca contactes")
        buscar=input ("contacte a cercar: ")
        print(contactes[buscar])
        if buscar not in contactes:
          print("El contacte no existeix, dessal en el menu")
          continue
      elif eleccion == "4":
        eliminar = input("Contacte a eliminar: ")
        if contacte not in contactes:
          print("El contacte no existeig afegeixlo")
          continue
        del(contactes[eliminar])
        print("contacte",eliminar,"eliminat amb exit")    
agenda()
