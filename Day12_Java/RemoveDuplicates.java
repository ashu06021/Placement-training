package leetcode83;

class Node {

    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }
}

public class RemoveDuplicates {

    public static void main(String[] args) {

        Node head = new Node(1);
        head.next = new Node(1);
        head.next.next = new Node(2);
        head.next.next.next = new Node(3);
        head.next.next.next.next = new Node(3);

        Node current = head;

        while (current != null && current.next != null) {

            if (current.data == current.next.data) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }

        current = head;

        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
    }
}