const prompt = require("prompt-sync")();

let qtdFuncao = prompt("Digite a quantidade de funções a serem avaliadas: ");

function nova_funcao() {

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
    console.log("Termos:", termos);
    return termos;
}

let funcoes = [];
for (let i = 0; i < qtdFuncao; i++) {
    funcoes.push(nova_funcao());          
}