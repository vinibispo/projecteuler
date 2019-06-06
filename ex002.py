anterior = 0
atual = 1
proximo = 1
soma = 0
while soma < 4000000:
    anterior = atual
    atual = proximo
    proximo = anterior + atual
    soma += atual
print(soma)