import java.util.Vector;

public class vectorexample {
    public static void main(String[] args) {

        Vector<String> vector = new Vector<>();

        vector.add("Element 1");
        vector.add("Element 2");
        vector.add("Element 3");

        System.out.println("Vector Elements: " + vector);

        System.out.println("Vector Size: " + vector.size());

        System.out.println("Is Vector Empty? " + vector.isEmpty());

        System.out.println("Element at index 1: " + vector.get(1));
    

    }
}