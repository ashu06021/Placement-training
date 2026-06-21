// Question: Find the largest element in an array

public class LargestElement {

    public static void main(String[] args) {

        int[] arr = {10, 45, 20, 90, 35};

        int max = arr[0];

        for(int i = 1; i < arr.length; i++) {
            if(arr[i] > max) {
                max = arr[i];
            }
        }

        System.out.println("Largest = " + max);
    }
}