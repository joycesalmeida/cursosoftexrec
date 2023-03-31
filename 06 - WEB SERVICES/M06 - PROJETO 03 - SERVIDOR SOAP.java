/* CRIANDO O SERVIDOR SOAP SIMPLES COM 4 ENDPOINTS, UTILIZANDO AS BIBLIOTECAS JAX-WS e JAXB */

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.xml.bind.annotation.XmlElement;

@WebService
public class MeuServico {

    @WebMethod
    public String saudacao() {
        return "Olá, mundo!";
    }

    @WebMethod
    public int soma(int a, int b) {
        return a + b;
    }

    @WebMethod
    public Pessoa buscarPessoa(@XmlElement(required = true) String nome) {
        Pessoa pessoa = new Pessoa(nome, "Silva");
        return pessoa;
    }

    @WebMethod
    public int calcularIdade(int anoNascimento) {
        return 2023 - anoNascimento;
    }
}

public class Pessoa {

    private String nome;
    private String sobrenome;

    public Pessoa() {
    }

    public Pessoa(String nome, String sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }
}



/* COLOCANDO O SERVIDOR PRA RODAR NUMA PORTA 8080 */

import javax.xml.ws.Endpoint;

public class MeuServidor {

    public static void main(String[] args) {
        Endpoint.publish("http://localhost:8080/meuservico", new MeuServico());
    }
}

