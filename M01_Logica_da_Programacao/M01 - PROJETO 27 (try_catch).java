package material.excecao
import java.util.Scanner;

//Criando uma classe

public class Calculadora {
    public static void main(String[] args){
        try {
            Scanner s = new Scanner(System.in);
            System.out.print("Digite o valor do dividendo: ");
            int numero1 = s.nextInt();

            System.out.print("Digite o valor do divisor: ");
            int numero2 = s.nextIn();

            Calculadora teste = new Calculadora();

            System.out.printIn("Resto: " + teste.restoDaDivisao(numero1, numero2));
        } catch (ErroDivisao ex){
            System.out.printIn(ex.getMessage());
        }
    }

    public int restoDaDivisao(int dividendo, int divisor) thrwos ErroDivisao {
        if(divisor > dividendo) {
            throw new ErroDivisao();
        }
        return dividendo % divisor;
    }
}
