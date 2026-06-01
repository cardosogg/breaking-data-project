import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/eventos.csv")

df["categoria"].value_counts().plot(
    kind="bar"
)

plt.title(
    "Eventos por Categoria"
)

plt.show()