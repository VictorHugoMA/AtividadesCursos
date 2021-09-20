var victor = {nome: "Victor", vitorias: 0, empates: 0, derrotas: 0, pontos: 0}
var alisson = {nome: "Alisson", vitorias: 0, empates: 0, derrotas: 0, pontos: 0}
var daniel = {nome: "Daniel", vitorias: 0, empates: 0, derrotas: 0, pontos: 0}


function calculaPontos(jogador) {
    var pontos = (jogador.vitorias*3) + (jogador.empates)
    return pontos
}

function adicionarVitoria(i) {
    jogadores[i].vitorias+=1
    jogadores[i].pontos = calculaPontos(jogadores[i])
    exibeJogadoresNaTela(jogadores)
}
function adicionarEmpate(i) {
    jogadores[i].empates+=1
    jogadores[i].pontos = calculaPontos(jogadores[i])
    exibeJogadoresNaTela(jogadores)
}
function adicionarDerrota(i) {
    jogadores[i].derrotas+=1
    exibeJogadoresNaTela(jogadores)
}


victor.pontos = calculaPontos(victor)
alisson.pontos = calculaPontos(alisson)
daniel.pontos = calculaPontos(daniel)

var jogadores = [victor, alisson, daniel]

function exibeJogadoresNaTela(jogadores) {
    var elemento = ""
    for (let i = 0; i < jogadores.length; i++) {
        elemento+="<tr><td>"+jogadores[i].nome+"</td>"
        elemento+="<td>"+jogadores[i].vitorias+"</td>"
        elemento+="<td>"+jogadores[i].empates+"</td>"
        elemento+="<td>"+jogadores[i].derrotas+"</td>"
        elemento+="<td>"+jogadores[i].pontos+"</td>"
        elemento+="<td><button onClick='adicionarVitoria("+i+")'>Vitória</button></td>"
        elemento+="<td><button onClick='adicionarEmpate("+i+")'>Empate</button></td>"
        elemento+="<td><button onClick='adicionarDerrota("+i+")'>Derrota</button></td>"
        elemento+="</tr>"
    }
    var tabelaJogadores = document.getElementById("tabelaJogadores")
    tabelaJogadores.innerHTML = elemento
}

exibeJogadoresNaTela(jogadores)