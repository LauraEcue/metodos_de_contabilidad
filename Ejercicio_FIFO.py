class FIFO:
    def _init_(self):
        self.turnos = []

    def adicionar(self, turno):
        self.turnos.append(turno)

    def atender(self):
        if self.cantidad() > 0:
            return self.turnos.pop(0)
        return None

    def siguiente(self):
        if self.cantidad() > 0:
            return self.turnos[0]
        return None

    def ultimo(self):
        if self.cantidad() > 0:
            return self.turnos[-1]
        return None

    def cantidad(self):
        return len(self.turnos)


dijiturno = FIFO()
numero_turno = 1

while True:
    print("\n--- DIJITURNO ---")
    print("1. Adicionar turno")
    print("2. Atender turno")
    print("3. Mirar el siguiente turno")
    print("4. Mirar el último turno")
    print("5. Mirar la cantidad de turnos")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        dijiturno.adicionar(numero_turno)
        print("Turno agregado:", numero_turno)
        numero_turno += 1

    elif opcion == "2":
        turno = dijiturno.atender()
        if turno is None:
            print("No hay turnos para atender.")
        else:
            print("Atendiendo el turno:", turno)

    elif opcion == "3":
        turno = dijiturno.siguiente()
        if turno is None:
            print("No hay turnos en espera.")
        else:
            print("El siguiente turno es:", turno)

    elif opcion == "4":
        turno = dijiturno.ultimo()
        if turno is None:
            print("No hay turnos en espera.")
        else:
            print("El último turno es:", turno)

    elif opcion == "5":
        print("Turnos en espera:", dijiturno.cantidad())

    elif opcion == "6":
        print("Programa terminado.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")