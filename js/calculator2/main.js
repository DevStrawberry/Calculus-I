const prompt = require("prompt-sync")();
const derivadaString = require("./funcoes/derivada.js");

let qtdFuncao = parseInt(prompt("Digite a quantidade de funções a serem avaliadas: "));

function nova_funcao() {

    console.log("Função de exemplo: f(x) = 5x^2 - (2x - e^x)");
    let funcao = prompt("Entre com a função: f(x) = ");
    funcao = funcao.replace(/\s+/g, ''); // Remove todos os espaços da função

    let termos = [];
    let inicio = 0;
    let dentro_parenteses = 0;

    for (let i = 1; i < funcao.length; i++) {
        switch(funcao[i]) {
            case '(':
                dentro_parenteses++;
                break;
            case ')':
                dentro_parenteses--;
                break;
            case '+':
            case '-':
                if (dentro_parenteses === 0) {
                    termos.push(funcao.slice(inicio, i));
                    inicio = i;
                }
                break;
        }
    }
                    
    termos.push(funcao.slice(inicio));
    return termos;
}

let funcoes = [];
for (let i = 0; i < qtdFuncao; i++) {
    const termos = nova_funcao();
    funcoes.push(termos);          

    console.log(`Termos da ${i + 1}º função:`, termos);

    const derivada = derivadaString(termos);
    console.log(`f'(x) = ${derivada.join(' + ').replace(/\+\s-\s/g, '- ')}`);
}