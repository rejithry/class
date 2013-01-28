package com.test.btree;

import java.util.Arrays;

public class Test {
	public static void main(String args[]){
		String [] a = {"Rejith","Abhi","Musthu","Mano"};
		int mid = a.length/2;
		String []s1 = Arrays.copyOfRange(a, 0, mid  );
		String []s2 = Arrays.copyOfRange(a, mid, a.length);

		
		String [] s3 = new String[s1.length + s2.length ];
		for (int i=0; i< s1.length; i++)
			s3[i] = s1[i];
		for (int i=s1.length; i< s1.length + s2.length; i++)
			s3[i] = s2[i-s1.length];
		Test.printArray(s3);
	}
	static void printArray(String [] a){
			System.out.println(Arrays.toString(a));
	}

}
