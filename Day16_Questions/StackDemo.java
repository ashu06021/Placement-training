// Question: Reverse a String using Stack

import java.util.Stack;

public class StackDemo {

    public static void main(String[] args) {

        String str = "JAVA";

        Stack<Character> stack = new Stack<>();

        for(char ch : str.toCharArray()) {
            stack.push(ch);
        }

        while(!stack.isEmpty()) {
            System.out.print(stack.pop());
        }
    }
}