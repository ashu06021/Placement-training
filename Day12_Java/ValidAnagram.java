package leetcode61;

import java.util.Scanner;

public class ValidAnagram {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first string: ");
        String s = sc.nextLine();

        System.out.print("Enter second string: ");
        String t = sc.nextLine();

        if (isAnagram(s, t)) {
            System.out.println("Anagram");
        } else {
            System.out.println("Not Anagram");
        }

        sc.close();
    }

    public static boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        int[] count = new int[26];

        for (int i = 0; i < s.length(); i++) {

            count[s.charAt(i) - 'a']++;

            count[t.charAt(i) - 'a']--;
        }

        for (int i = 0; i < 26; i++) {

            if (count[i] != 0) {
                return false;
            }
        }

        return true;
    }
}
