const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const app = express();

//Conexão com o banco de dados MongoDB
mongoose.connect('mongodb://localhost/banco-de-dados', { useNewUrlParser: true });
const db = mongoose.connection;

// Verificar se houve erro na conexão com o banco de dados
db.on('error', console.error.bind(console, 'Erro na conexão com o MongoDB'));

// Verificar se a conexão com o banco de dados foi estabelecida com sucesso
db.once('open', function() {
  console.log('Conexão com o MongoDB estabelecida com sucesso');
});

// Definir um schema para o modelo de dados
const Schema = mongoose.Schema;
const userSchema = new Schema({
  name: String,
  email: String,
  password: String
});

// Definir um modelo de dados com base no schema definido anteriormente
const User = mongoose.model('User', userSchema);

// Configurar o middleware bodyParser para interpretar JSON
app.use(bodyParser.json());

// Definir a rota para criar um novo usuário
app.post('/users', function(req, res) {
  const user = new User({
    name: req.body.name,
    email: req.body.email,
    password: req.body.password
  });

  user.save(function(err) {
    if (err) {
      console.error(err);
      res.status(500).send('Erro ao criar usuário');
    } else {
      res.send('Usuário criado com sucesso');
    }
  });
});

// Definir a rota para listar todos os usuários
app.get('/users', function(req, res) {
  User.find(function(err, users) {
    if (err) {
      console.error(err);
      res.status(500).send('Erro ao recuperar usuários');
    } else {
      res.send(users);
    }
  });
});

// Definir a rota para recuperar um usuário específico
app.get('/users/:id', function(req, res) {
  User.findById(req.params.id, function(err, user) {
    if (err) {
      console.error(err);
      res.status(500).send('Erro ao recuperar usuário');
    } else if (!user) {
      res.status(404).send('Usuário não encontrado');
    } else {
      res.send(user);
    }
  });
});

// Definir a rota para atualizar um usuário específico
app.put('/users/:id', function(req, res) {
  User.findByIdAndUpdate(req.params.id, req.body, {new: true}, function(err, user) {
    if (err) {
      console.error(err);
      res.status(500).send('Erro ao atualizar usuário');
    } else if (!user) {
      res.status(404).send('Usuário não encontrado');
    } else {
      res.send(user);
    }
  });
});

// Definir a rota para excluir um usuário específico
app.delete('/users/:id', function(req, res) {
