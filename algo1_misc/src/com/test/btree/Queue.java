package com.test.btree;

public class Queue {
	String queue[];
	int tail = 0;
	int head = 0;

	Queue() {
		queue = new String[10];
	}

	void put(String s) {
		if ((tail + 1) % 10 == head)
			System.out.println("Queue is full");
		else {
			queue[tail] = s;
			tail = (tail + 1) % 10;
		}

	}
	String get() {
		if(tail == head){
			System.out.println("Queue is empty");
			return null;
		}
		else
		{
			String t = queue[head];
			head = (head + 1) % 10;
			return t;
		}
	}
	int length() {
		if(head < tail)
			return tail - head;
		else if (tail < head)
			return 10 + tail - head;
		else
			return 0;
	}
	public static void main(String args[]) {
		Queue q = new Queue();
		q.put("1");
		q.put("2");
		q.put("3");
		q.put("4");
		q.put("5");
		q.put("3");
		q.put("4");
		q.put("5");
		q.put("4");
		q.put("5");
		System.out.println(q.get());
		System.out.println(q.get());
		System.out.println(q.get());
		System.out.println(q.get());
		System.out.println(q.get());
		System.out.println(q.get());
		System.out.println("length is " + q.length());
		System.out.println(q.get());
		System.out.println(q.get());
		System.out.println(q.get());
		System.out.println("length is " + q.length());
		System.out.println(q.get());
		MergeMain.printArray(q.queue);
	}
}
