
package typecastin;

import java.util.Scanner;

public class AtmDenomination {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int[] notes = { 500, 200, 100 };

		System.out.print("Enter amount: ");
		int amount = sc.nextInt();

		System.out.println("\nDenominations:");

		for (int note : notes) {

			int count = amount / note;

			if (count > 0) {
				System.out.println(note + " x " + count);
				amount = amount % note;
			}
		}

		sc.close();
	}
}