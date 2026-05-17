"""Módulo para buscar cotação do dólar via AwesomeAPI."""

import urllib.request
import json


def buscar_cotacao_dolar():
    """Busca a cotação atual do dólar via AwesomeAPI."""
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            dados = json.loads(response.read().decode())
            cotacao = dados["USDBRL"]["bid"]
            return float(cotacao)
    except Exception:
        return None


def exibir_cotacao():
    """Exibe a cotação do dólar formatada."""
    valor = buscar_cotacao_dolar()
    if valor:
        print(f"💵 Cotação do dólar hoje: R$ {valor:.2f}")
    else:
        print("⚠️  Não foi possível obter a cotação do dólar.")