import java.util.Scanner;

public class duplicatelement
{	
	public static void main(String[] ags)
	{
	   Scanner sc = new Scanner(System.in);
	    
	   System.out.print("Enter the size of array: ");
	   int size= sc.nextInt();
	   
           int[] array= new int[size];
           
           for(int i=0;i<size;i++)
	   {
		System.out.print("Enter the "+ i +" element of array : ");
		array[i]=sc.nextInt(); 
	   }
		
          
		
	   System.out.print("Entered Array is ");
	   for(int i=0;i<size;i++)
	   {
		System.out.print(array[i] + " ");
	   }

	   boolean checkif=false;
	   for(int i=0;i<size;i++)
	   {
		for(int j=i+1;j<size;j++)
		{
		   if(array[i]==array[j])
			checkif=true;
		}
		
	   }

	   System.out.print("\n Does array have Duplicate element ? -" + checkif);
		
	}
}