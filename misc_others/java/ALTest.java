package com.test;

import java.util.ArrayList;
import java.util.List;

public class ALTest {
	
	public static void main(String args[]){
		List<String> al = new ArrayList<String>();
		al.add("A");
		al.add("B");
		al.add("C");
		System.out.println(al.size());
		al.remove(1);
		System.out.println(al.size());
		al.add(1, "D");
		System.out.println(al.size());
		for (String a : al)
			System.out.println(a);
	}

}
