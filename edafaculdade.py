import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
file_path = 'C:\\Users\\matheus\\Documents\\earthquake_data_tsunami.csv'  
df = pd.read_csv(file_path)

# 1. Informações gerais sobre o dataset
print("Informações gerais sobre o dataset:")
df_info = df.info()
print(df_info)

# Verificar dados ausentes
print("\nDados ausentes por coluna:")
missing_data = df.isnull().sum()
print(missing_data)

# 2. Estatísticas descritivas
print("\nEstatísticas descritivas:")
stats = df.describe()
print(stats)

# 3. Visualizações

# 3.1. Distribuição das magnitudes
plt.figure(figsize=(8, 6))
sns.histplot(df['magnitude'], bins=30, kde=True, color='blue')
plt.title('Distribuição das Magnitudes dos Terremotos')
plt.xlabel('Magnitude')
plt.ylabel('Frequência')
plt.show()

# 3.2. Relação entre Magnitude e Ocorrência de Tsunami
plt.figure(figsize=(8, 6))
sns.boxplot(x='tsunami', y='magnitude', data=df, palette='Set2')
plt.title('Relação entre Magnitude e Ocorrência de Tsunami')
plt.xlabel('Ocorrência de Tsunami (0 = Não, 1 = Sim)')
plt.ylabel('Magnitude')
plt.show()

# 3.3. Matriz de Correlação
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlação entre Variáveis Numéricas')
plt.show()
