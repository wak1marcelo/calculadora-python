# Calculadora em Python

## Visão geral

Este documento registra a evolução da calculadora em Python desenvolvida no arquivo `hello.py`, desde a primeira versão até a versão mais organizada e robusta.

O objetivo do programa é:

- Ler dois números digitados pelo usuário
- Ler a operação matemática desejada
- Executar o cálculo
- Mostrar o resultado formatado
- Tratar erros comuns de entrada e execução

---

## Objetivo inicial

A calculadora começou como um script simples de terminal com suporte para:

- soma (`+`)
- subtração (`-`)
- multiplicação (`*`)
- divisão (`/`)

A primeira ideia era apenas fazer o cálculo com `match` e imprimir o resultado no final.

---

## Primeira versão

Estrutura inicial:

- leitura de `number1`
- leitura de `number2`
- leitura de `opcao`
- uso de `match`
- cálculo armazenado em `result`
- impressão final do resultado

Exemplo da lógica inicial:

```python
match opcao:
    case '+':
        result = number1 + number2
    case '-':
        result = number1 - number2
    case '*':
        result = number1 * number2
    case '/':
        if number2 == 0:
            print("Operacao invalida!!")
        else:
            result = number1 / number2

print("Resultado = ", f"{result:.2f}")
```

### Problemas encontrados

1. `result` podia não existir.
   Isso acontecia quando a operação era inválida ou quando ocorria divisão por zero.

2. O programa ainda tentava imprimir `result` no final.
   Isso causava erro de execução (`NameError`).

3. Não existia tratamento para operador inválido.

4. Não havia tratamento para entrada inválida em `float(...)`.

5. Havia erros de digitação nas mensagens exibidas ao usuário.

---

## Primeira correção: impressão dentro dos casos válidos

Uma das primeiras melhorias foi mover a impressão do resultado para dentro de cada `case`.

### Vantagem

- Evitou tentar imprimir `result` quando ele não tivesse sido criado.

### Resultado

A lógica passou a funcionar melhor para operações válidas e para o caso de divisão por zero.

### Limitação

- Havia repetição de `print(...)` em vários pontos do código.

---

## Adição do `case _`

Depois foi adicionado um caso padrão no `match`:

```python
case _:
    print("Operacao Invalida!!")
```

### Melhoria obtida

- O programa passou a tratar operadores não suportados.

### Importância

Esse ajuste tornou o fluxo mais seguro e previsível.

---

## Refatoração para funções

Em seguida, a calculadora foi reorganizada em funções separadas:

```python
def soma(number1, number2):
    ...

def subtracao(number1, number2):
    ...

def multiplicacao(number1, number2):
    ...

def divisao(number1, number2):
    ...
```

### Objetivo dessa mudança

- organizar melhor o código
- separar responsabilidades
- facilitar manutenção
- praticar criação de funções em Python

### Problema observado

Nas primeiras versões com funções, elas ainda faziam `print(...)` diretamente em vez de retornar valores.

---

## Mudança de `print` para `return`

Depois as funções passaram a retornar o resultado:

```python
def soma(number1, number2):
    return number1 + number2
```

### Melhoria obtida

- as funções ficaram reutilizáveis
- a lógica de cálculo ficou separada da lógica de exibição
- o código ficou mais próximo de boas práticas

### Conceito importante aprendido

- `print(...)` mostra algo na tela
- `return ...` devolve o valor para quem chamou a função

---

## Criação de uma função para exibir o resultado

Foi criada uma função `resultado(result)` para centralizar a saída:

```python
def resultado(result):
    print("Resultado = ", f"{result:.2f}")
```

### Problema intermediário

Antes dessa correção, havia uma função `resultado()` que dependia da variável global `result`.

### Ajuste importante

Ela passou a receber `result` como parâmetro, o que melhorou a estrutura e eliminou dependência desnecessária do escopo global.

---

## Tratamento da divisão por zero com `None`

Em uma fase intermediária, a divisão passou a retornar `None` quando o divisor era zero:

```python
def divisao(number1, number2):
    if number2 == 0:
        return None
    return number1 / number2
```

### Objetivo

- evitar quebra do programa
- permitir checagem antes de imprimir

### Problema associado

Se o código tentasse formatar `None` com `:.2f`, ocorria erro.

### Solução

Foi adicionada verificação:

```python
if result is not None:
    print(f"Resultado = {result:.2f}")
```

---

## Inicialização de `result = None`

Outro problema importante surgiu quando a operação era inválida:

- `result` podia não ser criado
- o programa ainda tentava verificar ou imprimir seu valor

### Correção

Foi introduzido:

```python
result = None
```

antes da lógica principal de escolha da operação.

### Benefício

- todos os fluxos do programa passaram a ter uma referência segura para `result`

---

## Tratamento de entrada inválida com `try/except`

Depois disso, foi tratado um novo tipo de erro: quando o usuário digitava algo que não podia ser convertido para `float`.

Versão conceitual:

```python
try:
    number1 = float(input("Digite o primeiro numero: "))
    number2 = float(input("Digite o segundo numero: "))
except ValueError:
    print("Valor Invalido!!")
```

### Problema intermediário

No começo, o `except` apenas imprimia a mensagem, mas o programa continuava.

Isso fazia com que `number1` e `number2` pudessem não existir, gerando novos erros mais adiante.

### Correção aplicada

Toda a lógica dependente dos números foi colocada dentro do `try`, ou o fluxo foi interrompido após erro.

---

## Uso de exceção para divisão por zero

Em vez de retornar `None`, a função `divisao` evoluiu para lançar uma exceção específica:

```python
def divisao(number1, number2):
    if number2 == 0:
        raise ZeroDivisionError("Nao e possivel dividir por zero")
    return number1 / number2
```

### Vantagens

- a função ficou responsável apenas por calcular ou sinalizar erro
- o tratamento ficou fora da função
- a lógica ficou mais clara e mais próxima de um modelo profissional

### Tratamento aplicado

```python
try:
    result = divisao(number1, number2)
except ZeroDivisionError as error:
    print(error)
```

---

## Troca do `match` por dicionário de operações

Na fase final, a seleção da operação foi simplificada com um dicionário:

```python
operacoes = {
    '+': soma,
    '-': subtracao,
    '*': multiplicacao,
    '/': divisao
}
```

Depois:

```python
funcao = operacoes.get(opcao)
```

### Benefícios dessa abordagem

- reduz repetição
- elimina a necessidade de `match`
- deixa o código mais limpo
- facilita adicionar novas operações no futuro

### Tratamento para operação inválida

```python
if funcao is None:
    print("Operacao Invalida!!")
    exit()
```

---

## Erro de regressão durante a refatoração

Durante a troca para o dicionário, ocorreu um erro temporário:

```python
operacoes = {
    '+': soma,
    '-': subtracao,
    '*': divisao,
    '/': multiplicacao
}
```

### Problema

- `*` ficou ligado à função de divisão
- `/` ficou ligado à função de multiplicação

### Impacto

A calculadora passou a executar operações trocadas.

### Correção

O mapeamento foi ajustado para:

```python
operacoes = {
    '+': soma,
    '-': subtracao,
    '*': multiplicacao,
    '/': divisao
}
```

---

## Versão final documentada

A estrutura final ficou conceitualmente assim:

```python
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
```

---

## Principais aprendizados

Durante a evolução da calculadora, os conceitos mais importantes praticados foram:

1. Uso de `match` e escolha de fluxo
2. Criação de funções
3. Diferença entre `print` e `return`
4. Escopo de variáveis
5. Inicialização segura de variáveis
6. Tratamento de erros com `try/except`
7. Tratamento específico de exceções
8. Refatoração para reduzir repetição
9. Uso de dicionários para mapear operações para funções

---

## Melhorias futuras possíveis

A calculadora já está funcional, mas ainda pode evoluir:

- criar uma função `main()`
- trocar `exit()` por uma estrutura mais organizada
- padronizar nomes de variáveis em português
- permitir várias operações em sequência
- adicionar potência, raiz quadrada ou porcentagem
- validar também entradas vazias

---

## Conclusão

A evolução da calculadora mostra uma progressão clara:

- começou como um script simples
- enfrentou problemas de fluxo e variáveis indefinidas
- foi reorganizada em funções
- ganhou tratamento de erro
- passou a usar exceções corretamente
- terminou com uma estrutura mais limpa e mais próxima de boas práticas

Esse processo foi importante não só para construir a calculadora, mas para praticar fundamentos reais de programação em Python.
