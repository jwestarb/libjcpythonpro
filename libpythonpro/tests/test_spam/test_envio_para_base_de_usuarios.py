from unittest.mock import Mock
import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [Usuario(nome='Julio', email='jwestarb@gmail.com'), Usuario(nome='Adriana', email='jwestarb@gmail.com')],
        [Usuario(nome='Julio', email='jwestarb@gmail.com')]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'jwestarb@gmail.com',
        'Assunto do E-mail',
        'Corpo do E-mail.'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Julio', email='jwestarb@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'julio.westarb@acsc.org.br',
        'Assunto do E-mail',
        'Corpo do E-mail.'
    )
    enviador.enviar.assert_called_once_with(
        'julio.westarb@acsc.org.br',
        'jwestarb@gmail.com',
        'Assunto do E-mail',
        'Corpo do E-mail.'
    )
