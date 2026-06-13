package leetcode61;

class Node {

    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }
}

public class RotateList {

    public static void main(String[] args) {

        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);

        int k = 2;

        head = rotateRight(head, k);

        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }
    }

    public static Node rotateRight(Node head, int k) {

        if (head == null || head.next == null || k == 0)
            return head;

        int length = 1;
        Node tail = head;

        while (tail.next != null) {
            tail = tail.next;
            length++;
        }

        k = k % length;

        tail.next = head;

        int steps = length - k;

        Node newTail = head;

        for (int i = 1; i < steps; i++) {
            newTail = newTail.next;
        }

        Node newHead = newTail.next;

        newTail.next = null;

        return newHead;
    }
}