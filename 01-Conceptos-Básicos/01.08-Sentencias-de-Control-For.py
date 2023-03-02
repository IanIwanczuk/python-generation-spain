for x in range(5, 0, -1):
    print(f"Número {x}")

citricos = ["naranja", "limón", "pomelo", "líma", "mandarina"]
print(citricos)
print(citricos[3])
print(f"Número de valores: {len(citricos)}")
print("")

for x in range(0, 4, 1):
    print(f"{x}: {citricos[x]}")
print("")

for x in range(4):
    print(f"{x}: {citricos[x]}")
print("")

for x in range(0, len(citricos), 1):
    print(f"{x}: {citricos[x]}")
print("")

for x in range(len(citricos)):
    print(f"{x}> {citricos[x]}")
print("")

for x in citricos:
    print(f"{x}")
print("")
