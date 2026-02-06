# %% 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%

df = pd.read_csv("data/points_tmw.csv")
df.head()

# %%

group_prod = (df.groupby("descProduto")["idTransacao"]
              .count().reset_index())
group_prod = group_prod.sort_values(by="idTransacao")

# %%

plt.grid(True)
sns.barplot(group_prod, x="idTransacao", y="descProduto")
plt.xlabel("Quantidade Transações")
plt.ylabel("Produto")
plt.title("Frequência de Produtos")
plt.show()

# %%

df["dataTransacao"] = pd.to_datetime(df["dtTransacao"]).dt.date
group_data = df.groupby("dataTransacao").agg(
    {
        "qtdPontos": "sum",
        "idTransacao": "count",
    }
).reset_index()

group_data = group_data.sort_values(by="dataTransacao")

plt.figure(figsize=(8,6))
plt.plot(group_data["dataTransacao"], group_data["idTransacao"])
plt.ylabel("Qtde. Transações")
plt.title("Série Histórica de Transações")

# %%

plt.hist(group_data["qtdPontos"], bins=18)
plt.xlabel("Pontos")
plt.show()

# %%

plt.boxplot(group_data["qtdPontos"])
plt.title("Box-plot")
plt.ylabel("Pontos")

# %%

sns.scatterplot(group_data, x="qtdPontos", y="idTransacao")
