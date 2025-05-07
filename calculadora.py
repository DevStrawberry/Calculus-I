import math

def ler_valores():
    try:
        tipo = input("Tipo de termo (p para polinomial, e para exponencial): ").strip().lower()
        coef = float(input("Digite o coeficiente: "))
    except ValueError:
        print("Entrada inválida! Assumindo coeficiente 0.")
        coef = 0
    
    if tipo == 'p':
        try:
            exp = float(input("Digite o expoente: "))
            return {"tipo": "polinomial", "coeficiente": coef, "expoente": exp}
        except ValueError:
            print("Expoente inválido! Usando 1.")
            return {"tipo": "polinomial", "coeficiente": coef, "expoente": 1}
    elif tipo == 'e':
        base_input = input("Digite a base da exponencial (pode ser 'e' para base natural): ").strip().lower()
        try:
            base = math.e if base_input == 'e' else float(base_input)
            if base <= 0:
                print("Base inválida! Usando 1.")
                base = 1
            return {"tipo": "exponencial", "coeficiente": coef, "base": base}
        except ValueError:
            print("Base inválida! Usando 1.")
            return {"tipo": "exponencial", "coeficiente": coef, "base": 1}
    else:
        print("Tipo inválido! Assumindo polinomial com expoente 1.")
        return {"tipo": "polinomial", "coeficiente": coef, "expoente": 1}

def imprime_funcao(funcao):
    for i, termo in enumerate(funcao):
        coef = termo["coeficiente"]
        if termo["tipo"] == "polinomial":
            exp = termo["expoente"]
            coef_str = f"{int(coef)}" if coef.is_integer() else f"{coef:.4f}"
            exp_str = f"{int(exp)}" if exp.is_integer() else f"{exp:.4f}"
            print(f"Termo {i + 1}: {coef_str} * x^{exp_str}")
        else:
            base = termo["base"]
            base_str = "e" if abs(base - math.e) < 1e-6 else f"{base:.4f}"
            coef_str = f"{int(coef)}" if coef.is_integer() else f"{coef:.4f}"
            print(f"Termo {i + 1}: {coef_str} * {base_str}^x")

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

def encontrar_pontos_criticos(derivada_funcao, inicio=-10, fim=10, passo=0.001, tolerancia=1e-8):
    pontos_criticos = []
    x = inicio
    y_anterior = avaliar(derivada_funcao, x)
    while x <= fim:
        y = avaliar(derivada_funcao, x)
        if abs(y) < tolerancia or (y * y_anterior < 0): 
            if round(x, 3) not in pontos_criticos:
                pontos_criticos.append(round(x, 3))
        y_anterior = y
        x += passo
    return pontos_criticos

try:
    n = int(input("Digite a quantidade de termos: "))
    if n <= 0:
        print("Número de termos deve ser positivo!")
        n = 1
except ValueError:
    print("Entrada inválida! Usando 1 termo.")
    n = 1

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

print("\nClassificação dos pontos críticos:")
for x in pontos:
    segunda = avaliar(segunda_derivada, x)
    if segunda > 0:
        print(f"x = {x}: Mínimo local")
    elif segunda < 0:
        print(f"x = {x}: Máximo local")
    else:
        print(f"x = {x}: Ponto de inflexão ou indeciso")
