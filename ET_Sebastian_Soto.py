
import csv 
import random
import math
import os
os.system("cls")
sueldos = []

trabajadores = [
    {'nombre': 'Juan Perez'},
    {'nombre': 'Maria Garcia'},
    {'nombre': 'Carlos Lopez'},
    {'nombre': 'Ana Martinez'},
    {'nombre': 'Pedro Rodriguez'},
    {'nombre': 'Laura Hernandez'},
    {'nombre': 'Miguel Sanchez'},
    {'nombre': 'Isabel Gomez'},
    {'nombre': 'Francisco Diaz'},
    {'nombre': 'Elena Fernandez'}
]

def asignar_sueldo():
    os.system("cls")
    if len(sueldos)<10:
        for trabajador in trabajadores:
            sueldo = random.randint(300000, 2500000)
            sueldos.append(sueldo)
        print(sueldos)
    else:
        sueldos.clear()
        for trabajador in trabajadores:
            sueldo = random.randint(300000, 2500000)
            sueldos.append(sueldo)
        print(sueldos)
    

def clasificacion():
    os.system("cls")
    print('Clasificación de sueldo\n')
    print('Sueldos menores a $800.000:\n')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            print(f"Nombre: {trabajador['nombre']} | Sueldo: ${sueldo}")
    print('\nSueldos entre $800.000 y $2.000.000:\n')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo >800000 and sueldo<=2000000:
            print(f"Nombre: {trabajador['nombre']} | Sueldo: ${sueldo}")
    print('\nSueldos superiores a $2.000.000\n')
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo > 2000000:
            print(f"Nombre: {trabajador['nombre']} | Sueldo: ${sueldo}")

def ver_estadisticas():
    os.system("cls")
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    sueldo_promedio = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))
    print(f'Sueldo más alto: ${sueldo_max}')
    print(f'Sueldo más bajo: ${sueldo_min}')
    print(f'Promedio de sueldos: {sueldo_promedio}')
    print(f'Media geométrica de sueldo: {sueldo_geom}')

def reporte_de_sueldos():
    os.system("cls")
    try:
        with open('archivo_trab.csv', 'w', newline='') as archivo_trab:
            escritor = csv.writer(archivo_trab)
            encabezado = ['Nombre Empleado', 'Sueldo Base', 'Desc Salud', 'Desc AFP', 'Sueldo Bruto']
            escritor.writerow(encabezado)
            for trabajador, sueldo in zip(trabajadores, sueldos):
                salud = (sueldo * 7) / 100
                afp = (sueldo * 12) / 100
                sueldo_bruto = sueldo - salud - afp
                escritor.writerow([trabajador['nombre'], sueldo, int(salud), int(afp), int(sueldo_bruto)])
                print(f"Nombre:{trabajador['nombre']}, Sueldo: ${sueldo}, Salud: ${salud},AFP: ${afp}, Sueldo Total: ${sueldo_bruto}")
    except:
        print("No se han asignado los sueldos, no se puede crear el archivo")

def salir_programa():
    print('Finalizando el programa...')
    print('Desarrollado por Sebastián Soto')
    print('RUT 21.918.877-3')

def programa_principal():
    try:
        while True:
            print('1.- Asignar sueldo')
            print('2.- Clasificación de sueldo')
            print('3.- Estadísticas')
            print('4.- Reporte de sueldo')
            print('5.- Salir')
            opcion = int(input('Seleccione una opción: '))
            if opcion == 1:
                asignar_sueldo()
            elif opcion == 2:
                clasificacion()
            elif opcion == 3:
                ver_estadisticas()
            elif opcion == 4:
                reporte_de_sueldos()
            elif opcion == 5:
                salir_programa()
                break
            else:
                os.system("cls")
                print('opción inválida')
    except:
        os.system("cls")
        print("opción inválida")
        programa_principal()

programa_principal()