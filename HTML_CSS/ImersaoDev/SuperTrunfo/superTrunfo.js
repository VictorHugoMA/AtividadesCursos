var carta1 = {  nome: "Reyna",
                imagem: "https://img.ibxk.com.br/2020/06/01/01124655734193.jpg",
                atributos:{ataque: 9, defesa: 6, magia: 8}
                }

var carta2 = {  nome:"Jet",
                imagem: "https://images2.alphacoders.com/114/thumb-1920-1149474.jpg",
                atributos:{ataque:9, defesa: 5, magia: 5}
                }

var carta3 = {  nome: "KillJoy",
                imagem: "https://conteudo.imguol.com.br/c/entretenimento/a0/2020/07/29/valorant-killjoy-1596049018638_v2_450x337.png", 
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
    exibirCartaPlayer()
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
    var divRes = document.getElementById("resultado")
    var valorPlayer = cartaPlayer.atributos[atrSel]
    var valorIA = cartaIA.atributos[atrSel]

    if(valorPlayer>valorIA){
        elemRes = "<p class='resultado-final'>Venceu</p>"
    }
    else if(valorIA>valorPlayer){
        elemRes = "<p class='resultado-final'>Perdeu</p>"
    }
    else{
        elemRes = "<p class='resultado-final'>Empatou</p>"
    }

    divRes.innerHTML = elemRes;

    document.getElementById("btnJogar").disabled = true;
    exibirCartaIA()
}

function exibirCartaPlayer() {
    var divCartaP = document.getElementById("carta-jogador")
    divCartaP.style.backgroundImage=`url(${cartaPlayer.imagem})`
    var moldura =
    '<img src="https://www.alura.com.br/assets/img/imersoes/dev-2021/card-super-trunfo-transparent-ajustado.png" style=" width: inherit; height: inherit; position: absolute;">'
    var tagHTML = "<div id='opcoes' class='carta-status'>"

    var opcoesTexto = ""
    for(var atributo in cartaPlayer.atributos){
        opcoesTexto += "<input type='radio' name='atributo' value='"+atributo+"'>"+atributo + " " + cartaPlayer.atributos[atributo] + "<br>"
    }

    var nome = `<p class="carta-subtitle">${cartaPlayer.nome}</p>`

    divCartaP.innerHTML = moldura + nome + tagHTML + opcoesTexto + "</div>"
}

function exibirCartaIA() {
    var divCartaIA = document.getElementById("carta-maquina")
    divCartaIA.style.backgroundImage=`url(${cartaIA.imagem})`
    var moldura =
    '<img src="https://www.alura.com.br/assets/img/imersoes/dev-2021/card-super-trunfo-transparent-ajustado.png" style=" width: inherit; height: inherit; position: absolute;">'
    var tagHTML = "<div id='opcoes' class='carta-status'>"

    var opcoesTexto = ""
    for(var atributo in cartaIA.atributos){
        opcoesTexto += "<p type='text' name='atributo' value='"+atributo+"'>"+atributo + " " + cartaIA.atributos[atributo] + "</p>"
    }

    var nome = `<p class="carta-subtitle">${cartaIA.nome}</p>`

    divCartaIA.innerHTML = moldura + nome + tagHTML + opcoesTexto + "</div>"

}