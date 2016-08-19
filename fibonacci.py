# Matheus Andrade Rodrigues - 115210160

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2)+fib(n-1)

while True:
    try:
        N = int(raw_input("Digite um número natural positivo: "))
        if N > 0:
            print "O valor correspondente de", N, "na Sequência de Fibonacci é", fib(N)
            break
        else:
            print "Apenas números positivos\n"
    except ValueError:
        print "Insira um inteiro\n"

# Este seria o código ideal, com todos os if/else no seu devido lugar, tabulações ok e prints verdadeiros!
