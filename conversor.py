print("======================\n  CONVERSOR DE BASE\n======================")
escolha = 1
while(escolha > 0):
    escolha = int(input("\n1 - DECIMAL PARA BINARIO\n2 - BINARIO PARA DECIMAL\n3 - DECIMAL PARA HEXADECIMAL\n0 - ENCERRAR\nDIGITE O VALOR DA OPERAÇÃO: "))
    if(escolha >= 0 and escolha <=3):
        if(escolha == 1):
            numb = int(input("Digite o valor em decimal para converter para binario: "))
            var = numb
            binario = ""
            if(numb != 0):
                while(numb>0):
                    resto = numb % 2
                    binario = str(resto)+binario
                    numb //= 2
                print("O valor {}  em binario é {}".format(var, binario))
            else:
                print("O valor 0  em binario é 0")
                
        elif(escolha == 2):
            numb = int(input("Digite o valor em binario para transforma em decimal: "))
            var = numb
            larg = len(str(numb))
            dec = 0
            i = 0
            while(larg>=0):
                
                resto = numb % 10
                dec = dec + (resto*(2**i))
                larg = larg - 1
                i = i + 1
                numb //=10
            print("o valor {} em decimal é {}".format(var, dec))
                
        elif(escolha == 3):
            numb = int(input("Digite o valor em decimal para transforma em hexadecimal: "))
            var = numb
            hexa = ""
            if(numb != 0):
                while(numb>0):
                    resto = numb % 16
                    numb //= 16
                    if(resto < 10):
                        hexa = str(resto) + hexa
                    elif(resto == 10):
                        hexa = "A" +hexa
                    elif(resto == 11):
                        hexa = "B" +hexa
                    elif(resto == 12):
                        hexa = "C" +hexa
                    elif(resto == 13):
                        hexa = "D" +hexa
                    elif(resto == 14):
                        hexa = "E" +hexa
                    elif(resto == 15):
                        hexa = "F" +hexa
                        
                print("O valor {} em Hexadecimal é {}".format(var, hexa))
            else:
                print("O valor 0 em hexadecimal é 0")
    else:
        print("valor invalido")
