var listaFilmes = []

listaFilmes.push("https://observatoriodocinema.uol.com.br/wp-content/uploads/2021/02/homem-de-ferro-tony-divulgacao.jpg")
listaFilmes.push("https://images-3.wuaki.tv/system/shots/184879/original/snapshot-1590658151.jpeg")
listaFilmes.push("https://ichef.bbci.co.uk/news/640/cpsprodpb/BF0D/production/_106090984_2e39b218-c369-452e-b5be-d2476f9d8728.jpg")

for (let i = 0; i < listaFilmes.length; i++) {
    document.write("<img src=" + listaFilmes[i] + ">")
    
}