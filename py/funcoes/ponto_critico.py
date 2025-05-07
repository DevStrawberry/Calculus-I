def avaliar(funcao, x):
    resultado = 0
    for termo in funcao:
        if termo["tipo"] == "polinomial":
            resultado += termo["coeficiente"] * (x ** termo["expoente"])
        elif termo["tipo"] == "exponencial":
            resultado += termo["coeficiente"] * (termo["base"] ** x)
    return resultado

def encontrar_ponto_critico_bissecao(primeira_derivada, inicio, fim, tolerancia=1e-8, max_iteracoes=100):
    a = inicio
    b = fim
    fa = avaliar(primeira_derivada, a)
    fb = avaliar(primeira_derivada, b)

    if (fa * fb > 0):
        return None

    iteracao = 0
    while (b - a) > tolerancia and iteracao < max_iteracoes:
        c = (a+b) / 2
        fc = avaliar(primeira_derivada, c)

        if abs(fc) < tolerancia:
            return round(c, 6)
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        iteracao += 1
    
    return round((a+b) / 2, 6)

def encontrar_pontos_criticos(primeira_derivada, inicio=-10, fim=10, granularidade=0.1, tolerancia = 1e-8):
    pontos_criticos = []

    i = inicio
    while i < fim:
        subInicio = i
        subFim = min(i+granularidade, fim)

        valorInicio = avaliar(primeira_derivada, subInicio)
        valorFim = avaliar(primeira_derivada, subFim)

        if valorInicio*valorFim <= 0 or abs(valorInicio) < tolerancia or abs(valorFim) < tolerancia:
            ponto = encontrar_ponto_critico_bissecao(primeira_derivada, subInicio, subFim, tolerancia)

            if ponto is not None:
                if not any(abs(p - ponto) < tolerancia * 10 for p in pontos_criticos):
                    pontos_criticos.append(ponto)
        
        i += granularidade
    
    return sorted(pontos_criticos)