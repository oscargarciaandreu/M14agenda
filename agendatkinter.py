import tkinter as tk

def afegir_contacte():
    Nom = entry_nom.get()
    Numero = entry_numero.get()
    if Nom.strip() == "" or Numero.strip() == "":
        return
    if Nom in contactes:
        print("Problema al afegir un contacte ja existent")
    else:
        contactes[Nom] = Numero
        entry_nom.delete(0, tk.END)
        entry_numero.delete(0, tk.END)

def veure_contactes():
    for Nom, Numero in contactes.items():
        print(Nom, Numero)

def cerca_contactes():
    buscar = entry_cerca.get()
    if buscar in contactes:
        print("Contacte:", buscar, ", Numero:", contactes[buscar])
    else:
        print("El contacte no existeix")

def eliminar_contacte():
    eliminar = entry_eliminar.get()
    if eliminar in contactes:
        del contactes[eliminar]
        print("Contacte", eliminar, "eliminat amb èxit")
    else:
        print("El contacte no existeix")

contactes = {}

root = tk.Tk()
root.title("Agenda")

label_nom = tk.Label(root, text="Nom:")
label_nom.grid(row=0, column=0)
entry_nom = tk.Entry(root)
entry_nom.grid(row=0, column=1)

label_numero = tk.Label(root, text="Número:")
label_numero.grid(row=1, column=0)
entry_numero = tk.Entry(root)
entry_numero.grid(row=1, column=1)

btn_afegir = tk.Button(root, text="Afegir contacte", command=afegir_contacte)
btn_afegir.grid(row=2, column=0, columnspan=2)

btn_veure = tk.Button(root, text="Veure contactes", command=veure_contactes)
btn_veure.grid(row=3, column=0, columnspan=2)

label_cerca = tk.Label(root, text="Cerca contacte:")
label_cerca.grid(row=4, column=0)
entry_cerca = tk.Entry(root)
entry_cerca.grid(row=4, column=1)
btn_cerca = tk.Button(root, text="Cerca", command=cerca_contactes)
btn_cerca.grid(row=5, column=0, columnspan=2)

label_eliminar = tk.Label(root, text="Eliminar contacte:")
label_eliminar.grid(row=6, column=0)
entry_eliminar = tk.Entry(root)
entry_eliminar.grid(row=6, column=1)
btn_eliminar = tk.Button(root, text="Eliminar", command=eliminar_contacte)
btn_eliminar.grid(row=7, column=0, columnspan=2)

root.mainloop()
