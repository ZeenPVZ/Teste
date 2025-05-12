from fca_grammar import ArithGrammar
from pprint import PrettyPrinter

pp = PrettyPrinter(sort_dicts=False)

ag = ArithGrammar()
ag.build()

exemplos = [
    "Id,Local,Coordenadas",
    "E1,Terras de Bouro/Barral (CIM),[-8.31808611,41.70225278]",
    "E2,Graciosa/Serra das Fontes (DROTRH),[-28.0038,39.0672]",
    "E3,Olhão, EPPO, [-7.821,37.033]",
    "E4, Setúbal, Areias, [-8.89066111,38.54846667]"
]

for frases in exemplos:
    print(f"----------------------")
    print(f"--- Frase: '{frases}'")
    res = ag.parse(frases)
    print("Resultado: ")
    pp.pprint(res)