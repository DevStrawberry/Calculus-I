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
            ponto = round(x, 3)
            if not any(abs(p - ponto) < passo * 2 for p in pontos_criticos):
                pontos_criticos.append(ponto)
        y_anterior = y
        x += passo

    return pontos_criticos