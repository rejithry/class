package com.test.btree;

import java.util.ArrayList;

public class EmpManager {

	Employee addEmployee(ArrayList<Employee> elist, Employee e, Employee root,
			Employee prev, String dir) {
		if (root == null) {
			e.prev = prev;
			elist.add(e);
			if (!(dir == null)) {
				if (dir.equals("r")) {
					prev.right = e;
				} else {
					prev.left = e;
				}
			}
		} else if (e.empName.compareTo(root.empName) < 0) {
			addEmployee(elist, e, root.left, root, "l");
		} else {
			addEmployee(elist, e, root.right, root, "r");
		}
		return e;
	}

	void printEmpList(Employee root) {
		if (!(root.left == null)) {
			printEmpList(root.left);
		}
		System.out.println(root.empName);
		if (!(root.right == null)) {
			printEmpList(root.right);
		}

	}

}
