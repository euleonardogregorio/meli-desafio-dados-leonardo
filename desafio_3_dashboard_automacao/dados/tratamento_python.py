import pandas as pd


# 1. Carregar o CSV original

df = pd.read_csv("/Users/red/Desktop/DEV/meli-desafio-dados-leonardo/desafio_3_dashboard_automacao/dashboard/resultado_query.csv")

col_produtos = "TOP_3_PERFORMANCE_VENDAS"


# 2. Explodir os produtos da coluna Z

# Dividir a string
df["produtos_lista"] = df[col_produtos].str.split(",")

# Criar uma linha por produto
df_explodido = df.explode("produtos_lista").reset_index(drop=True)

# Renomear a coluna para PRODUTO
df_explodido = df_explodido.rename(columns={"produtos_lista": "PRODUTO"})

# Remover espaços
df_explodido["PRODUTO"] = df_explodido["PRODUTO"].str.strip()

# 3. Exportar o CSV final
output_file = "produtos_explodidos.csv"
df_explodido.to_csv(output_file, index=False, encoding="utf-8")

print("Arquivo gerado com sucesso!")
print(f"Salvo como: {output_file}")

print(df_explodido.head(10))
