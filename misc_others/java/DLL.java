package com.test;

class Node1{
	String name;
	Node1 next;
	Node1 prev;
	Node1(){
		
	}
	Node1(String name){
		this.name = name;
	}
}

public class DLL {
	
	Node1 head;
	
	DLL(){
		head = null;
	}
	
	void add(String name){
		Node1 t = new Node1(name);
		if (head == null){
			
			t.next = t;
			t.prev = t;
			head = t;
		}
		else {
			t.next = head;
			t.prev = head.prev;
			head.prev = t;
			head = t;
		}
	}
	
	void delete(){
		head.prev.next = head.next;
		head.next.prev = head.prev;
		head = head.next;
	}
	
	void print(){
		Node1 cur = head;
		while(cur != head){
			System.out.println(cur.name);
			cur = cur.next;
		}
	}
	

	public static void main(String a[]){
		DLL ll = new DLL();
		ll.add("a");
		System.out.println(ll.head.next.name);
		ll.add("b");
		System.out.println(ll.head.next.next.name);
		ll.add("c");
		System.out.println(ll.head.next.next.next.name);
		ll.add("d");
		System.out.println(ll.head.next.next.next.next.name);
		
		
		
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
