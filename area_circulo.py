
import math


def area_circulo(radio):
    """
    Calcula el área de un círculo.

    Args:
        radio (int o float): Radio del círculo.

    Returns:
        float: Área del círculo.

    Raises:
        TypeError: Si el radio no es numérico o es booleano.
        ValueError: Si el radio es negativo o infinito.
    """
    if isinstance(radio, bool) or not isinstance(radio, (int, float)):
        raise TypeError("El radio debe ser un número.")

    if not math.isfinite(radio):
        raise ValueError("El radio debe ser un número finito.")

    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")

    return math.pi * radio ** 2
