import json

frutas = ["naranja", "limón", "pomelo", "líma", "mandarina"]
frutasJSON = json.dumps(frutas)

print(frutas)
print(f"Posición 2 frutas {frutas[2]}")
print(type(frutas))
print("")

print(frutasJSON)
print(f"Posición 2 de frutasJSON: {frutasJSON[2]}")
print(type(frutasJSON))
print("")

frutas2 = json.loads(frutasJSON)
print(frutas2)
print(type(frutas2))
print(f"Posición 2 frutas2: {frutas2[2]}")