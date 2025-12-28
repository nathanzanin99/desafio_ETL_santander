import pandas as pd
import numpy as np
df = pd.read_csv("usuarios.csv")
user_ids = df['ID'].tolist()


users = df.to_dict(orient='records')
tabela = pd.DataFrame(users)


def analise_de_credito():
    tabela.insert(loc=6,column="Status", value=np.where(tabela["Saldo"]>=1000,"Concedido","Negado"))



analise_de_credito()
print(tabela)


tabela.to_csv("usuarios_novo.csv", index=False)

