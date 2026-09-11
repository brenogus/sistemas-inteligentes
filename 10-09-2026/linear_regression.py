
from sklearn.linear_model import LinearRegression

treino= [[50,2], [80,3], [120,4], [150,5], [200,6]]
precos = [200,300,450,600,800]
modelo = LinearRegression()
modelo.fit(treino,precos)


print("---- Previsão de Desempenho ----")
try:
    tamanho = float(input("Digite o tamanho da casa em m2: "))
    if tamanho <= 0:
        raise ValueError("Tamanho inválido")
except ValueError:
    print("Erro: Por favor, insira um número válido de área.")
    exit()
    
try:
    quartos = int(input("Digite o número de quartos: "))
    if quartos <= 0:
        raise ValueError("Número de quartos inválido.")
except ValueError:
    print("Erro: Por favor, insira um número inteiro positivo para o número de quartos.")
    exit()
    
previsao = modelo.predict([[tamanho, quartos]])
print(f"\nPreço estimado da casa: R$ {previsao[0]:,.2f} mil")
