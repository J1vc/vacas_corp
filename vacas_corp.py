class Vaca:
    def __init__(self, nombre, codigo, raza, peso, next = None):
        self.nombre = nombre
        self.codigo = codigo
        self.raza = raza
        self.peso = peso
        self.next = next

class VacasCorp:
    def __init__(self):
        self.head = None

    def agregar_vaca(self, nombre, codigo, raza, peso):
        nueva_vaca = Vaca(nombre, codigo, raza, peso)
        if self.head is None:
            self.head = nueva_vaca
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nueva_vaca
            

    def mostrar_vacas(self):
        actual = self.head
        while actual is not None:
            print(f"Nombre: {actual.nombre}, Codigo: {actual.codigo}, Raza: {actual.raza}, Peso: {actual.peso} Kg")
            actual = actual.next

    def listar_vacas_menor_peso(self,peso_limite):
        actual = self.head
        while actual:
            if actual.peso < peso_limite:
                print(f"Nombre: {actual.nombre}, Codigo: {actual.codigo}, Raza: {actual.raza}, Peso: {actual.peso}")
            actual = actual.next

    def nueva_vaca_posicion(self, nombre, codigo, raza, peso, posicion):
        nueva_vaca = Vaca(nombre, codigo, raza, peso)
        if posicion == 1:
            nueva_vaca.next = self.head
            self.head = nueva_vaca
            return
        
        actual = self.head
        contador = 1

        while actual and contador < posicion - 1:
            actual = actual.next
            contador += 1

        if actual is None:
            print("Posicion invalida. Se agregara al final")
            self.agregar_vaca(nombre, codigo, raza, peso)
        else:
            nueva_vaca.next = actual.next
            actual.next = nueva_vaca

vacas_corp = VacasCorp()

vacas_corp.agregar_vaca("Juanita", 1, "Pardo Suizo", 500) 
vacas_corp.agregar_vaca("Pedro", 2, "Normando", 450)
vacas_corp.agregar_vaca("Marta", 3, "Holstein", 470)
vacas_corp.agregar_vaca("Juana", 4, "Jersey", 480)

vacas_corp.mostrar_vacas()

print("\nVacas con peso menor a 470 Kg:")
vacas_corp.listar_vacas_menor_peso(470)

print("\nNueva vaca en la posicion 3:")
vacas_corp.nueva_vaca_posicion("Rosa", 5, "Angus", 460, 3)
vacas_corp.mostrar_vacas()