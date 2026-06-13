package leetcode61;

import java.util.Stack;

public class ValidParentheses {

    public static void main(String[] args) {

        String s = "([])";

        Stack<Character> stack = new Stack<>();

        boolean valid = true;

        for (char ch : s.toCharArray()) {

            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else {

                if (stack.isEmpty()) {
                    valid = false;
                    break;
                }

                char top = stack.pop();

                if ((ch == ')' && top != '(') ||
                    (ch == '}' && top != '{') ||
                    (ch == ']' && top != '[')) {

                    valid = false;
                    break;
                }
            }
        }

        if (!stack.isEmpty()) {
            valid = false;
        }

        System.out.println(valid);
    }
}
