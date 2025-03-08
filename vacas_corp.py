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
            print(f"Nombre: {actual.nombre}, Codigo: {actual.codigo}, Raza: {actual.raza}, Peso{actual.peso} Kg")
            actual = actual.next

vacas_corp = VacasCorp()

vacas_corp.agregar_vaca("Juanita", 1, "Holstein", 500)  

vacas_corp.mostrar_vacas()