public class Interleave {
	private Node head1;
	private Node head2;
	private Node head3;
	private Node head4;

	public static void main(String[] args) {
		Interleave program = new Interleave();
		program.run();
	}

	public void run() {
		// Build each test list

		// 1
		head1 = new Node(1, null);

		// 1, 2
		head2 = new Node(1, new Node(2, null));

		// 1, 2, 3, 4, 5
		for (int i = 5; i >= 1; i--) {
			Node newNode = new Node(i, head3);
			head3 = newNode;
		}

		// 1, 2, 3, 4, 5, 6
		for (int i = 6; i >= 1; i--) {
			Node newNode = new Node(i, head4);
			head4 = newNode;
		}

		interleave(head1);
		System.out.print("\n");
		interleave(head2);
		System.out.print("\n");
		interleave(head3);
		System.out.print("\n");
		interleave(head4);
	}

	private Node interleave(Node head) {
		if (head == null) {
			return null;
		}

		Node slow = head;
		Node fast = head;

		int length = 1;

		while (fast.getNext() != null) {
			if (fast.getNext().getNext() != null) {
				fast = fast.getNext().getNext();
				slow = slow.getNext();
				length += 2;
			} else {
				fast = fast.getNext();
				length += 1;
			}
		}

		Node firstStack;
		Node secondStack;

		// append to end
		Node iterator = head;
		for (int i = 0; i < length / 2 - 1; i++) {
			iterator = iterator.getNext();
		}
		iterator.setNext(null);
		firstStack = head;

		// insert at start
		iterator = slow;
	}

	private class Node {
		private int data;
		private Node next;

		public Node(int data, Node next) {
			this.data = data;
			this.next = next;
		}

		public int getData() {
			return this.data;
		}

		public Node getNext() {
			return this.next;
		}

		public void setNext(Node next) {
			this.next = next;
		}
	}
}
