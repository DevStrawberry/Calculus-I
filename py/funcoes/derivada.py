import math

def derivada(funcao):
    derivada_funcao = []
    for termo in funcao:
        if termo["tipo"] == "polinomial":
            if termo["expoente"] == 0:
                derivada_funcao.append({
                    "tipo": "polinomial",
                    "coeficiente": 0,
                    "expoente": 0
                })
            else:
                derivada_funcao.append({
                    "tipo": "polinomial",
                    "coeficiente": termo["coeficiente"] * termo["expoente"],
                    "expoente": termo["expoente"] - 1
                })
        elif termo["tipo"] == "exponencial":
            derivada_funcao.append({
                "tipo": "exponencial",
                "coeficiente": termo["coeficiente"] * math.log(termo["base"]),
                "base": termo["base"]
            })
    return derivada_funcao