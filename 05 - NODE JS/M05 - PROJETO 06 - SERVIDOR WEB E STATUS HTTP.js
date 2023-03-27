const express = require('express');
const app = express();

app.get('/listar/:parametro', (req, res) => {
  const parametro = parseInt(req.params.parametro);
  if (parametro === 50) {
    res.status(404).send('Não foi possível listar');
  } else {
    res.status(200).send('Aqui está a lista!');
  }
});

app.listen(3000, () => {
  console.log('Servidor rodando na porta 3000');
});
