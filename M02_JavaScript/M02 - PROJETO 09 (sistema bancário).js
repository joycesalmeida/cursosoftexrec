//Definindo informações do titular da conta.
var cliente = {
    banco: "Popular",
    titular: "Joyce Almeida",
    conta: 12345,
    agencia: 123,
    tipoConta: "corrente",
    saldo: 100.00,

}

//Efetuando um depósito na conta.
var deposito = function(valor){
    cliente.saldo = cliente.saldo + valor;
}

//Efetuando um saque da conta.
var saque = function(valor){
    cliente.saldo = cliente.saldo - valor;
}

//Consultando o saldo atual da conta.
var consultar_saldo = function(){
    console.log('SALDO: ' + cliente.saldo);
}

//Consultando informações do titular da conta.
var consultar_cliente = function(){
    console.log('Banco: ' + cliente.banco);
    console.log('Titular: ' + cliente.titular);
    console.log('Conta: ' + cliente.conta);
    console.log('Agencia: ' + cliente.agencia);
    console.log('Tipo da Conta: ' + cliente.tipoConta);
    console.log('Saldo: ' + cliente.saldo);
}

consultar_cliente();

deposito(250.00);
consultar_saldo();

saque(75);
consultar_saldo();