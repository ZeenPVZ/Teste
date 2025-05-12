from fca_lexer import ArithLexer

exemplos = [
    "Id,Local,Coordenadas",
    "E1,Terras de Bouro/Barral (CIM),[-8.31808611,41.70225278]",
    "E2,Graciosa/Serra das Fontes (DROTRH),[-28.0038,39.0672]",
    "E3,Olhão, EPPO, [-7.821,37.033]",
    "E4, Setúbal, Areias, [-8.89066111,38.54846667]"
]

for frases in exemplos:
    print(f"----------------------")
    print(f"Frase: '{frases}")
    al = ArithLexer()
    al.build()
    al.input(frases)
    print('Tokens: ',end="")
    while True:
        tk = al.token()
        if not tk:
            break
        print(tk,end="")
    print()