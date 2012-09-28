package com.test.btree;

import java.util.Arrays;

public class QuickSort {
	String[] sort(String[] a) {
		if (a.length == 1) {
			return a;
		} else {
			return partition(a);
		}
	}

	String[] partition(String[] a) {
		String s1[] = null, s2[] = null;
		String pivot = a[0];
		int i = 1, j = a.length - 1;
		MergeMain.printArray(a);
		while (i <= j) {
			System.out.println(" i = " + i + " j = "+ j);
			if (a[i].compareTo(pivot) < 0){
				a[i-1] = a[i];
				a[i] = pivot;
				i++;
			}
			else if (a[j].compareTo(pivot) > 0){
				j--;
			}
			else {
				if(i != j){
				String t = a[i];
				a[i] = a[j];
				a[j] = t;
				j--;
				}
			}
		}
		System.out.println(" i = " + i + " j = "+ j);
		if(a.length ==2 && i == 2)
				i--;
				s1 = Arrays.copyOfRange(a, 0, i );
				s2 = Arrays.copyOfRange(a, i  , a.length);

		System.out.println("S1 and S2 are :");
		MergeMain.printArray(s1);
		MergeMain.printArray(s2);
		return joinString(sort(s1), sort(s2));

	}

	String[] joinString(String[] s1, String s2[]) {
		String[] s3 = new String[s1.length + s2.length];
		for (int i = 0; i < s1.length; i++)
			s3[i] = s1[i];
		for (int i = s1.length; i < s1.length + s2.length; i++)
			s3[i] = s2[i - s1.length];
		return s3;
	}

}
