package Day10_placement;

public class numtables {

	    public static void main(String[] args) {

	        for (int table = 2; table <= 10; table++) {

	            System.out.println("Table of " + table);

	            for (int i = 1; i <= 10; i++) {
	                System.out.println(table + " * " + i + " = " + (table * i));
	            }

	            System.out.println();
	        }
	    }
	}


