def inputInt(msg):
    num = 0
    erro = True
    while erro == True:
        try:
            num = int(input(msg))
            erro = False
        except ValueError:
            print('Valor inválido. Informe novamente.')
            erro = True
    return num
