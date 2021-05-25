A = int(input("Digite o 1º valor: "))
B = int(input("Digite o 2º valor: "))
operacao = input("Digite Soma(soma), Subtração(sub), Multiplicação(mult), Divisão(div) ou Exponenciação(exp):")
if operacao == "soma":
    Soma = A + B
    print("Resultado da subtração :", Soma)
elif operacao == "sub":
    sub = A-B
    print("Subtração :", sub)
elif operacao == "mult":
    mult = A * B
    print("Multiplicação: ", mult)
elif operacao == "div":
    div = A/B
    print("Divisão: ", div)
elif operacao == "exp":
    exp = A ** B
    print("Exponenciação: ", exp) 
print("Operação realizada!!!")  