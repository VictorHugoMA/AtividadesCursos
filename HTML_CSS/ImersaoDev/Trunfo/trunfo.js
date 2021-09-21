var carta1 = {  nome: "Reyna",
                atributos:{ataque: 9, defesa: 6, magia: 8}
                }

var carta2 = {  nome:"Jet",
                atributos:{ataque:9, defesa: 5, magia: 5}
                }

var carta3 = {  nome: "KillJoy",
                atributos:{ataque:6, defesa: 9, magia: 2}
                }

var cartas = [carta1, carta2, carta3]

var cartaIA
var cartaPlayer

function sortearCarta(){
    var indCartaIA = parseInt(Math.random()*cartas.length)
    cartaIA = cartas[indCartaIA]
    
    var indCartaPlayer = parseInt(Math.random()*cartas.length)

    while (indCartaIA==indCartaPlayer) {
        indCartaPlayer = parseInt(Math.random()*cartas.length)
    }  
    cartaPlayer = cartas[indCartaPlayer]
    
    console.log(cartaPlayer)

    document.getElementById("btnSortear").disabled = true;
    document.getElementById("btnJogar").disabled = false;
    exibirOpcoes()
}

function exibirOpcoes(){
    var opcoes = document.getElementById("opcoes")
    var opcoesTexto = ""

    for(var atributo in cartaPlayer.atributos){
        opcoesTexto += "<input type='radio' name='atributo' value='"+atributo+"'>"+atributo
    }
    opcoes.innerHTML = opcoesTexto
}

function obtemAtrSel() {
    var radioAtr = document.getElementsByName("atributo")
    for (let i = 0; i < radioAtr.length; i++) {
        if(radioAtr[i].checked){
            return radioAtr[i].value
        }
        
    }
}

function jogar(){
    var atrSel = obtemAtrSel()
    var elemRes = document.getElementById("resultado")
    var valorPlayer = cartaPlayer.atributos[atrSel]
    var valorIA = cartaIA.atributos[atrSel]

    if(valorPlayer>valorIA){
        elemRes.innerHTML = "Voce venceu"
    }
    else if(valorIA>valorPlayer){
        elemRes.innerHTML = "Voce perdeu"
    }
    else{
        elemRes.innerHTML = "Empate"
    }

    console.log(cartaIA)
}