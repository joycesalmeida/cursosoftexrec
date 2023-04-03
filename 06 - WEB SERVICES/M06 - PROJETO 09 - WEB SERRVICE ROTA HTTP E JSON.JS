const express = require('express')
const app = express()

app.use(express.json())

app.get('/', (req, res) => {
  res.send('Bem-vindo ao meu web service!')
})

app.post('/usuario', (req, res) => {
  const usuario = req.body
  console.log(usuario)
  res.json({ message: 'Usuário cadastrado com sucesso!', usuario })
})

app.listen(3000, () => {
  console.log('Web service iniciado na porta 3000!')
})
