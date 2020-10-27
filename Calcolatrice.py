print("==============================================")
print("Benvenuto nella calcolatrice morente di Marco")
print("==============================================")
print()

continua = True

while continua:
    #Richiesta dei dati
    import math
    op = input("Che operatore vuoi? [+, -, *, /, ^, √, ³√, **/]")
    if op == ("+" or "-" or "*" or "/" or "^" or "**/"):
        y = input("Primo numero: ")
        x = input("Secondo numero: ")
    elif op == ("√" or "³√"):
        x = input("Primo numero: ")
        y = "useful"
    else:
        x = "useful"
        y = "useful"

    #Validazione dei dati
    #if (x.isdigit()) & (y.isdigit()) & (op == "+" or op == "-"):# il punto vuol dire chiamare una funzione su quella variabile. la dicitura "==" è una comparazione
        #print("Perfetto!")

    #else:
        #print("Attenzione, sono stati rilevati 1 o più dati inesatti!")

    # OPPURE
    if (op == "+" or op == "-" or op == "*" or op == "/" or op == "^" or op == "**/") & ((x.isdigit()) & (y.isdigit())):
        print("Perfetto...sto calcolando, un attimo di pazienza!")
    elif (op == "√" or op == "³√") & (x.isdigit()):
        print("Perfetto!")
    else:
# if not (x.isdigit()) & (y.isdigit()) & (op == "+" or op == "-" or op == "*" or op == "/" or op == "**") or (x.isdigit() & (op == "√")):
    # I dati non sono a posto
        retry = input("Attenzione, sono stati rilevati 1 o più dati inesatti! Riprovare? (y/n)")
        if retry == "y":
            retry = continua
        else:
            print("Grazie per aver utilizzato la calcolatrice morente di Marco")

        #Cast
    if (op == "+" or op == "-" or op == "*" or op == "/" or op == "^" or op == "**/") & ((x.isdigit()) & (y.isdigit())):
        x = int(x)
        y = int(y)
    elif (op == "√" or op == "³√") & (x.isdigit()):
        x = int(x)
    else:
        "nothing"
            #I dati sono a posto
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
    else:
        risultato = x**(1/3)
    print("Il risultato è:", risultato, "!")


    #if condizione:
    #    ramo_true
    #else:
    #    ramo_false
    #       =
    #if not condizione:
    #    ramo_false
    #else:
    #    ramo_true


    print("==============================================")

    cont_risp = input("Desideri effettuare un altro calcolo? (y/n)")
    if cont_risp == "y":
        cont_risp = continua
    else:
        print("Grazie per aver utilizzato la calcolatrice morente di Marco")