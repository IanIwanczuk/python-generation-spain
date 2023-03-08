#####################################################################
# Procesamiento Síncrono                                            #
#####################################################################
def main():
    print("Hola ....")
    print("... Mundo !!!")

print("Inicio Sync")
main()
print("Fin Sync")  
print("")

#####################################################################
# Procesamiento Asíncrono                                           #
#####################################################################
import asyncio, time

async def main():
    print("Inicio Main")
    await asyncio.gather(func1(), func2())    
    print("Fin Main")

async def func1():
    print("Inicio Func1")
    for i in range(11):
        print(i)
        await asyncio.sleep(0.6)
    print("Fin Func1")

async def func2():
    print("Inicio Func2")
    print("Hola ....")    
    await asyncio.sleep(5)
    print("... Mundo !!!")
    print("Fin Func2")

print("Inicio Async")
tiempo = time.perf_counter()
asyncio.run(main())
tiempoElapsed = time.perf_counter() - tiempo
print(f"Ejecutado en {tiempoElapsed:0.2f} segundos")
print("Fin Async")