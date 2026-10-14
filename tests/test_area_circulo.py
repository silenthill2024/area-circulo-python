
import math
import pytest

from area_circulo import area_circulo


def test_area_circulo_caso_correcto():
    """Comprueba el área de un círculo con radio 5."""
    assert area_circulo(5) == pytest.approx(math.pi * 25)


def test_area_circulo_radio_cero():
    """Comprueba que un radio de cero produzca un área de cero."""
    assert area_circulo(0) == 0


def test_area_circulo_radio_negativo():
    """Comprueba que un radio negativo genere un error."""
    with pytest.raises(ValueError):
        area_circulo(-5)


def test_area_circulo_entrada_incorrecta():
    """Comprueba que una entrada de texto genere un error."""
    with pytest.raises(TypeError):
        area_circulo("cinco")


if __name__ == "__main__":
    pytest.main()
