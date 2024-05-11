from cliente import Clientes
from producto.productos import Producto

class Tienda:
    def __init__(self):
        self.compras = []

    def agregar_producto(self, producto):
        self.compras.append(producto)

    def mostrar_productos_disponibles(self):
        print("Productos disponibles:")
        print("1. Remera - $800")
        print("2. Campera - $1800")
        print("3. Pantalon - $1500")
        print("4. Champion - $5500")

    def calcular_total(self):
        total = sum(producto.precio for producto in self.compras)
        return total

def main():
    # Crear un cliente
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de teléfono: ")
    cliente1 = Clientes(nombre, apellido, correo, telefono)
    print(cliente1)

    tienda = Tienda()
    seguir_comprando = True

    while seguir_comprando:
        tienda.mostrar_productos_disponibles()
        opcion = input("Selecciona el producto que deseas comprar (1/2/3/4): ")
        
        if opcion in ['1', '2', '3', '4']:
            productos = {
                '1': Producto("Remera", 800),
                '2': Producto("Campera", 1800),
                '3': Producto("Pantalon", 1500),
                '4': Producto("Champion", 5500)
            }
            producto_seleccionado = productos[opcion]
            tienda.agregar_producto(producto_seleccionado)
            print(f"Has agregado {producto_seleccionado} a tu compra.")
        else:
            print("Opción inválida. Por favor selecciona un número válido.")

        respuesta = input("¿Deseas agregar algo más a tu compra? (si/no): ")
        if respuesta.lower() != "si":
            seguir_comprando = False
    total = tienda.calcular_total()
    print(f"\nTotal a pagar: ${total}")

    metodo_pago = input("¿Deseas pagar en efectivo o con tarjeta?: ")
    if metodo_pago.lower() == "efectivo":
        monto_efectivo = float(input(f"¿Con cuanto vas a pagar? (${total:.2f}): "))
        if monto_efectivo >= total:
            cambio = monto_efectivo - total
            print(f"Gracias por su compra. Aquí tiene su cambio: ${cambio:.2f}")
        else:
            print("El monto en efectivo no es suficiente.")
    elif metodo_pago.lower() == "tarjeta":
        pin = input("Pin y verde porfavor: ")
        print("LISTO!. ¡Disfrute su compra!")
    else:
        print("Método de pago no válido.")

if __name__ == "__main__":
    main()