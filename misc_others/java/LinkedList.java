package com.test;


public class LinkedList {
	
	Node head, tail;
	
	LinkedList(){
		head = null;
		tail = null;
	}
	
	void add(String s){
		Node t = new Node(s);
		if (head == null){
			t.next = null;
			head = t;
			tail  = t;
		}
		else{
			t.next = head;
			head = t;
		}
	}
	
	void addToEnd(String s){
		Node t = new Node(s);
		if (tail == null){
			t.next = null;
			tail = t;
			head = t;
		}
		else{
			tail.next = t;
			t.next = null;
			tail = t;
		}
	}
	
	void traverseList(){
		Node curNode = head;
		while(curNode != null){
			System.out.println(curNode.element);
			curNode = curNode.next;
		}
	}
	
	public static void main(String a[]){
		LinkedList l = new LinkedList();
		l.addToEnd("a");
		l.addToEnd("b");
		l.addToEnd("c");
		l.addToEnd("d");
		l.addToEnd("e");
		l.addToEnd("f");
		l.add("1");
		l.add("2");
		l.add("3");
		l.traverseList();
	}

}
