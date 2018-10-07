import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tier Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    # Setup
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    # Tier Down
    sessao_obj.roll_back()
    sessao_obj.fechar()
