//1. Interface Sanduíche
public interface Sanduiche {
    public double preco();
    public String descricao();
}

//2. Implementação do Sanduíche de Frango Assado
public class FrangoAssado implements Sanduiche {
    public double preco() {
        return 4.50;
    }
    public String descricao() {
        return "Sanduíche de Frango Assado";
    }
}

//3. Classe abstrata Adicional
public abstract class Adicional implements Sanduiche {
    protected Sanduiche sanduiche;
    public Adicional(Sanduiche sanduiche) {
        this.sanduiche = sanduiche;
    }
    public double preco() {
        return sanduiche.preco();
    }
    public String descricao() {
        return sanduiche.descricao();
    }
}

//4. Implementação dos ingredientes adicionais Pepperoni e Queijo Mussarela Ralado
public class Pepperoni extends Adicional {
    public Pepperoni(Sanduiche sanduiche) {
        super(sanduiche);
    }
    public double preco() {
        return super.preco() + 0.99;
    }
    public String descricao() {
        return super.descricao() + ", Pepperoni";
    }
}

public class QueijoMussarelaRalado extends Adicional {
    public QueijoMussarelaRalado(Sanduiche sanduiche) {
        super(sanduiche);
    }
    public double preco() {
        return super.preco() + 2.00;
    }
    public String descricao() {
        return super.descricao() + ", Queijo Mussarela Ralado";
    }
}

//5. Criando o sanduíche com ingredientes adicionais
Sanduiche sanduiche = new
