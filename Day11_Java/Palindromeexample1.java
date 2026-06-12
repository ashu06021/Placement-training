//solve inO(1) extra space and on(n) time complexity

package Day10_placement;
import java.util.Scanner;

public class Palindromeexample1 {
	

	    public static void main(String[] args) {

	        Scanner sc = new Scanner(System.in);

	        System.out.print("Enter a string: ");
	        String str = sc.nextLine();

	        int left = 0;
	        int right = str.length() - 1;

	        boolean palindrome = true;

	        while (left < right) {

	            while (left < right &&
	                   !Character.isLetterOrDigit(str.charAt(left))) {
	                left++;
	            }

	            while (left < right &&
	                   !Character.isLetterOrDigit(str.charAt(right))) {
	                right--;
	            }

	            if (Character.toLowerCase(str.charAt(left)) !=
	                Character.toLowerCase(str.charAt(right))) {
	                palindrome = false;
	                break;
	            }

	            left++;
	            right--;
	        }

	        if (palindrome) {
	            System.out.println("Palindrome");
	        } else {
	            System.out.println("Not Palindrome");
	        }

	        sc.close();
	    }
	}
	
