package com.test.btree;


class Employee1 {
	String empName;
	int empNo;
	Employee1 next;
	Employee1(String empName, int empNo){
		this.empName = empName;
		this.empNo = empNo;
	}
}

public class Stack {
	Employee1 top = null;

	boolean isEmpty() {
		if (top == null)
			return true;
		else
			return false;
	}

	int push(Employee1 e) {
		if (top == null) {
			e.next = null;
			top = e;

		} else {
			e.next = top;
			top = e;

		}
		return 1;
	}

	Employee1 pop() {
		Employee1 t;
		if (!isEmpty()) {
			 t = top;
			if (top.next != null) {
				top = top.next;
			} else {
				top = null;
			}
		}
		else return null;
		return t;

	}
	int getSize(){
		int count = 1;
		Employee1 temp = top;
		if(temp ==null)
			return 0;
		else{
		while(temp.next != null){
				count++;
				temp = temp.next;
		}
		return count;
		}
	}
	public static void main(String args[]){
		Stack s =  new Stack();
		System.out.println(s.getSize());;
		if(s.isEmpty()){
			System.out.println("Stack is empty");
		}
		s.push(new Employee1("Rejith",1));
		s.push(new Employee1("Abhi",1));
		System.out.println(s.getSize());;
		s.push(new Employee1("rajesh",1));
		s.push(new Employee1("Manohar",1));
		System.out.println(s.getSize());;
		System.out.println(s.pop().empName);
		System.out.println(s.pop().empName);
		System.out.println(s.getSize());;
		System.out.println(s.pop().empName);
		System.out.println(s.getSize());;
		System.out.println(s.pop().empName);
		System.out.println(s.getSize());;
		System.out.println(s.pop());
		
	}
}