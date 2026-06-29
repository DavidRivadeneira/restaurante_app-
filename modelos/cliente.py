# modelos/cliente.py
# Esta clase representa a un cliente registrado en el sistema del restaurante.


class Cliente:
    """Representa a un cliente registrado en el restaurante."""

    def __init__(
        self,
        codigo_cliente: str,
        nombre_completo: str,
        correo_electronico: str,
        numero_visitas: int,
        es_miembro_vip: bool,
    ) -> None:
        # Identificador unico del cliente (ejemplo: "C001")
        self.codigo_cliente: str = codigo_cliente

        # Nombre completo del cliente
        self.nombre_completo: str = nombre_completo

        # Correo electronico de contacto del cliente
        self.correo_electronico: str = correo_electronico

        # Numero de veces que el cliente ha visitado el restaurante
        self.numero_visitas: int = numero_visitas

        # Indica si el cliente pertenece al programa de membresia VIP
        self.es_miembro_vip: bool = es_miembro_vip

    def registrar_visita(self) -> None:
        """Incrementa en uno el numero de visitas del cliente."""
        self.numero_visitas += 1

    def calcular_descuento(self) -> float:
        """Calcula el porcentaje de descuento segun el tipo de cliente."""
        if self.es_miembro_vip:
            return 0.15
        return 0.0

    def __str__(self) -> str:
        # Representacion legible del cliente para mostrar en consola
        estado_membresia = "VIP" if self.es_miembro_vip else "Regular"
        return (
            f"[{self.codigo_cliente}] {self.nombre_completo} - "
            f"{self.correo_electronico} - Visitas: {self.numero_visitas} "
            f"- ({estado_membresia})"
        )