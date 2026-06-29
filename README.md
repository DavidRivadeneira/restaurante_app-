# Sistema de Gestión de Restaurante

**Estudiante:** Juan David Rivadeneira Cuascota
**Carrera:** Tecnologías de la Información
**Asignatura:** Programación Orientada a Objetos
**Actividad:** Taller Semana 5 - Organización modular de un sistema orientado a objetos en Python

## Descripción del sistema

Este proyecto implementa un sistema básico de gestión de restaurante utilizando Programación Orientada a Objetos en Python. El sistema permite registrar productos del menú (platos y bebidas) y clientes del restaurante, almacenarlos en listas administradas por una clase de servicio, y mostrar su información de forma organizada en consola.

El objetivo de la actividad no es construir una aplicación compleja, sino demostrar el uso correcto de identificadores descriptivos, convenciones de nombres en Python, tipos de datos básicos, listas como tipo de dato compuesto, clases, objetos, constructores, el método especial `__str__()` e importaciones entre módulos.

## Estructura del proyecto
restaurante_App/

├── modelos/

│   ├── init.py

│   ├── producto.py      -> Clase Producto

│   └── cliente.py       -> Clase Cliente

├── servicios/

│   ├── init.py

│   └── restaurante.py   -> Clase Restaurante (gestiona las listas)

└── main.py               -> Punto de arranque del programa
- **modelos/producto.py**: contiene la clase `Producto`, que representa un plato o bebida disponible en el restaurante.
- **modelos/cliente.py**: contiene la clase `Cliente`, que representa a una persona registrada en el sistema.
- **servicios/restaurante.py**: contiene la clase `Restaurante`, que administra las listas de productos y clientes mediante métodos como `agregar_producto`, `agregar_cliente`, `mostrar_productos` y `mostrar_clientes`.
- **main.py**: crea los objetos, los agrega al servicio principal y muestra la información registrada en consola.

## Tipos de datos utilizados

| Tipo  | Ejemplo de uso                                              |
|-------|--------------------------------------------------------------|
| str   | `nombre_producto`, `correo_electronico`, `codigo_cliente`    |
| int   | `cantidad_disponible`, `numero_visitas`                      |
| float | `precio_unitario`                                            |
| bool  | `es_vegetariano`, `es_miembro_vip`                            |
| list  | `lista_productos`, `lista_clientes`                          |

## Ejecución del programa

Desde la carpeta `restaurante_App`, ejecutar:

```bash
python main.py
```

## Reflexión

Utilizar identificadores descriptivos, tipos de datos adecuados y listas como estructuras compuestas resulta fundamental en un proyecto Python modular, ya que permite que el código sea legible, mantenible y fácil de extender. Un identificador claro comunica de inmediato el propósito de una variable o método sin necesidad de comentarios adicionales, mientras que el uso correcto de tipos de datos evita errores lógicos al operar con la información. Asimismo, las listas permiten administrar múltiples objetos de manera ordenada, lo cual es esencial en sistemas que, como este, deben escalar para representar muchos productos y clientes a la vez.