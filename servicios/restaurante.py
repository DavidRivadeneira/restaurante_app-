# servicios/restaurante.py
# Esta clase administra las listas de productos y clientes del restaurante.

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Gestiona los productos y clientes registrados en el restaurante."""

    def __init__(self, nombre_restaurante: str) -> None:
        # Nombre del establecimiento
        self.nombre_restaurante: str = nombre_restaurante

        # Lista compuesta que almacena objetos de tipo Producto
        self.lista_productos: list[Producto] = []

        # Lista compuesta que almacena objetos de tipo Cliente
        self.lista_clientes: list[Cliente] = []

    def agregar_producto(self, producto_nuevo: Producto) -> None:
        """Agrega un nuevo producto a la lista del restaurante."""
        self.lista_productos.append(producto_nuevo)

    def agregar_cliente(self, cliente_nuevo: Cliente) -> None:
        """Agrega un nuevo cliente a la lista del restaurante."""
        self.lista_clientes.append(cliente_nuevo)

    def calcular_valor_total_inventario(self) -> float:
        """Calcula el valor total del inventario disponible."""
        valor_total: float = 0.0
        for producto_actual in self.lista_productos:
            valor_total += producto_actual.precio_unitario * producto_actual.cantidad_disponible
        return valor_total

    def contar_clientes_vip(self) -> int:
        """Cuenta cuantos clientes registrados son miembros VIP."""
        total_vip: int = 0
        for cliente_actual in self.lista_clientes:
            if cliente_actual.es_miembro_vip:
                total_vip += 1
        return total_vip

    def mostrar_productos(self) -> None:
        """Muestra en consola la informacion de todos los productos registrados."""
        print(f"--- Productos de {self.nombre_restaurante} ---")
        for producto_actual in self.lista_productos:
            print(producto_actual)

    def mostrar_clientes(self) -> None:
        """Muestra en consola la informacion de todos los clientes registrados."""
        print(f"--- Clientes de {self.nombre_restaurante} ---")
        for cliente_actual in self.lista_clientes:
            print(cliente_actual)

    def __str__(self) -> str:
        return (
            f"Restaurante: {self.nombre_restaurante} - "
            f"{len(self.lista_productos)} productos, "
            f"{len(self.lista_clientes)} clientes"
        )