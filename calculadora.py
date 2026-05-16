
def soma(number1, number2):
    return number1 + number2

def multiplicacao(number1, number2):
    return number1 * number2

def subtracao(number1, number2):
    return number1 - number2

def divisao(number1, number2):
    if number2 == 0:
        raise ZeroDivisionError("Nao e possivel dividir por zero")
    return number1 / number2

operacoes = {
    '+': soma,
    '-': subtracao,
    '*': multiplicacao,
    '/': divisao
}

try:
    number1 = float(input("Digite o primeiro numero: "))
    number2 = float(input("Digite o segundo numero: "))

except ValueError:
    print("Valor Invalido!!")
    exit()


opcao = input("Digite a operacao: ")

funcao = operacoes.get(opcao)

if funcao is None:
    print("Operacao Invalida!!")
    exit()

try:
    result = funcao(number1, number2)
    print(f"Resultado = {result:.2f}")
except ZeroDivisionError as error:
    print(error)
