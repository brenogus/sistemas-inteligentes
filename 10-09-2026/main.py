from sklearn.tree import DecisionTreeClassifier

treino = [
    [4,5,0], [4,4,0], [4,2,0],
    [4,2,1], [4,5,1], [4,6,2],
    [4,7,1], [4,12,1], [4,15,1], [4,20,1],
    [2,2,0], [2,1,0],
    [2,1,2],
    [6,40,1], [6,50,1], [8,80,1], [4,25,1],
    [6,2,1], [10,2,1], [14,2,1], [18,2,1], [18, 3, 1],
    [1,1,2], [3,1,2], [3,2,2]
] 

rotulos = [
    "carro", "carro", "carro",
    "caminhonete", "caminhonete", "caminhonete",
    "van", "van", "van","van",
    "moto", "moto",
    "bicicleta",
    "onibus", "onibus", "onibus", "onibus",
    "caminhao", "caminhao", "caminhao", "caminhao", "caminhao",
    "monociclo",
    "triciclo",
    "tuk-tuk"
]

modelo = DecisionTreeClassifier()
modelo.fit(treino, rotulos)

try:
    rodas = int(input("Digite o número de rodas do veículo: "))
    if rodas <= 0:
        raise ValueError("Número de rodas inválido")
except ValueError:
    print("Erro: Por favor, insira um número inteiro positivo para o número de rodas.")
    exit()
    
try:
    capacidade = int(input("Digite a capacidade de passageiros do veículo: "))
    if capacidade <= 0:
        raise ValueError("Capacidade inválida")
except ValueError:
    print("Erro: Por favor, insira um número inteiro positivo para a capacidade.")
    exit()
    
try:
    combustivel = int(input("Digite o tipo de combustivel (0- gasolina / etanol, 1- diesel, 2- outro): "))
    if capacidade < 0:
        raise ValueError("Combustivel inválido")
except ValueError:
    print("Erro: Por favor, insira um número inteiro positivo para o tipo de combustivel.")
    exit()

previsao = modelo.predict([[rodas, capacidade, combustivel]])
print(f"Predição: Este veículo provavelmente é um {previsao[0]}.")