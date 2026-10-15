# pylint: disable=invalid-name

"""
Proyecto Integrador: Billetera Digital

Practica Semana 1 - Clean Code
Plantilla inicial para auditoria del modulo.
"""

base_datos = {
    "cuentas": {},
    "transacciones": {}
}


def crear_cuenta(numero_cuenta, titular, saldo_inicial=0.0):
    """
    Crea una nueva cuenta en la billetera digital.

    Args:
        numero_cuenta (str): Identificador único de la cuenta.
        titular (str): Nombre del titular.
        saldo_inicial (float): Saldo inicial de la cuenta.

    Returns:
        bool: True si la cuenta fue creada correctamente.
        False en caso contrario.
    """

    if not numero_cuenta:
        print("Error: El número de cuenta es obligatorio.")
        return False

    if not titular:
        print("Error: El nombre del titular es obligatorio.")
        return False

    if saldo_inicial < 0:
        print("Error: El saldo inicial no puede ser negativo.")
        return False

    if numero_cuenta in base_datos["cuentas"]:
        print("Error: La cuenta ya existe.")
        return False

    base_datos["cuentas"][numero_cuenta] = {
        "titular": titular,
        "saldo": saldo_inicial
    }

    print("Cuenta creada correctamente.")
    return True


def depositar_dinero(numero_cuenta, monto):
    """
    Deposita dinero en una cuenta existente.
    """

    raise NotImplementedError(
        "La función depositar_dinero aún no ha sido implementada."
    )


def transferir_fondos(cuenta_origen, cuenta_destino, monto):
    """
    Transfiere fondos entre dos cuentas.
    """

    raise NotImplementedError(
        "La función transferir_fondos aún no ha sido implementada."
    )


def consultar_saldo(numero_cuenta):
    """
    Consulta el saldo de una cuenta.
    """

    raise NotImplementedError(
        "La función consultar_saldo aún no ha sido implementada."
    )


def cerrar_cuenta(numero_cuenta):
    """
    Cierra una cuenta existente.
    """

    raise NotImplementedError(
        "La función cerrar_cuenta aún no ha sido implementada."
    )
