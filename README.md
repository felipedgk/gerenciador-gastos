# 💰 Gerenciador de Gastos Pessoais

[![CI](https://github.com/felipedgk/gerenciador-gastos/actions/workflows/ci.yml/badge.svg)](https://github.com/felipedgk/gerenciador-gastos/actions/workflows/ci.yml)

---

## 📌 Descrição do Problema

Uma grande parcela da população brasileira enfrenta dificuldades para controlar seus gastos mensais. Sem registro e acompanhamento, é comum gastar mais do que o planejado, acumular dívidas e perder a noção de para onde vai o dinheiro. Esse problema afeta especialmente jovens adultos, estudantes e trabalhadores de baixa renda, que não possuem acesso ou familiaridade com ferramentas financeiras complexas.

## 💡 Proposta da Solução

O **Gerenciador de Gastos Pessoais** é uma aplicação de linha de comando (CLI) simples, leve e sem necessidade de internet ou cadastro. Com ela, qualquer pessoa pode registrar seus gastos do dia a dia, categorizá-los, visualizar o total e entender melhor seus hábitos financeiros — diretamente pelo terminal.

## 👥 Público-alvo

- Estudantes universitários que querem controlar seus gastos mensais
- Trabalhadores que desejam organizar suas finanças sem usar apps complexos
- Qualquer pessoa que queira registrar despesas de forma simples e rápida

---

## ✨ Funcionalidades

- ➕ **Adicionar gasto** — registra descrição, valor e categoria
- 📄 **Listar gastos** — exibe todos os gastos ou filtra por categoria
- 💵 **Ver total** — calcula o total geral de gastos
- 📊 **Resumo por categoria** — mostra quanto foi gasto em cada categoria
- 🗑️ **Remover gasto** — remove um gasto pelo ID
- ✅ **Validações automáticas** — impede valores negativos, categorias inválidas e descrições vazias

**Categorias disponíveis:** `alimentacao`, `transporte`, `saude`, `educacao`, `lazer`, `moradia`, `outros`

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python 3.9+ | Linguagem principal |
| pytest | Testes automatizados |
| ruff | Análise estática de código (linting) |
| GitHub Actions | Integração contínua (CI) |

---

## ⚙️ Instalação

### Pré-requisitos

- Python 3.9 ou superior instalado
- pip (geralmente já vem com o Python)

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/felipedgk/gerenciador-gastos.git
cd gerenciador-gastos

# 2. (Opcional, mas recomendado) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

---

## ▶️ Execução

```bash
# A partir da pasta raiz do projeto
python src/app.py
```

Você verá o menu principal:

```
==================================================
   💰 GERENCIADOR DE GASTOS PESSOAIS v1.0.0
==================================================

Bem-vindo! Controle seus gastos de forma simples e rápida.

📋 MENU PRINCIPAL
------------------------------
  1. Adicionar gasto
  2. Listar gastos
  3. Ver total
  4. Resumo por categoria
  5. Remover gasto
  0. Sair
------------------------------
Escolha uma opção:
```

---

## 🧪 Rodando os Testes

```bash
# Executar todos os testes com detalhes
pytest tests/ -v
```

Saída esperada:

```
tests/test_gastos.py::TestAdicionar::test_adicionar_gasto_valido PASSED
tests/test_gastos.py::TestAdicionar::test_adicionar_valor_negativo_levanta_erro PASSED
...
20 passed in 0.XXs
```

---

## 🔍 Rodando o Lint

```bash
# Verificar qualidade do código com ruff
ruff check src/
```

Se não houver problemas, o comando retorna sem saída (sucesso silencioso).

---

## 📁 Estrutura do Projeto

```
gerenciador-gastos/
├── src/
│   ├── __init__.py
│   ├── app.py          # Interface CLI (menu e interações)
│   └── gastos.py       # Lógica de negócio
├── tests/
│   ├── __init__.py
│   └── test_gastos.py  # Testes automatizados (20+ casos)
├── .github/
│   └── workflows/
│       └── ci.yml      # Pipeline de CI
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── README.md
├── pyproject.toml      # Configuração do projeto e do ruff
└── requirements.txt    # Dependências
```

---

## 🔄 Versão

**1.0.0** — Versão inicial com funcionalidades completas de CRUD de gastos.

Consulte o [CHANGELOG](CHANGELOG.md) para histórico de mudanças.

---

## 👤 Autor

**Felipe Camargo Do Nascimento**  
📂 Repositório: [https://github.com/felipedgk/gerenciador-gastos](https://github.com/SEU-USUARIO/gerenciador-gastos)
