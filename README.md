# desafio_ETL_santander
Código de compleção do desafio de código de ETL do curso de Ciência de Dados do Santander da DIO.

#Importação das bibliotecas necessárias para o funcionamento do código.

import pandas as pd
import numpy as np

##Etapa de extração:
##Utilização da biblioteca pandas para a extração dos dados do arquivo csv.

df = pd.read_csv("usuarios.csv")
tabela = pd.DataFrame(users)

#Etapa de transformação:
##Criação de uma nova coluna Status com um valor condicionado pelos dados apresentados pelo primeiro arquivo, com o intuito de simular uma análise de crédito.

def analise_de_credito():
    tabela.insert(loc=6,column="Status", value=np.where(tabela["Saldo"]>=1000,"Concedido","Negado"))

analise_de_credito()

#Etapa de carregamento:
##Criação de um novo arquivo csv com as mudanças feitas através da função previamente declarada.

tabela.to_csv("usuarios_novo.csv", index=False)

