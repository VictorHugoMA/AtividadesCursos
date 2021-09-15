function Chutar(){
    var numeroSecreto = parseInt(Math.random()*11);
    var resultado = document.getElementById("resultado")
    var chute = parseInt(document.getElementById("valor").value)
     console.log(chute)
  
    if (chute == numeroSecreto) {
        resultado.innerHTML = "Acertou !!"
    }
    else if(chute > 10 || chute < 0){
        resultado.innerHTML = "Coloque um numero de 0 a 10"
        
    }
    else{
        resultado.innerHTML = "Errou, o numero secreto era " + numeroSecreto
    }

}