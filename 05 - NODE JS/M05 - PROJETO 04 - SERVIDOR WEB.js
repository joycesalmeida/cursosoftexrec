const express = require('express')
const app = express()

// Rota estática
app.get('/', (req, res) => {
  res.send('Bem-vindo à página principal')
})

// Rota dinâmica com placeholder
app.get('/usuarios/:id', (req, res) => {
  const { id } = req.params
  res.send(`Informações do usuário ${id}`)
})

// Rota dinâmica com query
app.get('/pesquisa', (req, res) => {
  const { q } = req.query
  res.send(`Resultado da pesquisa por ${q}`)
})

app.listen(3000, () => {
  console.log('Servidor rodando na porta 3000')
})
