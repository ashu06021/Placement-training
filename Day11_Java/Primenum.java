//Problem statement create a program that generates and stores all prime numbers up to a given number in a list
// input - a positive number 
// output - display the list of prime numbers
// logic write a function that checks if a number is prime 
// use a loop to generate all prime numbers up to n and store them in a list
// challenge - prompt the user to enter a positive integer n 



package Day10_placement;
import java.util.ArrayList;
import java.util.Scanner; 
public class Primenum {

	    public static boolean isPrime(int num) {
	        if (num < 2) {
	            return false;
	        }

	        for (int i = 2; i < num; i++) {
	            if (num % i == 0) {
	                return false;
	            }
	        }

	        return true;
	    }

	    public static void main(String[] args) {

	        Scanner sc = new Scanner(System.in);

	        System.out.print("Enter a positive integer: ");
	        int n = sc.nextInt();

	        ArrayList<Integer> primes = new ArrayList<>();

	        for (int i = 2; i <= n; i++) {
	            if (isPrime(i)) {
	                primes.add(i);
	            }
	        }

	        System.out.println("Prime Numbers: " + primes);

	        sc.close();
	    }
	}

