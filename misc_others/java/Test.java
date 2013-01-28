package com.test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Test {
	
	static Character getFirstUnique(String s){
		Map <Character, Integer> hm =  new HashMap<Character, Integer>();
		for (int i = 0 ; i < s.length(); i ++){
			if (hm.containsKey(s.charAt(i))){
					int v = hm.get(s.charAt(i)) + 1;
					hm.put(s.charAt(i), v);
			}
			else
				hm.put(s.charAt(i), 1);
			
		}
		for (int i = 0 ; i < s.length(); i ++){
			if (hm.get(s.charAt(i)) == 1)
				return s.charAt(i);
		}
		return null;
	}

	static String removeDupes(String s){
		Set  <Character> hm =  new HashSet<Character>();
		ArrayList<Character> al = new ArrayList<Character> ();
		for (int i = 0 ; i < s.length(); i ++){
			if (hm.add(s.charAt(i)))
				al.add(s.charAt(i));
			
		}
		StringBuilder sb = new StringBuilder();
		for (Character c : al){
			sb.append(c.toString());
		}
		return sb.toString();
	}
	
	public static void main(String args[]){
		System.out.println(Test.getFirstUnique("ABCABCCCCDCCCCCC"));
		System.out.println(Test.removeDupes("AAACCCCDBBB"));
	}
	
}
