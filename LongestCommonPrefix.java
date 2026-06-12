package Day10_placement;


public class LongestCommonPrefix {

	    public static void main(String[] args) {

	        String[] strs = {"flower", "flow", "flight"};

	        String prefix = "";

	        for (int i = 0; i < strs[0].length(); i++) {

	            char ch = strs[0].charAt(i);

	            for (int j = 1; j < strs.length; j++) {

	                if (i >= strs[j].length() || strs[j].charAt(i) != ch) {
	                    System.out.println("Longest Common Prefix: " + prefix);
	                    return;
	                }
	            }

	            prefix += ch;
	        }

	        System.out.println("Longest Common Prefix: " + prefix);
	    }
	}

