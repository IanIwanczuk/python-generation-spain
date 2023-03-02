for x in range(0, 20, 1):
    print(f"Número: {x} - Inicio")
    if (x == 10):
        break
    print(f"Número: {x} - Fin")

citricos = ["naranja", "limón", "pomelo", "líma", "mandarina"]
for x in citricos:
    if(x == "limón"):
        continue
    print(f"{x}")
print("")
