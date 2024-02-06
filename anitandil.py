def rec_imprimir_num(n:int):
    if n==0:
        print(n)
    else:
        print(n)
        rec_imprimir_num(n-1)

rec_imprimir_num(100)

#extra
def factorial(n:int)->int:
    if n==0:
        return n
    else:
        return n + factorial(n-1)

print(factorial(5))

def fibonacci(n,a=0,b=1):
    while n!=0:
        return fibonacci(n-1,b,a+b)
    return a

print(fibonacci(5))
