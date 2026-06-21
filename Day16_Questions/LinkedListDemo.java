// Question: Create a Linked List and display it

class Node {

    int data;
    Node next;

    Node(int data) {
        this.data = data;
    }
}

public class LinkedListDemo {

    public static void main(String[] args) {

        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);

        Node temp = head;

        while(temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
    }
}