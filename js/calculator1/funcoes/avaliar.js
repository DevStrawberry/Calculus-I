function avaliar(funcao, x) {
    let resultado = 0;
    funcao.forEach(termo => {
        if (termo.tipo === "polinomial") {
            resultado += termo.coef * (x ** termo.exp);
        } else {
            resultado += termo.coef * (termo.base ** x); 
        }
    });
    return resultado;
}

module.exports = avaliar;