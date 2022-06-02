def es_palindromo(numero):
    k = 0
    n = numero.copy()
    while n // 10 > 0:
        n //= 10
        k += 1

    print(k)

    pal = True
    i = 0
    while i < k/2:
    # p = (numero // (10 ** (k-i-1))) % 10
    # u = (numero % 10**(i+1)) // 10**i
        p = (numero // (10 ** (k-1-i))) % 10
        u = (numero % 10**(i + 1)) // 10**i
        # print(p, u)

   
    if p != u:
        pal = False
        break
    i+=1

    return pal

print(es_palindromo(123454321))

# lista = [151, 60, -5, 135, 18, 40]
# positivos = all(map(lambda x: x>= 0, lista))
# palindromos = any(map(es_palindromo, lista))
# print(positivos and palindromos)