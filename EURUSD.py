# Importando bibliotecas

import yfinance as yf
import pandas as pd

#Criando uma função

def analise_quantitativa_eurusd():

# Agora iremos definir um período para nossa análise
    data_inicio = pd.Timestamp.now() - pd.DateOffset(years=1)
    data_fim = pd.Timestamp.now()

# Obtendo os dados históricos do eurusd

    eurusd = yf.download('EURUSD = X', start=data_inicio, end=data_fim)

# Calcular algumas métricas quantitativas

    média_preço = eurusd['Adj Close'].mea()
    volatilidade = eurusd['Adj Close'].std()
    retorno_diario = eurusd['Adj Close'].pct_change().dropna()
    retorno_anualizado = retorno_diario.mean() * 252 # 252 é o número médio de dias de negociação em um ano

# Calcular o máximo e minimo do preço durante o período analisado
    preco_máximo = eurusd['Adj Close'].max()
    preco_minimo = eurusd['Adj Close']. min()

# Calcular o retorno total durante o periodo analisado

    retorno_total = (eurusd['Adj Close'].iloc[-1] / eurusd['Adj Close']. iloc[0]-1) * 100

# Imprimindo os resultados

    print(f'Análise quantitativa do par EURUSD')
    print(f'Período: {data_inicio.strftime('%Y-%m-%d')} a {data_fim.strftime('%Y-%m-%d')}')
    print(f'Média do preço: {media_preco:.4f}')
    print(f'Volatilidade: {volatilidade:.4f}')
    print(f'Retorno Anualizado: { retorno_anualizado:.4f} (em %)')
    print(f'Preço Máximo: {preco_máximo:.4f}')
    print(f'Preço Mínimo: {preco_minimo:.4f}')
    print(f'Retorno total no período: {retorno_total:.4f}%')


if __name__ == "__main__":
    analise_quantitativa_eurusd()
   

 


  