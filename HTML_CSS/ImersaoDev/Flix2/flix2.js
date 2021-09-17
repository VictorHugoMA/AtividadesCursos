function adicionarFilme() {
    var filmeFavorito = document.getElementById("filme").value;
    if (filmeFavorito.endsWith(".jpg")) {
      listarFilmesNaTela(filmeFavorito);
    } else {
      console.error(
        "Endereço de filme inválido, por favor coloque uma imagem.jpg");
    }
  
    document.getElementById("filme").value = "";
  }
  
  function listarFilmesNaTela(filme) {
    var elementoFilmeFavorito = "<img src =" + filme + ">";
    var elementolistaFilmes = document.getElementById("listaFilmes");
    elementolistaFilmes.innerHTML =
      elementolistaFilmes.innerHTML + elementoFilmeFavorito;
  }