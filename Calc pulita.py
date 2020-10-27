print("==============================================")
print("Benvenuto nella calcolatrice morente di Marco")
print("==============================================")
print()

continua = True
riprova = True

while continua or riprova:

    import math
    op = input("Che operatore desideri utilizzare? [+, -, *, /, ^, √, ³√, **/]")
    if (op == "+" or op == "-" or op == "*" or op == "/" or op == "^" or op == "**/"):
        x = input("Primo numero: ")
        y = input("Secondo numero: ")
    elif (op == "√" or op == "³√"):
        x = input("Primo numero: ")
        y = "useful"
    else:
        x = "useful"
        y = "useful"

    if (op == "+" or op == "-" or op == "*" or op == "/" or op == "^" or op == "**/") & ((x.isdigit()) & (y.isdigit())):
        print("Perfetto...sto calcolando, un attimo di pazienza!")
    elif (op == "√" or op == "³√") & (x.isdigit()):
        print("Perfetto!")
    else:
        retry = input("Attenzione, sono stati rilevati 1 o più dati inesatti! Riprovare? (y/n)")
        if retry == "y":
            retry = riprova
        else:
            print("Grazie per aver utilizzato la calcolatrice morente di Marco")

    if (op == "+" or op == "-" or op == "*" or op == "/" or op == "^" or op == "**/") & ((x.isdigit()) & (y.isdigit())):
        x = int(x)
        y = int(y)
    elif (op == "√" or op == "³√") & (x.isdigit()):
        x = int(x)
    else:
        "nothing"

    if op == "+":
        risultato = x+y
    elif op == "-":
        risultato = x-y
    elif op == "*":
        risultato = x*y
    elif op == "/":
        risultato = x/y
    elif op == "^":
        risultato = x**y
    elif op == "√":
        risultato = math.sqrt(x)
    elif op == "**/":
        risultato = x**(1/y)
    elif op == "³√":
        risultato = x**(1/3)

    if (op == "+" or op == "-" or op == "*" or op == "/" or op == "^" or op == "**/" or op == "√" or op == "³√"):
        print("Il risultato è:", risultato, "!")

    print("==============================================")
    if (op == "+" or op == "-" or op == "*" or op == "/" or op == "^" or op == "**/" or op == "√" or op == "³√"):
        cont_risp = input("Desideri effettuare un altro calcolo? (y/n)")
        if cont_risp == "y":
            cont_risp = continua
        else:
            print("Grazie per aver utilizzato la calcolatrice morente di Marco")
            exit()
            input()