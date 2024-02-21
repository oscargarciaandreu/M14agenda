def agenda():
  contactes{
  "oscar garcia": "625931706",
  "nabil azariouh": "680624564"
  }
  sortir = true
  while(sortir):
    print("MENU AGENDA")
    print("1.Afegir contacte")
    print("2.Veure contactes")
    print("3.Eliminar contacte")
    print("4.Cerca de contactes")
    print("5.Desar contactes")
    print("6.Carregar contactes")
    print("7.Sortir")
    
    eleccion = input("Escoge una de estas opciones")
    
    ###
    No especificamos el input de numero como integro porque esperamos que introduzcan el prefijo
    ###
    if eleccion == "1":
      print("Menu afegir contacte")
      nombre=input("Nom: ")
      Numero=input("Número: ")
      contactes[(Nom)] = numero
      if Nombre = in contactes:
        print("Problema al dessar un conctacte ya existent")
    elif eleccion == "2":
      for contacte in contactes:
        for numero in contactes:
          print("Nom | Número")
    elif eleccion == "3":
    
    elif eleccion == "4":
    
    elif eleccion == "5":
    
    elif eleccion == "6":
    
    elif eleccion == "7"
  
    else:
      print("La eleccion que has elegido no coincide con ningun numero")
