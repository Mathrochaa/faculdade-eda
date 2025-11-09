Aqui está um exemplo de **README** explicando o código de análise exploratória de dados (EDA) para o dataset de **terremotos e tsunamis**.

---

# Análise Exploratória de Dados (EDA) - Terremotos e Tsunamis

Este projeto realiza uma análise exploratória de dados (EDA) utilizando o **dataset de terremotos e tsunamis**. O código é escrito em Python, utilizando as bibliotecas `pandas`, `matplotlib` e `seaborn`.

## Objetivo

O objetivo deste código é analisar as características principais dos dados relacionados aos terremotos, como magnitude, profundidade, e a ocorrência de tsunamis. O código inclui:

* Carregamento do dataset
* Exibição de informações gerais
* Estatísticas descritivas das variáveis numéricas
* Visualizações importantes para entender os dados

## Requisitos

Certifique-se de que as seguintes bibliotecas estejam instaladas no seu ambiente Python:

```bash
pip install pandas matplotlib seaborn
```

## Passo a Passo do Código

### 1. **Carregar o Dataset**

Primeiro, o dataset é carregado usando a biblioteca **`pandas`**. O arquivo CSV contém informações sobre terremotos e tsunamis, incluindo variáveis como **magnitude**, **profundidade**, **latitude**, **longitude**, e **ano**. O caminho do arquivo CSV é especificado e o dataset é carregado no DataFrame `df`.

```python
file_path = 'C:\\Users\\Pichau\\Documents\\earthquake_data_tsunami.csv'
df = pd.read_csv(file_path)
```

### 2. **Informações Gerais sobre o Dataset**

O método `df.info()` fornece informações sobre as colunas do dataset, tipos de dados e quantidade de entradas não nulas. Isso ajuda a entender rapidamente a estrutura dos dados.

```python
df_info = df.info()
```

### 3. **Verificar Dados Ausentes**

O código verifica se existem valores ausentes no dataset utilizando o método `df.isnull().sum()`. Isso ajuda a garantir que não haja dados faltantes antes de realizar outras análises.

```python
missing_data = df.isnull().sum()
```

### 4. **Estatísticas Descritivas**

Usamos o método `df.describe()` para gerar estatísticas descritivas das variáveis numéricas, como **média**, **mínimo**, **máximo**, e **desvio padrão**. Isso permite entender melhor a distribuição dos dados.

```python
stats = df.describe()
```

### 5. **Visualizações**

As visualizações ajudam a entender melhor os dados. O código gera três tipos de gráficos:

#### 5.1 **Distribuição das Magnitudes**

Um **histograma** com uma linha de densidade (KDE) é gerado para visualizar a distribuição das magnitudes dos terremotos.

```python
sns.histplot(df['magnitude'], bins=30, kde=True, color='blue')
```

#### 5.2 **Relação entre Magnitude e Ocorrência de Tsunami**

Um **boxplot** é criado para mostrar a relação entre a magnitude dos terremotos e se um tsunami ocorreu (0 = Não, 1 = Sim).

```python
sns.boxplot(x='tsunami', y='magnitude', data=df, palette='Set2')
```

#### 5.3 **Matriz de Correlação**

Uma **matriz de correlação** é gerada para visualizar como as variáveis numéricas estão correlacionadas entre si. Isso ajuda a identificar relações importantes entre as variáveis.

```python
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
```

### 6. **Exibir Gráficos**

Após cada visualização, `plt.show()` é chamado para exibir o gráfico na tela.

---

## Como Rodar o Código

1. **Instalar as dependências**:

   * Instale as bibliotecas necessárias com o comando `pip install pandas matplotlib seaborn`.

2. **Alterar o caminho do arquivo**:

   * Certifique-se de que o caminho para o arquivo CSV (`file_path`) esteja correto, apontando para onde você armazenou o arquivo `earthquake_data_tsunami.csv`.

3. **Executar o código**:

   * Execute o código em seu ambiente Python local. Ele irá carregar o dataset, realizar as análises e gerar as visualizações.

---

## Exemplos de Saída

1. **Informações gerais sobre o dataset**:

   * A saída do `df.info()` mostra o número de entradas, tipos de dados e colunas no dataset.

2. **Estatísticas descritivas**:

   * As estatísticas geradas pelo `df.describe()` mostram a distribuição numérica das variáveis como **magnitude**, **profundidade**, e outras variáveis numéricas.

3. **Gráficos**:

   * O **histograma** mostra a distribuição das magnitudes dos terremotos.
   * O **boxplot** mostra a relação entre a magnitude e a ocorrência de tsunamis.
   * A **matriz de correlação** exibe as relações entre variáveis numéricas, ajudando a identificar possíveis padrões ou redundâncias.

---

## Conclusão

Este código realiza uma análise exploratória de dados do dataset de terremotos e tsunamis, proporcionando uma visão geral das principais características dos dados, além de gerar visualizações que ajudam a entender melhor as distribuições e correlações. É uma etapa inicial importante para qualquer análise de dados, antes de realizar modelagem ou outras análises mais avançadas.

---

Com isso, o **README** está completo! Agora, você pode usar este arquivo para documentar seu código e compartilhar com outros. Se precisar de mais ajustes ou explicações, é só avisar! 😊
