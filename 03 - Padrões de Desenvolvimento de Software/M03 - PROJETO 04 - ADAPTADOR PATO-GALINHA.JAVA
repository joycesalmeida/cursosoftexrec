public interface Galinha {
    void cacarejar();
    void botarOvo();
}

public class Pato {
    public void grasnar() {
        System.out.println("Quack, quack");
    }
    
    public void voar() {
        System.out.println("Pato voando");
    }
    
    public void nadar() {
        System.out.println("Pato nadando");
    }
    
    public void botarOvo() {
        System.out.println("Pato botou um ovo");
    }
}

public class AdaptadorPato implements Galinha {
    private Pato pato;
    
    public AdaptadorPato(Pato pato) {
        this.pato = pato;
    }
    
    public void cacarejar() {
        pato.grasnar();
    }
    
    public void botarOvo() {
        pato.botarOvo();
    }
}

public class AdaptadorPatoDemo {
    public static void main(String[] args) {
        Pato pato = new Pato();
        Galinha adaptador = new AdaptadorPato(pato);
        
        adaptador.cacarejar();
        adaptador.botarOvo();
    }
}
