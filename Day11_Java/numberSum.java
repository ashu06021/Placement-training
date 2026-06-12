//write a program to calculate the sum of the digits of a given positive integer 
//input prompt the user to enter a positive integer 
//output display the sum of the digits 
//logic use a for loop to iterate through each digit of the number and calculate the sum;



package Day10_placement;
import java.util.Scanner;
public class numberSum {
	
	    public static void main(String[] args) {

	        Scanner sc = new Scanner(System.in);

	        System.out.print("Enter a positive integer: ");
	        int number = sc.nextInt();

	        int sum = 0;

	        for (; number > 0; number = number / 10) {
	            int digit = number % 10;
	            sum = sum + digit;
	        }

	        System.out.println("Sum of digits = " + sum);

	        sc.close();
	    }
	}


