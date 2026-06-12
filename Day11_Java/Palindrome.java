//given a string determine if it is a palindrome 
//ignore a special characters
//input value - madam , race car , z ,""

package Day10_placement;
import java.util.Scanner;
public class Palindrome {
	

	public class PalindromeString {

	    public static void main(String[] args) {

	        Scanner sc = new Scanner(System.in);

	        System.out.print("Enter a string: ");
	        String str = sc.nextLine();

	        str = str.toLowerCase().replaceAll("[^a-z0-9]", "");

	        String reverse = "";

	        for (int i = str.length() - 1; i >= 0; i--) {
	            reverse = reverse + str.charAt(i);
	        }

	        if (str.equals(reverse)) {
	            System.out.println("Palindrome");
	        } else {
	            System.out.println("Not Palindrome");
	        }

	        sc.close();
	    }
	}

}
