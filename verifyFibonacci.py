fib = [0, 1]

n = int(input("Digite um numero para verificar se pertence a sequencia de Fibonacci: "))
  
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
        
if n in fib:
    print(f"{n} pertence a sequencia de Fibonacci")
else:
    print(f"{n} não pertence a sequencia de Fibonacci")
