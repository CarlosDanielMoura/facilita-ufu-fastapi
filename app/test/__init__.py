import pytest

# Suprimir o aviso específico durante os testes
@pytest.fixture(autouse=True)
def suppress_warnings():
    with pytest.warns(None) as warnings:
        yield

# Outras configurações
