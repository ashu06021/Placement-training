package leetcode725;

class Node {

    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }
}

public class SplitLinkedList {

    public static void main(String[] args) {

        

        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);
        head.next.next.next.next.next = new Node(6);
        head.next.next.next.next.next.next = new Node(7);
        head.next.next.next.next.next.next.next = new Node(8);
        head.next.next.next.next.next.next.next.next = new Node(9);
        head.next.next.next.next.next.next.next.next.next = new Node(10);

        int k = 3;

        splitList(head, k);
    }

    public static void splitList(Node head, int k) {

        int length = 0;
        Node temp = head;

        while (temp != null) {
            length++;
            temp = temp.next;
        }

        int partSize = length / k;
        int extra = length % k;

        Node current = head;

        for (int i = 0; i < k; i++) {

            Node partHead = current;

            int currentSize = partSize;

            if (extra > 0) {
                currentSize++;
                extra--;
            }

            for (int j = 1; j < currentSize; j++) {
                if (current != null) {
                    current = current.next;
                }
            }

            if (current != null) {
                Node nextPart = current.next;
                current.next = null;
                current = nextPart;
            }

            System.out.print("Part " + (i + 1) + ": ");
            display(partHead);
        }
    }

    public static void display(Node head) {

        if (head == null) {
            System.out.println("[]");
            return;
        }

        while (head != null) {
            System.out.print(head.data + " ");
            head = head.next;
        }

        System.out.println();
    }
}