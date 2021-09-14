function Converter() {
    var valorE = document.getElementById("valor");
    var valor = valorE.value;
    var valorDolar = parseFloat(valor);
  
    var valorReal = valorDolar * 5;
    console.log(valorReal);
  
    var elementoConvertido = document.getElementById("valorConvertido");
  
    var valorConvertido = "O resultado em real: R$ " + valorReal;
    elementoConvertido.innerHTML = valorConvertido;
  }
  