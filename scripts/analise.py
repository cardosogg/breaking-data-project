import pandas as pd

df = pd.read_csv("dados/eventos.csv")

print("===== TABELA COMPLETA =====")
print(df)

print("\n===== TOTAL DE EVENTOS =====")
print(len(df))

print("\n===== EVENTOS POR CATEGORIA =====")
print(df["categoria"].value_counts())

print("\n===== EVENTOS POR CIDADE =====")
print(df["cidade"].value_counts())

print("\n===== MAIOR PONTUAÇÃO =====")
print(df["pontos"].max())

print("\n===== MENOR PONTUAÇÃO =====")
print(df["pontos"].min())

print("\n===== MÉDIA DE PONTOS =====")
print(df["pontos"].mean())

print("\n===== RANKING =====")

ranking = df.sort_values(
    by="pontos",
    ascending=False
)

print(ranking[["vencedor", "pontos"]])
