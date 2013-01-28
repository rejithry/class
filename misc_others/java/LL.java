package com.test;

public class LL {
	
	Node head;
	
	LL() {
		head = null;
	}
	
	void add(String element){
		Node t = new Node(element);
			t.next = head;
			head = t;
	}
	
	void delete(){
		if (head != null){
			head = head.next;
			
		}
	}
	
	void print(){
		Node cur = head;
		while(cur != null){
			System.out.println(cur.element);
			cur = cur.next;
		}
	}

	public static void main(String a[]){
		LL ll = new LL();
		ll.add("a");
		ll.add("b");
		ll.add("c");
		ll.add("d");
		
		ll.print();
		
		ll.delete();
		ll.delete();
		System.out.println("deleted 2");
		ll.print();
		
		ll.delete();
		ll.delete();
		System.out.println("deleted all");
		
		ll.print();
		
		ll.delete();
		ll.print();
		
		ll.add("new");
		ll.print();
		
	}
}
