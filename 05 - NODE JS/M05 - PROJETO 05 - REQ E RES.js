const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Olá, mundo!');
});

app.post('/', (req, res) => {
    res.send('Requisição POST recebida');
});

app.put('/', (req, res) => {
    res.send('Requisição PUT recebida');
});

app.delete('/', (req, res) => {
    res.send('Requisição DELETE recebida');
});

app.listen(3000, () => {
    console.log('Servidor rodando na porta 3000');
});

/* Para rodar o código, abra o terminal na pasta onde o arquivo .js foi salvo
e execute o comando node nome-do-arquivo.js.
Em seguida, abra o navegador e acesse a URL http://localhost:3000/ para ver a mensagem de resposta da rota GET.
Para testar as outras rotas, é preciso utilizar um cliente HTTP, como o Postman ou o Insomnia. */