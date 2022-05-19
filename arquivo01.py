import pandas as pd

#dataframe = pd.DataFrame() # metodo de criar uma tabela dataframe vazia

venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50, 70],
         }

#DICA = QUANDO VC QUISER GERAR UM DATAFRAME - CRIE UMA VARIAVEL COM O ALGUMA COISA QUE IDENTIFIQUE, NESSE CASO " vendas_df "

vendas_df = pd.DataFrame(venda) # Transformar os dados do dicionário em um dataframe.

print(vendas_df)# print df
