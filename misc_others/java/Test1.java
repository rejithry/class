public class Test1
{
    private String s;

    Test1(String a)
    {
	s = a;
    }
    void printString(){
	System.out.println(s);
	    }

    void changeString() {
	s = "World";
	    }
    void change(String t, MyInt i, int j){
	t = "Changed" + t;
	i.setInt(10);
	j = 20;
    }
    public static void main(String args[]){
	Test1 t1 = new Test1("Hello");
	    t1.printString();
	    t1.changeString();
	    t1.printString();
	    String t="String";
	    System.out.println(t);
	    MyInt m = new MyInt(5);
	    m.toString();
	    int j = 1;
	    t1.change(t,m,j);
	    System.out.println(t);
	    System.out.println(m.i);
	    System.out.println(j);
	    
    }
}

class MyInt{
    public int i;
    MyInt(int i){
	this.i = i;
    }
    
    void setInt(int i){
	this.i  = i;
    }

    int getInt(){
	return i;
    }

    public String toString(){
	System.out.println(i);
	return "Int";
    }
}