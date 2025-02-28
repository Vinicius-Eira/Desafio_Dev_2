
import json

# 1) Cálculo da variável SOMA
def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K += 1
        SOMA += K
    print(f"Valor final da variável SOMA: {SOMA}")

#__________________________________________________________

# 2) Fibonacci e verificação
def pertence_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

#__________________________________________________________

# 3) Faturamento diário
def analisar_faturamento(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        dados = json.load(file)
        valores = [dia["valor"] for dia in dados if dia["valor"] > 0]
        menor = min(valores)
        maior = max(valores)
        media = sum(valores) / len(valores)
        dias_acima_media = len([v for v in valores if v > media])
        
        print(f"Menor faturamento: R${menor:.2f}")
        print(f"Maior faturamento: R${maior:.2f}")
        print(f"Dias com faturamento acima da média: {dias_acima_media}")

#__________________________________________________________

# 4) Percentual de faturamento por estado
def percentual_faturamento(estado_valores):
    total = sum(estado_valores.values())
    for estado, valor in estado_valores.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")

#__________________________________________________________

# 5) Inverter string sem reverse
def inverter_string(texto):
    invertida = ""
    for i in range(len(texto)-1, -1, -1):
        invertida += texto[i]
    return invertida

if __name__ == "__main__":
    # Testes
    calcular_soma()
    numero = 21
    print(f"O número {numero} pertence à sequência Fibonacci? {pertence_fibonacci(numero)}")

    # Arquivo JSON de exemplo: faturamento.json
    analisar_faturamento("faturamento.json")

    estados = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    percentual_faturamento(estados)

    texto = "Desafio"  
    print(f"Texto invertido: {inverter_string(texto)}")
