package problemofjava;

class Node {

	int data;
	Node next;

	Node(int data) {
		this.data = data;
		this.next = null;
	}
}

public class ReverseLinkedList {

	public static void main(String[] args) {

		// Create Linked List
		Node head = new Node(1);
		head.next = new Node(2);
		head.next.next = new Node(3);
		head.next.next.next = new Node(4);
		head.next.next.next.next = new Node(5);

		System.out.println("Original Linked List:");
		display(head);

		head = reverse(head);

		System.out.println("\nReversed Linked List:");
		display(head);
	}

	// Reverse Method
	public static Node reverse(Node head) {

		Node prev = null;
		Node current = head;

		while (current != null) {

			Node next = current.next;

			current.next = prev;

			prev = current;
			current = next;
		}

		return prev;
	}

	// Display Method
	public static void display(Node head) {

		Node temp = head;

		while (temp != null) {
			System.out.print(temp.data + " ");
			temp = temp.next;
		}
	}
}
