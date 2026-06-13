package problemofjava;

import merging.Node;

class Node {

	int data;
	Node next;

	Node(int data) {
		this.data = data;
		this.next = null;
	}
}

public class LinkedListDemo {

	public static void main(String[] args) {

		Node node1 = new Node(1);
		Node node2 = new Node(2);
		Node node3 = new Node(3);
		Node node4 = new Node(4);
		Node node5 = new Node(5);

		// Linking nodes
		node1.next = node2;
		node2.next = node3;
		node3.next = node4;
		node4.next = node5;

		// Head points to first node
		Node head = node1;

		// Display Linked List
		Node temp = head;

		System.out.println("Linked List:");

		while (temp != null) {
			System.out.print(temp.data + " ");
			temp = temp.next;
		}
	}
}
