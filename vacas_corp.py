class Vaca:
    def __init__(self, nombre, codigo, raza, peso, next = None):
        self.nombre = nombre
        self.codigo = codigo
        self.raza = raza
        self.peso = peso
        self.next = next

class VacasCorp:
    def __init__(self):
        self.head_produccion = None
        self.head_reemplazo = None
    def agregar_vaca(self, nombre, codigo, raza, peso, reemplazo = False):
        nueva_vaca = Vaca(nombre, codigo, raza, peso)
        
        if reemplazo:
            if self.head_reemplazo is None:
                self.head_reemplazo = nueva_vaca
            else:
                actual = self.head_reemplazo
                while actual.next:
                    actual = actual.next
                actual.next = nueva_vaca
        
        else:
            if self.head_produccion is None:
                self.head_produccion = nueva_vaca
            else:
                actual = self.head_produccion
                while actual.next:
                    actual = actual.next
                actual.next = nueva_vaca

    def mostrar_vacas(self, reemplazo = False):
        actual = self.head_reemplazo if reemplazo else self.head_produccion
        lista = "Reemplazo" if reemplazo else "produccion"
        print(f"\nVacas en {lista}:")
        while actual is not None:
            print(f"Nombre: {actual.nombre}, Codigo: {actual.codigo}, Raza: {actual.raza}, Peso: {actual.peso} Kg")
            actual = actual.next

    def listar_vacas_menor_peso(self, peso_limite):
        actual = self.head_produccion
        while actual:
            if actual.peso < peso_limite:
                print(f"Nombre: {actual.nombre}, Codigo: {actual.codigo}, Raza: {actual.raza}, Peso: {actual.peso}")
            actual = actual.next


    def nueva_vaca_posicion(self, nombre, codigo, raza, peso, posicion):
        nueva_vaca = Vaca(nombre, codigo, raza, peso)
        if posicion == 1:
            nueva_vaca.next = self.head_produccion
            self.head_produccion = nueva_vaca
            return
        
        actual = self.head_produccion
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
        
    def reemplazar_vaca(self, codigo_vaca):
        if not self.head_produccion or not self.head_reemplazo:
            print("No hay vacas para ser reempladas")
            return
        
        actual = self.head_produccion
        anterior = None

        while actual and actual.codigo != codigo_vaca:
            anterior = actual
            actual = actual.next
        
        if actual is None:
            print("La vaca no fue encotrada en la produccion")
            return
        
        print(f"Reemplazando vaca {actual.nombre} (Codigo {actual.codigo})")
        
        vaca_reemplazo = self.head_reemplazo
        self.head_reemplazo = self.head_reemplazo.next
        vaca_reemplazo.next = actual.next

        if anterior:
            anterior.next = vaca_reemplazo
        else:
            self.head_produccion = vaca_reemplazo

    def listar_vacas_nombre(self):
        actual = self.head_produccion
        print("\nListado de nombres de las vacas en produccion:")
        while actual:
            print(actual.nombre)
            actual = actual.next

vacas_corp = VacasCorp()

for i in range(1,31):
    vacas_corp.agregar_vaca(f"Vaca{i}", i, "Holstein", 400 + i * 5)

for i in range(31, 51):
    vacas_corp.agregar_vaca(f"Reemplazo{i}", i, "Jersey", 380 + i * 5, reemplazo = True)

vacas_corp.mostrar_vacas()
vacas_corp.mostrar_vacas(reemplazo = True)

print("\nReemplazar vacas con codigo 5")
vacas_corp.reemplazar_vaca(5)
vacas_corp.mostrar_vacas()

print("\nVacas con peso menor a 470 Kg:")
vacas_corp.listar_vacas_menor_peso(470)

print("\nNueva vaca en la posicion 1:")
vacas_corp.nueva_vaca_posicion("Rosa", 5, "Angus", 460, 1)
vacas_corp.mostrar_vacas()

vacas_corp.listar_vacas_nombre()
