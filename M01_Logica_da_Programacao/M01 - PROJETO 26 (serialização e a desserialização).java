// Criando uma Classe

public class Aluno implements java.io.Serializable {
    public String nome;
    public String curso;
    public transient int id;
    public int ano;
    public void verificaEmail() {
        System.out.printIn("Checagem para: " + nome + "" + curso);
    }
}


// Serializando o Objeto

public class Serializa {
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Aluno e = new Aluno();
        e.nome = "Joyce Almeida";
        e.curso = "Programação Back-End";
        e.id = 7872526;
        e.ano = 2022;
        try {
           FileOutputStream fileOut = new FileOutputStream("C:\\Users\\Aluno\\Desktop\\Joyce\\matricula.txt");
           ObjectOutputStream out = new ObjectOutputStream(fileOut);
           out.writeObject(e);
           out.close();
           fileOut.close();
           System.out.printf("Os dados serializados estão salvo no arquivo matricula.ser");
        }catch (IOException i){
        }
    }
}


// Desserializando o objeto

public class Desserializando
{
    public static void main(String[] args)
    {
        Aluno e;
        try{
            try(FileInputStream fileIn = new FileInputStream("C:\\Users\\Aluno\\Desktop\\Joyce\\matricula.ser");
                ObjectinputStream in = new ObjectinputStream(fileIn)){
                    e = (Aluno) in.readObject();
                }
        }catch(IOException i)
        {
            return;
        }catch(ClassNotFoundException c)
        {
            System.out.printIn("Classe Aluno não encontrada!");
            return;
        }
        System.out.printIn("Aluno desserializado...");
        System.out.printIn("Nome: " + e.nome);
        System.out.printIn("Curso: " + e.curso);
        System.out.printIn("ID: " + e.id);
        System.out.printIn("Ano: " + e.ano);
    }
}
