# %% 

import pandas as pd

df = pd.read_csv("data/points_tmw.csv")
df.head()

# %%

print("Estatísticas de Posição para Transações:\n")

minimo = df["qtdPontos"].min()
print(f"Mínimo: {minimo}")

media = df["qtdPontos"].mean()
print(f"Média: {media}")

quartil_1 = df["qtdPontos"].quantile(0.25)
print(f"1° Quartil: {quartil_1}")

mediana = df["qtdPontos"].median()
print(f"Mediana: {mediana}")

quartil_3 = df["qtdPontos"].quantile(0.75)
print(f"3° Quartil: {quartil_3}")

maximo = df["qtdPontos"].max()
print(f"Máximo: {maximo}")

df["qtdPontos"].describe()

# %%

print("\n---------------------------------------\n")
print("Estatísticas de Posição para Usuários:\n")

usuarios = df.groupby(["idUsuario"]).agg(
    {
        "idTransacao":"count",
        "qtdPontos":"sum",
    }
).reset_index()

# %%

sumario = usuarios[['idTransacao', 'qtdPontos']].describe()
print(sumario.to_string())
