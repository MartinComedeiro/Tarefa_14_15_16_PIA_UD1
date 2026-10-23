print("Dime tu edad")
edad = int(input())

print("Dime tus ingresos")
ingresos = int(input())

if edad >= 16:
    if ingresos>= 1000:
        print("Tienes que tributar")
    else:
        print("Tienes que tener unos ingresos de ḿás de 1000$")
     
else:
    print("tienes que ser mayor de 16 años")
