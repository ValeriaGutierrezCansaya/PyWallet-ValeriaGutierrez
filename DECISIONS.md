# Decisions

## Decisión 1: Implementación de la función `crear_cuenta`

**Fecha:** 15/10/2026

### Contexto

La función `crear_cuenta` es una de las operaciones principales
de la billetera digital porque permite registrar nuevas cuentas
dentro del sistema.

La plantilla inicial utilizaba los parámetros genéricos
`*args` y `**kwargs`, los cuales no describían
claramente qué datos eran necesarios para la creación
de una cuenta.

### Decisión

Se decidió reemplazar los parámetros genéricos por
parámetros explícitos relacionados con el dominio del
problema.

La función fue diseñada para recibir la información
necesaria mediante los parámetros `numero_cuenta`,
`titular` y `saldo_inicial`.

También se incorporaron validaciones antes de registrar
una cuenta en la base de datos.

Las validaciones verifican que el número de cuenta y el
titular sean obligatorios, que el saldo inicial no sea
negativo y que la cuenta no exista previamente.

### Justificación

El uso de parámetros explícitos mejora la legibilidad
del código y permite comprender con mayor facilidad
qué información requiere la función.

Además, facilita la detección de errores durante el
desarrollo y simplifica el mantenimiento futuro del
sistema.

Las validaciones previas ayudan a preservar la
integridad de la información almacenada y reducen
la posibilidad de registrar datos inválidos o
duplicados.

### Principios de Clean Code aplicados

- Uso de nombres descriptivos para los parámetros.
- Eliminación de parámetros genéricos.
- Validación temprana de datos de entrada.
- Prevención de registros duplicados.
- Aplicación del principio de responsabilidad única.
- Mejora de la legibilidad y mantenibilidad.

### Beneficios

- Mayor claridad en la interfaz de la función.
- Reducción de errores por uso incorrecto.
- Mejor mantenibilidad del código.
- Facilidad para futuras ampliaciones.
- Cumplimiento de buenas prácticas de Clean Code.

### Cambio realizado

La versión inicial utilizaba los parámetros genéricos
`*args` y `**kwargs`.

Estos fueron reemplazados por los parámetros
`numero_cuenta`, `titular` y `saldo_inicial`.

Además, se implementaron validaciones para evitar
datos inválidos y la creación de cuentas duplicadas
dentro de la estructura `base_datos["cuentas"]`.

La cuenta se registra únicamente cuando todas las
validaciones se completan correctamente.
