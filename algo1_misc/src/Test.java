class Employee {
	int no;
	
	Employee(){
		no = 5;
	}
	
	
}
public class Test {
	
	public static void main(String args[]){
		Employee e  = new Employee();
		System.out.println(e.no);
		new Test().test(e);
		System.out.println(e.no);

		
		
		
	}
	

	void test(Employee a){
		a.no = 10;
		
	}
	
}
