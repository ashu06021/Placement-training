package problemofjava;

import java.util.Scanner;

public class SquareRoot {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		System.out.print("Enter a number: ");
		int num = sc.nextInt();

		int i = 1;

		while (i * i <= num) {
			i++;
		}

		System.out.println("Square Root = " + (i - 1));

		sc.close();
	}
}
