const prompt = require("prompt-sync")();

let n = Number(prompt("Digite a quantidade de termos: "));

function lerValores() {
    let coeficiente = Number(prompt("Digite o coeficiente: "));
    let expoente = Number(prompt("Digite o expoente: "));
    return [coeficiente, expoente];
}

let funcao = [];
for (let i = 0; i < n; i++) {
    funcao.push(lerValores());
}

console.log("\nFunção original:");
for (let i = 0; i < n; i++) {
    console.log(`Termo ${i + 1}: coef = ${funcao[i][0]}, exp = ${funcao[i][1]}`); 
}

// Derivada de potencia
function derivada(funcao) {
    for (let i = 0; i < n; i++) {
        if (funcao[i][1] != 0) {
            let exp = funcao[i][1];
            funcao[i][1] = funcao[i][1] - 1;
            funcao[i][0] = exp * funcao[i][0];
        } else {
            funcao[i][0] = 0;
            funcao[i][1] = 0;
        }
    }
}

derivada(funcao); // Primeira derivada

console.log("\nPrimeira derivada da função:");
for (let i = 0; i < n; i++) {
    console.log(`Termo ${i + 1}: coef = ${funcao[i][0]}, exp = ${funcao[i][1]}`); 
}

derivada(funcao); // Segunda derivada

let ptoCritico = null;
if (n === 1) { // Se a função tiver apenas um termo 
    let exp = funcao[0][1];
    if (exp === 0) {
        ptoCritico = "Todos os valores de x (função constante)";
    } else if (exp > 0) {
        ptoCritico = 0;
    } else if (exp < 0) {
        ptoCritico = "Nenhum (derivada nunca zera)";
    }
}
console.log(`\nPonto crítico: ${ptoCritico}`);

console.log("\nSegunda derivada da função:");
for (let i = 0; i < n; i++) {
    console.log(`Termo ${i + 1}: coef = ${funcao[i][0]}, exp = ${funcao[i][1]}`); 
}
