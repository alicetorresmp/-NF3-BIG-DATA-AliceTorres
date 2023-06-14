#questão 2)

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/alicetorresmp/NF3-BIG-DATA-AliceTorres/main/cursos-prouni.csv')

#a
df['nota_integral_ampla'].fillna(0.0)
df['nota_integral_cotas'].fillna(0.0)
df['nota_parcial_ampla'].fillna(0.0)
df['nota_parcial_cotas'].fillna(0.0)

# b
# Agrupe os dados por Grau;
grupoGrau = df.groupby('grau')
print("Agrupado por Grau:")
for grau, grupo in grupoGrau:
  print(grupo)
  print("\n")


# c
# Agrupe pelos cursos Matemática, Medicina e Pedagogia;
cursos = ['Matemática', 'Medicina', 'Pedagogia']
grupoCursos = df[df['curso_busca'].isin(cursos)].groupby('curso_busca')
print(grupoCursos)


# d
# Agrupar os dados por Estado e obter a média de notas de corte por Estado
grupoEstadoCortes = df.groupby('uf_busca')['nota_integral_cotas'].mean()
print("\nAgrupado por Estado e média das notas:")
print(grupoEstadoCortes)


# e
# Agrupar os dados pelos cursos Tecnológicos
grupoTec = df[df['grau'] == 'Tecnológico']
print("\nAgrupado por cursos tecnológicos")
print(grupoTec)


# f
# Eliminar a coluna "cidade_filtro" do dataframe
df.drop(columns=['cidade_filtro'], inplace=True)
print("\nSem coluna cidade_filtro:")
print(df)


# g ]
# Apresentar a média das mensalidades dos cursos de Medicina
mediaMedicina = df.loc[df['curso_busca'] == 'Medicina', 'mensalidade'].mean()
print("\nMédia de mensalidade dos cursos de medicina")
print(mediaMedicina)


# h
# Média das notas de corte dos cursos de tempo integral
mediaCursoIntegral = df.loc[df['turno'] == 'Integral', 'nota_integral_cotas'].mean()
print("\nMédia das notas de corte dos cursos de tempo integral")
print(mediaCursoIntegral)


# i
# Estatística Descritiva das Notas Integral Ampla dos cursos de Bacharelado
estatisticaBac = df.loc[(df['grau'] == 'Bacharelado') & (df['turno'] == 'Integral'), 'nota_integral_ampla'].describe()
estatisticaBac = df.loc[(df['grau'] == 'Bacharelado') & (df['turno'] == 'Integral'), 'nota_integral_ampla'].describe()
print()

# j
# Gráfico comparativo entre o grau dos cursos pelas Notas Integral de Cotas
graf = df.groupby('grau')['nota_integral_cotas'].mean().plot.bar(xlabel='Grau dos Cursos', ylabel='Notas Integral de Cotas')
print(graf)