from math import log

def soma(v1, v2):
    try:
        return v1+v2
    except:
        return "Digitos não somaveis. "

def subtracao(v1, v2):
    try: 
        return v1-v2
    except:
        return "digitos não subtraiveis. "
    

def divisao(v1, v2): 
    try: 
        div = v1/v2
    except:
        return "digitos não divisiveis. "
    return div

def multiplicacao(v1, v2):
    try:
        return v1*v2
    except: 
        return "digitos não multiplicaveis. "

def potenciaciacao(v1,v2):
    try:
        return v1**v2
    except:
        return "digitos inválidos para potenciação"

def raiz(v1, v2):
    try: 
        return v1**1/v2
    except:
        return "digitos inválidos para raiz. "
def logaritimo(v1,v2):
    try:
        return log(v1, v2)
    except:
        return "digitos invalidos para o logaritimo"

