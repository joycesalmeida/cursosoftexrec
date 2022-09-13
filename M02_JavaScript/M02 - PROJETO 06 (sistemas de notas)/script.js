// Função para o formulário da média e aprovação ou reprovação do alun
function mediaAluno(){
    
    function arredondar(n) {
        return (Math.round(n * 100) / 100).toFixed(1);
    }

    var nota1 = parseFloat(document.getElementById("nota1").value);
    var nota2 = parseFloat(document.getElementById("nota2").value);
    var nota3 = parseFloat(document.getElementById("nota3").value);
    var mediaTotal = (nota1 + nota2 + nota3)/3;
    
    if(mediaTotal >=7){
        alert("Parabéns, sua Média é " + arredondar(mediaTotal) + " você está Aprovado")}
        else{
        alert("Estude mais, sua Média é " + arredondar(mediaTotal) + " você está Reprovado")
    }
}

// Função para o formulário da nota mínima necessária para a aprovação do aluno
function mediaNota(){

    var nota4 = parseFloat(document.getElementById("nota4").value);
    var nota5 = parseFloat(document.getElementById("nota5").value);
    var notaParcial = (nota4 + nota5);

    if(notaParcial == 20){
        alert("você precisa tirar no mínimo nota 1")
    }else if (notaParcial == 19){
        alert("Você precisa tirar no mínimo nota 2")
    }else if (notaParcial == 18){
        alert("Você precisa tirar no mínimo nota 3")
    }else if (notaParcial == 17){
        alert("Você precisa tirar no mínimo nota 4")
    }else if (notaParcial == 16){
        alert("Você precisa tirar no mínimo nota 5")
    }else if (notaParcial == 15){
        alert("Você precisa tirar no mínimo nota 6")
    }else if (notaParcial == 14){
        alert("Você precisa tirar no mínimo nota 7")
    }else if (notaParcial == 13){
        alert("Você precisa tirar no mínimo nota 8")
    }else if (notaParcial == 12){
        alert("Você precisa tirar no mínimo nota 9")
    }else if (notaParcial == 11){
        alert("você precisa tirar no mínimo nota 10")
    }else if (notaParcial <= 10){
        alert("Estude mais, infelizmente não há como você atingir a nota minima suficiente para ser Aprovado!")
    }   

}