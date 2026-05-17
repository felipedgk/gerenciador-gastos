"""Interface CLI do Gerenciador de Gastos Pessoais."""

from gastos import GerenciadorGastos, CATEGORIAS_VALIDAS
from cotacao import exibir_cotacao


def limpar_tela():
    print("\n" + "=" * 50)


def exibir_cabecalho():
    print("=" * 50)
    print("   💰 GERENCIADOR DE GASTOS PESSOAIS v1.0.0")
    print("=" * 50)


def exibir_menu():
    print("\n📋 MENU PRINCIPAL")
    print("-" * 30)
    print("  1. Adicionar gasto")
    print("  2. Listar gastos")
    print("  3. Ver total")
    print("  4. Resumo por categoria")
    print("  5. Remover gasto")
    print("  0. Sair")
    print("-" * 30)


def obter_float(prompt: str) -> float:
    """Solicita um número decimal do usuário com validação."""
    while True:
        try:
            valor = float(input(prompt).strip().replace(",", "."))
            return valor
        except ValueError:
            print("❌ Digite um número válido (ex: 25.90)")


def obter_categoria() -> str:
    """Exibe as categorias disponíveis e retorna a escolhida."""
    print("\nCategorias disponíveis:")
    for i, cat in enumerate(CATEGORIAS_VALIDAS, 1):
        print(f"  {i}. {cat}")
    while True:
        try:
            opcao = int(input("Escolha o número da categoria: ").strip())
            if 1 <= opcao <= len(CATEGORIAS_VALIDAS):
                return CATEGORIAS_VALIDAS[opcao - 1]
            print(f"❌ Digite um número entre 1 e {len(CATEGORIAS_VALIDAS)}")
        except ValueError:
            print("❌ Digite um número válido.")


def acao_adicionar(gerenciador: GerenciadorGastos):
    print("\n➕ ADICIONAR GASTO")
    descricao = input("Descrição: ").strip()
    valor = obter_float("Valor (R$): ")
    categoria = obter_categoria()
    try:
        gasto = gerenciador.adicionar(descricao, valor, categoria)
        print(f"\n✅ Gasto adicionado! ID: {gasto['id']} | {gasto['descricao']} — R$ {gasto['valor']:.2f}")
    except ValueError as e:
        print(f"❌ Erro: {e}")


def acao_listar(gerenciador: GerenciadorGastos):
    print("\n📄 LISTAR GASTOS")
    print("Filtrar por categoria? (deixe em branco para ver todos)")
    filtro = input("Categoria (ou Enter): ").strip().lower()

    gastos = gerenciador.listar(filtro if filtro else None)

    if not gastos:
        print("  Nenhum gasto encontrado.")
        return

    print(f"\n{'ID':<5} {'Descrição':<25} {'Categoria':<15} {'Valor':>10}  {'Data'}")
    print("-" * 70)
    for g in gastos:
        print(f"  {g['id']:<4} {g['descricao']:<25} {g['categoria']:<15} R$ {g['valor']:>8.2f}  {g['data']}")
    print("-" * 70)
    print(f"  {'Total:':>47} R$ {gerenciador.total(filtro if filtro else None):>8.2f}")


def acao_total(gerenciador: GerenciadorGastos):
    print("\n💵 TOTAL DE GASTOS")
    total = gerenciador.total()
    print(f"  Total geral: R$ {total:.2f}")


def acao_resumo(gerenciador: GerenciadorGastos):
    print("\n📊 RESUMO POR CATEGORIA")
    resumo = gerenciador.resumo_por_categoria()
    if not resumo:
        print("  Nenhum gasto registrado ainda.")
        return
    print(f"\n  {'Categoria':<20} {'Total':>12}")
    print("  " + "-" * 34)
    for cat, total in sorted(resumo.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat:<20} R$ {total:>9.2f}")
    print("  " + "-" * 34)
    print(f"  {'TOTAL GERAL':<20} R$ {gerenciador.total():>9.2f}")


def acao_remover(gerenciador: GerenciadorGastos):
    print("\n🗑️  REMOVER GASTO")
    gastos = gerenciador.listar()
    if not gastos:
        print("  Nenhum gasto para remover.")
        return

    acao_listar(gerenciador)
    try:
        gasto_id = int(input("\nDigite o ID do gasto a remover (0 para cancelar): ").strip())
        if gasto_id == 0:
            print("  Operação cancelada.")
            return
        gasto = gerenciador.remover(gasto_id)
        print(f"✅ Gasto '{gasto['descricao']}' removido com sucesso.")
    except ValueError as e:
        print(f"❌ Erro: {e}")


def main():
    gerenciador = GerenciadorGastos()
    exibir_cabecalho()
    exibir_cotacao()
    print("\nBem-vindo! Controle seus gastos de forma simples e rápida.\n")

    acoes = {
        "1": acao_adicionar,
        "2": acao_listar,
        "3": acao_total,
        "4": acao_resumo,
        "5": acao_remover,
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("\n👋 Até logo! Cuide bem das suas finanças.\n")
            break
        elif opcao in acoes:
            limpar_tela()
            acoes[opcao](gerenciador)
        else:
            print("❌ Opção inválida. Digite um número do menu.")


if __name__ == "__main__":
    main()