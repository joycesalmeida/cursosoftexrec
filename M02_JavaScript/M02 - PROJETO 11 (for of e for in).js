let filme = {
    nome: 'A Fantástica Fábrica de Chocolate',
    Ano: 1971,
    categoria: 'fantasia',
};

for (let caracteristica in filme) {
  console.log(caracteristica + ": " + filme[caracteristica]);
}

var letras = ['a', 'b', 'c'];
for (let i in letras) {
    console.log(i);
}

for (let i of letras) {
    console.log(i);
}