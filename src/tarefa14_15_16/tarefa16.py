print("Dime tu nombre")
nombre = input()
inicial = nombre[0:1].capitalize()

print("Dime tu sexo (H | M)")
sexo = input()

if sexo == "M":
    if inicial <= "M":
        print("Eres del grupo A")
    else:
        print("Eres del grupo B")
     
else:
    if inicial <= "M":
        print("Eres del grupo B")
    else:
        print("Eres del grupo A")
