package com.test;


class Node{
	String element;
	Node next;
	
	Node(){
		
	}
	Node(String element){
		this.element = element;
	}
}

public class Stack {
	
	Node top;
	
	Stack(){
		 top = null;
	}

	String pop(){
		if ( top  == null)
			System.out.println("Stack is empty");
		else{
			String t = top.element;
			top = top.next;
			return t;
		}
		return null;
	}
	
	void push(String s){
		Node t = new Node(s);
		if (top == null){
			t.next = null;
			top = t;
		}
		else {
			t.next = top;
			top =t;
		}
	}
	
	public static void main(String a[]){
		Stack s = new Stack();
		System.out.println(s.pop());
		s.push("test");
		System.out.println(s.pop());
		System.out.println(s.pop());s.push("a");
		s.push("b");
		System.out.println(s.pop());
		System.out.println(s.pop());
		System.out.println(s.pop());
	}
}




