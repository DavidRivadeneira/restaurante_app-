# modelos/producto.py
# Esta clase representa un producto (plato o bebida) disponible en el restaurante.


class Producto:
    """Representa un producto del menu del restaurante."""

    def __init__(
        self,
        codigo_producto: str,
        nombre_producto: str,
        precio_unitario: float,
        cantidad_disponible: int,
        es_vegetariano: bool,
    ) -> None:
        # Identificador unico del producto (ejemplo: "P001")
        self.codigo_producto: str = codigo_producto

        # Nombre descriptivo del producto (ejemplo: "Ceviche de camaron")
        self.nombre_producto: str = nombre_producto

        # Precio de venta del producto, expresado en dolares
        self.precio_unitario: float = precio_unitario

        # Cantidad de unidades disponibles en inventario
        self.cantidad_disponible: int = cantidad_disponible

        # Indica si el producto es apto para dietas vegetarianas
        self.es_vegetariano: bool = es_vegetariano

    def actualizar_inventario(self, unidades_vendidas: int) -> None:
        """Reduce la cantidad disponible cuando se vende el producto."""
        if unidades_vendidas <= self.cantidad_disponible:
            self.cantidad_disponible -= unidades_vendidas

    def esta_disponible(self) -> bool:
        """Indica si todavia hay unidades disponibles del producto."""
        return self.cantidad_disponible > 0

    def __str__(self) -> str:
        # Representacion legible del producto para mostrar en consola
        condicion_dieta = "vegetariano" if self.es_vegetariano else "no vegetariano"
        return (
            f"[{self.codigo_producto}] {self.nombre_producto} - "
            f"${self.precio_unitario:.2f} - Stock: {self.cantidad_disponible} "
            f"- ({condicion_dieta})"
        )