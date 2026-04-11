"""Módulo de lógica de negócio do gerenciador de gastos."""

from datetime import date


CATEGORIAS_VALIDAS = [
    "alimentacao",
    "transporte",
    "saude",
    "educacao",
    "lazer",
    "moradia",
    "outros",
]


class GerenciadorGastos:
    """Gerencia a lista de gastos do usuário."""

    def __init__(self):
        self._gastos = []
        self._proximo_id = 1

    def adicionar(self, descricao: str, valor: float, categoria: str) -> dict:
        """Adiciona um novo gasto.

        Args:
            descricao: Descrição do gasto.
            valor: Valor do gasto (deve ser positivo).
            categoria: Categoria do gasto.

        Returns:
            O gasto adicionado como dicionário.

        Raises:
            ValueError: Se o valor for inválido ou a categoria não existir.
        """
        descricao = descricao.strip()
        if not descricao:
            raise ValueError("A descrição não pode ser vazia.")

        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        categoria = categoria.strip().lower()
        if categoria not in CATEGORIAS_VALIDAS:
            raise ValueError(
                f"Categoria inválida. Escolha uma de: {', '.join(CATEGORIAS_VALIDAS)}"
            )

        gasto = {
            "id": self._proximo_id,
            "descricao": descricao,
            "valor": round(valor, 2),
            "categoria": categoria,
            "data": str(date.today()),
        }
        self._gastos.append(gasto)
        self._proximo_id += 1
        return gasto

    def listar(self, categoria: str = None) -> list:
        """Retorna todos os gastos, opcionalmente filtrados por categoria."""
        if categoria:
            categoria = categoria.strip().lower()
            return [g for g in self._gastos if g["categoria"] == categoria]
        return list(self._gastos)

    def remover(self, gasto_id: int) -> dict:
        """Remove um gasto pelo ID.

        Returns:
            O gasto removido.

        Raises:
            ValueError: Se o ID não for encontrado.
        """
        for i, gasto in enumerate(self._gastos):
            if gasto["id"] == gasto_id:
                return self._gastos.pop(i)
        raise ValueError(f"Gasto com ID {gasto_id} não encontrado.")

    def total(self, categoria: str = None) -> float:
        """Calcula o total dos gastos, opcionalmente por categoria."""
        gastos = self.listar(categoria)
        return round(sum(g["valor"] for g in gastos), 2)

    def resumo_por_categoria(self) -> dict:
        """Retorna o total gasto por cada categoria."""
        resumo = {}
        for gasto in self._gastos:
            cat = gasto["categoria"]
            resumo[cat] = round(resumo.get(cat, 0) + gasto["valor"], 2)
        return resumo
