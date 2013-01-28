package com.test;

import java.util.HashSet;

public class Perm {
	
	static HashSet<String> permute(String str){
		HashSet<String> p = new HashSet<String>();
		if (str.length() == 1){
			p.add(str);
			return p;
		}
		for (int i = 0; i < str.length(); i++){
			for (String l : permute(str.substring(0,i) + str.substring(i+1, str.length())))
				p.add(l + str.charAt(i));
		}
		return p;
	}

	public static void main(String args[]){
		System.out.println(Perm.permute("string"));
	}
}
