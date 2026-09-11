import pandas as pd
from sklearn.tree import DecisionTreeClassifier


try:
    dados = pd.read_csv("base_treino_desempenho_alunos.csv")
except FileNotFoundError:
    print("Erro: Arquivo CSV não encontrado na pasta.")
    exit()
    
treino = dados[['horas_estudo_semana', 'taxa_frequencia_pct']]
rotulos = dados[["resultado_final"]]
modelo = DecisionTreeClassifier()
modelo.fit(treino, rotulos)

print("---- Previsão de Desempenho ----")
try:
    horas = float(input("Digite as horas de estudo por semana: "))
    if horas < 0:
        raise ValueError("As horas não podem ser negativas")
except ValueError:
    print("Erro: Por favor, insira um número válido de horas de estudo.")
    exit()
    
try:
    frequencia = int(input("Digite a taxa de frequencia (0 a 100): "))
    if frequencia < 0 or frequencia > 100:
        raise ValueError("A frequencia deve ser entre 0 e 100")
except ValueError:
    print("Erro: Por favor, insira um número inteiro válido oara a frequênci.")
    exit()
    
dados_usuario = pd.DataFrame([[horas, frequencia]], columns=["horas_estudo_semana", "taxa_frequencia_pct"])    
previsao = modelo.predict(dados_usuario)
print(f"\nPredição: Com {horas} horas de estudo e {frequencia}% de frequência, o aluno está provalvemente: {previsao[0].upper()}.")
