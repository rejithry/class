package com.test.btree;

import java.util.Arrays;

public class MergeSort {
	String[] sort(String[] a) {
		if (a.length == 1) {
			return a;
		} else {
			int mid = a.length / 2;
			String[] s1 = Arrays.copyOfRange(a, 0, mid);
			String[] s2 = Arrays.copyOfRange(a, mid, a.length);
			String []s3 =  merge(sort(s1), sort(s2));
			return s3;
		}
	}

	String[] merge(String[] s1, String[] s2) {
		String[] s3 = new String[s1.length + s2.length];
		int length = s1.length + s2.length;
		int i = 0, j = 0, l = 0;
		while (l < length) {
			if(i >= s1.length){
				s3[l] = s2[j];
				j++;
			}
			else if(j >= s2.length){
				s3[l] = s1[i];
				i++;
			}
			else {
				if (s1[i].compareTo(s2[j]) < 0) {
					s3[l] = s1[i];
					i++;
				} else {
					s3[l] = s2[j];
					j++;
				}
			}
			l++;
		}
		return s3;

	}

}
