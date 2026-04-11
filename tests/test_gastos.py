"""Testes automatizados do gerenciador de gastos."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from gastos import GerenciadorGastos


@pytest.fixture
def gerenciador():
    """Retorna uma instância limpa do gerenciador para cada teste."""
    return GerenciadorGastos()


# ── Testes de adição ──────────────────────────────────────────────────────────

class TestAdicionar:
    def test_adicionar_gasto_valido(self, gerenciador):
        gasto = gerenciador.adicionar("Almoço", 35.50, "alimentacao")
        assert gasto["descricao"] == "Almoço"
        assert gasto["valor"] == 35.50
        assert gasto["categoria"] == "alimentacao"
        assert gasto["id"] == 1

    def test_adicionar_gera_ids_sequenciais(self, gerenciador):
        g1 = gerenciador.adicionar("Café", 5.0, "alimentacao")
        g2 = gerenciador.adicionar("Ônibus", 4.5, "transporte")
        assert g1["id"] == 1
        assert g2["id"] == 2

    def test_adicionar_valor_negativo_levanta_erro(self, gerenciador):
        with pytest.raises(ValueError, match="maior que zero"):
            gerenciador.adicionar("Teste", -10.0, "alimentacao")

    def test_adicionar_valor_zero_levanta_erro(self, gerenciador):
        with pytest.raises(ValueError, match="maior que zero"):
            gerenciador.adicionar("Teste", 0, "alimentacao")

    def test_adicionar_descricao_vazia_levanta_erro(self, gerenciador):
        with pytest.raises(ValueError, match="vazia"):
            gerenciador.adicionar("   ", 10.0, "alimentacao")

    def test_adicionar_categoria_invalida_levanta_erro(self, gerenciador):
        with pytest.raises(ValueError, match="Categoria inválida"):
            gerenciador.adicionar("Teste", 10.0, "categoria_inexistente")

    def test_adicionar_arredonda_centavos(self, gerenciador):
        gasto = gerenciador.adicionar("Teste", 10.999, "outros")
        assert gasto["valor"] == 11.0


# ── Testes de listagem ────────────────────────────────────────────────────────

class TestListar:
    def test_listar_retorna_todos(self, gerenciador):
        gerenciador.adicionar("A", 10.0, "alimentacao")
        gerenciador.adicionar("B", 20.0, "transporte")
        assert len(gerenciador.listar()) == 2

    def test_listar_vazio(self, gerenciador):
        assert gerenciador.listar() == []

    def test_listar_por_categoria(self, gerenciador):
        gerenciador.adicionar("Almoço", 30.0, "alimentacao")
        gerenciador.adicionar("Ônibus", 5.0, "transporte")
        gerenciador.adicionar("Jantar", 40.0, "alimentacao")
        resultado = gerenciador.listar("alimentacao")
        assert len(resultado) == 2
        assert all(g["categoria"] == "alimentacao" for g in resultado)

    def test_listar_categoria_sem_gastos_retorna_vazio(self, gerenciador):
        gerenciador.adicionar("Almoço", 30.0, "alimentacao")
        assert gerenciador.listar("lazer") == []


# ── Testes de remoção ─────────────────────────────────────────────────────────

class TestRemover:
    def test_remover_gasto_existente(self, gerenciador):
        gerenciador.adicionar("Café", 5.0, "alimentacao")
        removido = gerenciador.remover(1)
        assert removido["descricao"] == "Café"
        assert len(gerenciador.listar()) == 0

    def test_remover_id_inexistente_levanta_erro(self, gerenciador):
        with pytest.raises(ValueError, match="não encontrado"):
            gerenciador.remover(999)

    def test_remover_nao_afeta_outros_gastos(self, gerenciador):
        gerenciador.adicionar("A", 10.0, "alimentacao")
        gerenciador.adicionar("B", 20.0, "transporte")
        gerenciador.remover(1)
        restantes = gerenciador.listar()
        assert len(restantes) == 1
        assert restantes[0]["descricao"] == "B"


# ── Testes de total ───────────────────────────────────────────────────────────

class TestTotal:
    def test_total_vazio(self, gerenciador):
        assert gerenciador.total() == 0.0

    def test_total_geral(self, gerenciador):
        gerenciador.adicionar("A", 10.0, "alimentacao")
        gerenciador.adicionar("B", 20.0, "transporte")
        assert gerenciador.total() == 30.0

    def test_total_por_categoria(self, gerenciador):
        gerenciador.adicionar("Almoço", 30.0, "alimentacao")
        gerenciador.adicionar("Jantar", 50.0, "alimentacao")
        gerenciador.adicionar("Ônibus", 5.0, "transporte")
        assert gerenciador.total("alimentacao") == 80.0
        assert gerenciador.total("transporte") == 5.0

    def test_total_apos_remocao(self, gerenciador):
        gerenciador.adicionar("A", 100.0, "outros")
        gerenciador.adicionar("B", 50.0, "outros")
        gerenciador.remover(1)
        assert gerenciador.total() == 50.0


# ── Testes de resumo ──────────────────────────────────────────────────────────

class TestResumo:
    def test_resumo_vazio(self, gerenciador):
        assert gerenciador.resumo_por_categoria() == {}

    def test_resumo_agrupa_por_categoria(self, gerenciador):
        gerenciador.adicionar("A", 10.0, "alimentacao")
        gerenciador.adicionar("B", 20.0, "alimentacao")
        gerenciador.adicionar("C", 15.0, "transporte")
        resumo = gerenciador.resumo_por_categoria()
        assert resumo["alimentacao"] == 30.0
        assert resumo["transporte"] == 15.0
