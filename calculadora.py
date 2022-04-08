def soma(v1, v2):
    try:
        return v1+v2
    except:
        return "Digitos não somaveis"

def subtracao(v1, v2):
    try: 
        return v1-v2
    except:
        return "digitos não subtraiveis"
    

def divisao(v1, v2): 
    try: 
        div = v1/v2
    except:
        return "digitos não divisiveis"
    return div

def multiplicacao(v1, v2):
    try:
        return v1*v2
    except: 
        return "digitos não multiplicaveis"