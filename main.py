# main.py
# Punto de arranque del sistema de gestion de restaurante.

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def main() -> None:
    # Se crea el objeto principal del servicio, encargado de administrar las listas
    restaurante_central: Restaurante = Restaurante("Sabor Andino")

    # Creacion de al menos dos objetos de tipo Producto
    producto_uno: Producto = Producto(
        codigo_producto="P001",
        nombre_producto="Locro de papa",
        precio_unitario=4.50,
        cantidad_disponible=20,
        es_vegetariano=True,
    )

    producto_dos: Producto = Producto(
        codigo_producto="P002",
        nombre_producto="Seco de pollo",
        precio_unitario=6.75,
        cantidad_disponible=15,
        es_vegetariano=False,
    )

    # Creacion de al menos dos objetos de tipo Cliente
    cliente_uno: Cliente = Cliente(
        codigo_cliente="C001",
        nombre_completo="Maria Fernanda Suarez",
        correo_electronico="maria.suarez@correo.com",
        numero_visitas=3,
        es_miembro_vip=True,
    )

    cliente_dos: Cliente = Cliente(
        codigo_cliente="C002",
        nombre_completo="Andres Tobar",
        correo_electronico="andres.tobar@correo.com",
        numero_visitas=1,
        es_miembro_vip=False,
    )

    # Se agregan los objetos creados a las listas administradas por el servicio
    restaurante_central.agregar_producto(producto_uno)
    restaurante_central.agregar_producto(producto_dos)
    restaurante_central.agregar_cliente(cliente_uno)
    restaurante_central.agregar_cliente(cliente_dos)

    # Se muestra la informacion registrada de forma organizada en consola
    print(restaurante_central)
    print()
    restaurante_central.mostrar_productos()
    print()
    restaurante_central.mostrar_clientes()
    print()

    # Se muestran algunos calculos adicionales para demostrar el uso de los metodos
    valor_total_inventario: float = restaurante_central.calcular_valor_total_inventario()
    total_clientes_vip: int = restaurante_central.contar_clientes_vip()

    print(f"Valor total del inventario: ${valor_total_inventario:.2f}")
    print(f"Cantidad de clientes VIP: {total_clientes_vip}")


# Punto de entrada estandar de un script en Python
if __name__ == "__main__":
    main()