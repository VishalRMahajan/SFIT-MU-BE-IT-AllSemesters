import java.util.Scanner; //used to take input

public class count {
    public static void main(String[] args) {
        System.err.print("Enter the word: ");
       
        Scanner sc = new Scanner(System.in);
        String word = sc.next();

        word = word.toLowerCase();
        
        int length = word.length();
        int vowel = 0, consonant = 0;

        for (int i = 0; i < length; i++) {
            char ch = word.charAt(i);

            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                vowel++;
            } else {
                consonant++;
            }
        }

        System.out.println("No. of Vowel in " + word + " is " + vowel);
        System.out.println("No. of Consonant in " + word + " is " + consonant);
    }
}