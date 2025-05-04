import math

def ler_valores():
    tipo = input("Tipo de termo (p para polinomial, e para exponencial): ")
    coef = float(input("Digite o coeficiente: "))
    if tipo == 'p':
        exp = float(input("Digite o expoente: "))
        return {
            "tipo": "polinomial", 
            "coeficiente": coef, 
            "expoente": exp
        }
    elif tipo == 'e':
        base = float(input("Digite a base da exponencial: "))
        return { 
            "tipo": "exponencial", 
            "coeficiente": coef, 
            "base": base
        }
    else:
        print("Tipo inválido! Assumindo polinomial com expoente 1.")
        return {
            "tipo": "polinomial", 
            "coeficiente": coef, 
            "expoente": 1
        }

def imprime_funcao(funcao):
    for i, termo in enumerate(funcao):
        if termo["tipo"] == "polinomial":
            print(f"Termo {i + 1}: {termo['coeficiente']} * x^{termo['expoente']}")
        else:
            print(f"Termo {i + 1}: {termo['coeficiente']:.4f} * {termo['base']}^x")


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

def avaliar(funcao, x):
    resultado = 0
    for termo in funcao:
        if termo["tipo"] == "polinomial":
            resultado += termo["coeficiente"] * (x ** termo["expoente"])
        elif termo["tipo"] == "exponencial":
            resultado += termo["coeficiente"] * (termo["base"] ** x)
    return resultado

def encontrar_pontos_criticos(derivada_funcao, inicio=-10, fim=10, passo=0.1, tolerancia=1e-3):
    pontos_criticos = []
    x = inicio
    while x <= fim:
        y = avaliar(derivada_funcao, x)
        if abs(y) < tolerancia:
            pontos_criticos.append(round(x, 3))
        x += passo
    return pontos_criticos


n = int(input("Digite a quantidade de termos: "))

funcao = []
for i in range(n):
    funcao.append(ler_valores())
print("\nFunção original:")
imprime_funcao(funcao)

primeira_derivada = derivada(funcao)
print("\nPrimeira derivada da função:")
imprime_funcao(primeira_derivada)

pontos = encontrar_pontos_criticos(primeira_derivada)
print("\nPontos críticos encontrados (f'(x) ≈ 0):")
print(pontos if pontos else "Nenhum ponto crítico encontrado.")

segunda_derivada = derivada(primeira_derivada)
print("\nSegunda derivada da função:")
imprime_funcao(segunda_derivada)