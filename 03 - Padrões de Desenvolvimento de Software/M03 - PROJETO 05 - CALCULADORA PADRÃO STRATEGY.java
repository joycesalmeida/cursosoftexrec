import java.util.Scanner;

interface Strategy {
    int execute(int num1, int num2);
}

class Soma implements Strategy {
    public int execute(int num1, int num2) {
        return num1 + num2;
    }
}

class Subtracao implements Strategy {
    public int execute(int num1, int num2) {
        return num1 - num2;
    }
}

class Multiplicacao implements Strategy {
    public int execute(int num1, int num2) {
        return num1 * num2;
    }
}

public class Calculadora {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Digite o primeiro número: ");
        int num1 = input.nextInt();
        System.out.println("Digite o segundo número: ");
        int num2 = input.nextInt();
        System.out.println("Digite a operação que deseja realizar (+, -, *): ");
        String operacao = input.next();
        Strategy strategy;
        switch (operacao) {
            case "+":
                strategy = new Soma();
                break;
            case "-":
                strategy = new Subtracao();
                break;
            case "*":
                strategy = new Multiplicacao();
                break;
            default:
                System.out.println("Operação inválida!");
                return;
        }
        int resultado = strategy.execute(num1, num2);
        System.out.println("Resultado: " + resultado);
    }
}
