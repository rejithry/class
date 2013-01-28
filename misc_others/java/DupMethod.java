package com.test;

interface A{
	int a();
}

interface B{
	int a();
}

public class DupMethod implements A, B {

	@Override
	public int a() {
		System.out.println("AB");
		return 0;
	}
	
public static void main(String args[]){
	A a = new DupMethod();
	B b = new DupMethod();
	
	a.a();
	b.a();
}
	
}
