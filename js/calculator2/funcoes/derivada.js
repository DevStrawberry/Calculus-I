function derivadaString(termosStr) {
    function derivarTermo(termo, sinal = 1) {
        // Detectar termo polinomial: ex: 3x^2
        if (/^\d*\.?\d*x\^\d+$/.test(termo)) {
            const match = termo.match(/^(\d*\.?\d*)x\^(\d+)$/);
            const coef = sinal * parseFloat(match[1] || '1');
            const exp = parseInt(match[2]);

            if (exp === 0) return '0';

            const novoCoef = coef * exp;
            const novoExp = exp - 1;

            return novoExp === 0 ? `${novoCoef}` :
                   novoExp === 1 ? `${novoCoef}x` :
                   `${novoCoef}x^${novoExp}`;

        // Detectar termo linear: ex: 2x
        } else if (/^\d*\.?\d*x$/.test(termo)) {
            const coef = sinal * parseFloat(termo.replace('x', '') || '1');
            return `${coef}`;
        
        // Detectar termo exponencial: ex: 2e^(x)
        } else if (/^\d*\.?\d*e\^\(.*\)$/.test(termo)) {
            const match = termo.match(/^(\d*\.?\d*)e\^\((.*)\)$/);
            const coef = sinal * parseFloat(match[1] || '1');
            const argumento = match[2];
            const base = Math.E;
            const novoCoef = coef * Math.log(base);
            return `${novoCoef.toFixed(2)}e^(${argumento})`;
        }

        return `Não reconhecido: ${termo}`;
    }

    return termosStr.flatMap((termo) => {
        // Extrair o sinal externo
        let sinal = 1;
        if (termo.startsWith('+')) {
            termo = termo.slice(1);
        } else if (termo.startsWith('-')) {
            sinal = -1;
            termo = termo.slice(1);
        }

        // Caso composto entre parênteses: ex: -(2x - e^(x))
        if (/^\(.*\)$/.test(termo)) {
            termo = termo.slice(1, -1); // remove parênteses
        }

        // Se ainda tiver parênteses dentro (ex: -(2x-e^(x))), dividir os subtermos
        if (termo.includes('+') || termo.includes('-')) {
            // quebra em subtermos, mantendo os sinais
            const subTermos = [];
            let buffer = '';
            for (let i = 0; i < termo.length; i++) {
                if ((termo[i] === '+' || termo[i] === '-') && i > 0) {
                    subTermos.push(buffer);
                    buffer = termo[i];
                } else {
                    buffer += termo[i];
                }
            }
            if (buffer) subTermos.push(buffer);

            // Recursivamente derivar os subtermos
            return subTermos.map(sub => derivarTermo(sub.trim(), sinal));
        }

        return [derivarTermo(termo, sinal)];
    });
}

module.exports = derivadaString;