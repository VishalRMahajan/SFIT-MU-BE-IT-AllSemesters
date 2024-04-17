import java.util.Scanner;


public class reverse
{
	public static void main(String[] args)
	{
		Scanner sc=new Scanner(System.in);
		
		
		
		System.out.print("Enter the Size of Array: ");
		int size = sc.nextInt();
		
		int[] ar= new int[size];
		int[] reverse= new int[size];


		for(int i=0;i<size;i++)
		{
		   System.out.print("Enter the "+ i+1 + " element of array : ");
		   ar[i]=sc.nextInt();
		}

	
			for(int j=0;j<size;j++)
		 	{
			      reverse[j]=ar[size-1-j];
			}

		

		System.out.print("Original Array is ");
		for(int i=0;i<size;i++)
		{
		    
		    System.out.print(ar[i] +" ");
		}

		System.out.print("\n Reversed Array is ");
		for(int i=0;i<size;i++)
		{
		    
		    System.out.print(reverse[i] +" ");
		}
    }
}