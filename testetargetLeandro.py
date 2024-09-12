 # Leandro Ciysz de Oliveira
 # TESTE TARGET PARA O ESTÁGIO: 
 # QUESTÃO 1
 # Declaração de Variáveis: - `int INDICE = 13, SOMA = 0, K = 0;` 
 # Aqui estamos declarando três variáveis: INDICE é inicializado com 13. Essa variável serve como um limite do laço. 
 # SOMA é inicializada com 0, ela irá acumular a soma dos números.  `K` também começa com 0. 
 # Essa variável será utilizada como contador dentro do laço.
 # O laço continuará executando enquanto o valor de `K` for menor que o valor de `INDICE` (que é 13). 
 # o valor da variável `SOMA` será 91. Isso representa a soma dos números de 1 a 13 
 # e pode ser confirmada pela fórmula da soma de uma progressão aritmética.
 
#QUESTÃO 2 em PYTHON
def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def is_in_fibonacci(n):
    fib_sequence = fibonacci_sequence(n)
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Solicitar um número ao usuário
numero = int(input("Informe um número: "))
print(is_in_fibonacci(numero))

#QUESTÃO 3 em PYTHON
import json

def calcular_faturamento(dados):
    faturamentos = [dado['valor'] for dado in dados if dado['valor'] > 0]
    
    if not faturamentos:
        return None, None, 0
    
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_faturamento = sum(faturamentos) / len(faturamentos)
    
    dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_faturamento)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

if __name__ == "__main__":
    with open('dados.json', 'r') as arquivo_json:
        dados = json.load(arquivo_json)
        
    menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(dados)
    
    print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
    print(f"Dias com valor de faturamento acima da média: {dias_acima_da_media}")


# QUESTÃO 4
def calcular_percentual(faturamento, total):
    return (faturamento / total) * 100

def main():
    faturamento_estados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    total_mensal = sum(faturamento_estados.values())

    for estado, faturamento in faturamento_estados.items():
        percentual = calcular_percentual(faturamento, total_mensal)
        print(f'{estado}: {percentual:.2f}%')

if __name__ == "__main__":
    main()
    
#QUESTÃO 5
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Entrada 
input_string = input("Digite a string a ser invertida: ")

# Inverte a string
reversed_string = reverse_string(input_string)

# resultado
print("String invertida:", reversed_string)