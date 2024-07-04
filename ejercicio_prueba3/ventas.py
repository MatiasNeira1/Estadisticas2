import globales
import math
import os
import random


def asignar_venta_aleatoria():
    todas_las_ventas=globales.leer_archivo_json('ventas.json')
    todos_los_empleados=globales.leer_archivo_json('empleados.json')

    for i in range(10):
        empleado=random.choice(todos_los_empleados)

        nombre_empleado=empleado['nombre']
        ventas=random.randint(1500000,5000000)

        venta_aleatoria={
            "nombre": nombre_empleado,
            "ventas": ventas
        }
        todas_las_ventas.append(venta_aleatoria)
    globales.guardar_archivo_json('ventas.json', todas_las_ventas)

def venta_mas_alta():
    todas_las_ventas=globales.leer_archivo_json('ventas.json')
    todos_los_empleados=globales.leer_archivo_json('empleados.json')

    venta_ordenada=sorted(todas_las_ventas, key=lambda x:x['ventas'], reverse=True)
    nombre_empleado=""
    for venta in venta_ordenada[:1]:
        nombre_empleado=""
        ventas=0
        for empleado in todos_los_empleados:
            if empleado['nombre']==venta['nombre']:
                nombre_empleado=f"{empleado['nombre']}"
                ventas=f"{venta['ventas']}"
    print(f"La venta mas alta es del empleado {nombre_empleado} y el total de la venta es de ${ventas}")







def venta_mas_baja():
    todas_las_ventas=globales.leer_archivo_json('ventas.json')
    todos_los_empleados=globales.leer_archivo_json('empleados.json')

    ventas_ordenadas=sorted(todas_las_ventas, key=lambda x: x['ventas'], reverse=False)

    for venta in ventas_ordenadas[:1]:
        empleados=""
        ventas=0
        for empleado in todos_los_empleados:
            if empleado['nombre']==venta['nombre']:
                empleados=f"{empleado['nombre']}"
                ventas=f"{venta['ventas']}"
    print(f"La venta mas alta de es del empleado {empleados} y el total de la venta es de {ventas}")





def promedio_ventas():
    todas_las_ventas=globales.leer_archivo_json('ventas.json')

    suma_ventas=0
    cantidad_ventas=0

    for venta in todas_las_ventas:

        suma_ventas+=venta['ventas']
        cantidad_ventas+=1

        promedio_ventas= suma_ventas / cantidad_ventas

    print(f"El promedio de las ventas es de ${int(promedio_ventas)}")





def media_geometrica():
    todas_las_ventas=globales.leer_archivo_json('ventas.json')

    suma_ventas=0
    cantidad_ventas=0

    for venta in todas_las_ventas:
        suma_ventas+=math.log(venta['ventas'])
        cantidad_ventas+=1

        media_geometrica=math.exp(suma_ventas/cantidad_ventas)

    print(f"La meadia geometrica de las ventas es ${int(media_geometrica)}")







def menu_estadisticas():
    os.system("cls")
    while True:
        print("1. Venta mas alta")
        print("2. Venta mas baja")
        print("3. Promedio de ventas")
        print("4. Media Geometrica")
        print("5. Salir")

        opcion=globales.seleccionar_opcion(5)

        if opcion==1:
            venta_mas_alta()
        elif opcion==2:
            venta_mas_baja()
        elif opcion==3:
            promedio_ventas()
        elif opcion==4:
            media_geometrica()
        elif opcion==5:
            print("SALIR")
            return
        input("Presione ENTER para continuar")
        


def menu_principal():
    os.system("cls")
    while True:
        print("1. Asignar ventas aleatorias.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa")

        opcion=globales.seleccionar_opcion(3)

        if opcion==1:
            asignar_venta_aleatoria()
        elif opcion==2:
            menu_estadisticas()
        elif opcion==3:
            input("Presione ENTER para continuar")
        return
menu_principal()


