import java.util.Scanner;

public class EXP4code {
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);

        // Input: Number of data bits
        System.out.println("Enter the number of data bits:");
        int dataSize = scanner.nextInt();

        // Input: Data bits
        System.out.println("Enter the data bits:");
        int[] data = new int[dataSize];
        for (int i = 0; i < dataSize; i++) {
            data[i] = scanner.nextInt();
        }

        // Input: Number of generator bits
        System.out.println("Enter the number of generator bits:");
        int generatorSize = scanner.nextInt();

        // Input: Generator bits
        System.out.println("Enter the generator bits:");
        int[] generator = new int[generatorSize];
        for (int i = 0; i < generatorSize; i++) {
            generator[i] = scanner.nextInt();
        }

        // CRC Encoding
        int[] encodedData = encodeCRC(data, generator);

        // Output: Appended data word
        System.out.println("The Appended data word is");
        printArray(encodedData);

        // Output: Transmitted code word
        System.out.println("Transmitted code word is:");
        printArray(encodedData);

        // CRC Decoding (Receiver side)
        System.out.println("At Receiver side, ");
        System.out.println("Enter the received code word:");
        int[] receivedData = new int[encodedData.length];
        for (int i = 0; i < encodedData.length; i++) {
            receivedData[i] = scanner.nextInt();
        }

        int[] remainder = divideCRC(receivedData, generator);

        // Output: Remainder after division
        System.out.println("The remainder after dividing received codeword by generator bits is:");
        printArray(remainder);

        // Output: Check for errors
        if (isZeroArray(remainder)) {
            System.out.println("As remainder is zero, received code word has no errors.");
        } else {
            System.out.println("As remainder is non zero, the received code word has errors.");
        }
    }

    // CRC Encoding Algorithm
    private static int[] encodeCRC(int[] data, int[] generator) 
    {
        int dataSize = data.length;
        int generatorSize = generator.length;
        int appendedSize = dataSize + generatorSize - 1;
        int[] appendedData = new int[appendedSize];

        // Copy data bits to the front of appendedData
        System.arraycopy(data, 0, appendedData, 0, dataSize);

        // Append zeros to the end of appendedData
        for (int i = dataSize; i < appendedSize; i++) {
            appendedData[i] = 0;
        }

        // Perform CRC Division
        int[] remainder = divideCRC(appendedData, generator);

        // Replace zeros with CRC remainder
        System.arraycopy(remainder, 0, appendedData, dataSize, generatorSize - 1);
        return appendedData;
    }

    // CRC Division Algorithm
    private static int[] divideCRC(int[] data, int[] generator)
     {
        int dataSize = data.length;
        int generatorSize = generator.length;
        int[] remainder = new int[generatorSize];
        System.arraycopy(data, 0, remainder, 0, generatorSize);

        for (int i = 0; i <= dataSize - generatorSize; i++) {
            if (remainder[0] == 1) {
                // XOR operation
                for (int j = 0; j < generatorSize; j++) {
                    remainder[j] = remainder[j] ^ generator[j];
                }
            }

            // Shift remainder to the right
            for (int j = 0; j < generatorSize - 1; j++) {
                remainder[j] = remainder[j + 1];
            }

            // Insert next bit from data
            if (i < dataSize - generatorSize) {
                remainder[generatorSize - 1] = data[i + generatorSize];
            }
        }
        return remainder;
    }

    // Utility function to check if an array is all zeros
    private static boolean isZeroArray(int[] array)
    {
        for (int value : array) {
            if (value != 0) {
                return false;
            }
        }
        return true;
    }

    // Utility function to print an array
    private static void printArray(int[] array) 
    {
        for (int value : array) {
            System.out.println(value);
        }
    }
}
