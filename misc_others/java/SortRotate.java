package com.test;

public class SortRotate {
	public static void main(String args[]){
		String s = "Password";
		String s2 = "wordPaas";
		String s3 = s + s;
		if (s2.length() !=  s.length())
			System.out.println(false);
		else
			System.out.println(s3.contains(s2));
	}

}
