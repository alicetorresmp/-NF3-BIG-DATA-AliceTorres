#questão 1)

import pandas as pd
#questão 1)

url = "world_alcohol.csv"
df = pd.read_csv(url)

#a
# Agrupe os dados por tipo de bebidas;
grupoBebidas = df.groupby('Beverage Types')
print("Agrupado por tipo de bebidas:")
for grupo, dados in grupoBebidas:
    print("\nGrupo:", grupo)
    print("Dados:")
    print(dados)

#b
# Agrupe os dados por Região e por Ano;
grupoRegiaoAno = df.groupby(['WHO region', 'Year'])
print("Agrupado por Região e Ano:")
for grupo, dados in grupoRegiaoAno:
    print("\nGrupo:", grupo)
    print("Dados:")
    print(dados)

#c
# Seção de Contagens: Contar a ocorrência de Regiões, de Países e a soma da coluna de valores
# por Bebida
contRegiao = df['WHO region'].nunique()
contPais = df['Country'].nunique()
somaPorBebidas = df.groupby('Beverage Types')['Display Value'].sum()
print("\nSoma por tipo de bebidas:")
print(somaPorBebidas)

#d
#Realize análises estatísticas da coluna dos valores: Média, Moda, Mediana, Estatística
#Descritiva e Gráfico de comparação dos valores agrupados por tipo de bebida.
media = df['Display Value'].mean()
moda = df['Display Value'].mode()
mediana = df['Display Value'].median()
descricao = df['Display Value'].describe()
print("\nEstatísticas descritivas:")
print(descricao)
df.groupby('Beverage Types')['Display Value'].sum().plot(kind='bar')

#e
# Mostre resultados de acordo com alguns critérios:
#i
# Mostrar a coluna de bebidas do ano de 1985.
bebidas1985 = df.loc[df['Year'] == 1985, 'Beverage Types']
print("\nBebidas do ano de 1985:")
print(bebidas1985)

#ii
# Mostrar a coluna de Região com valores acima de 4
regioesMaisDe4 = df.loc[df['Display Value'] > 4, 'WHO region']
print("\nRegiões com valores acima de 4:")
print(regioesMaisDe4)