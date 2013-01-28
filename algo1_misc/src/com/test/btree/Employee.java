package com.test.btree;

public class Employee {
	String empName;
	int empNo;
	Employee prev, left, right;
	Employee()
	{
		
	}
	Employee(String name, int no, Employee p, Employee l, Employee r ){
		this.empName = name;
		this.empNo = no;
		this.prev = p;
		this.left = l;
		this.right = r;
	}
}
