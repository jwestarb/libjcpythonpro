import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['jwestarb@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'julio.ti@acsc.org.br',
        'Cursos Python Pro',
        'Teste de envio de um e-mail.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foobar.com.br']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'julio.ti@acsc.org.br',
            'Cursos Python Pro',
            'Teste de envio de um e-mail.'
        )
