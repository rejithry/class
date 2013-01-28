import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;


public class InversionCounter {
	static  long count = 0;
	public static void main(String args[])
	  {
		int a[] =  new int[100000];
	  try{
	  // Open the file that is the first 
	  // command line parameter
	  FileInputStream fstream = new FileInputStream("f:\\file.txt");
	  // Get the object of DataInputStream
	  DataInputStream in = new DataInputStream(fstream);
	  BufferedReader br = new BufferedReader(new InputStreamReader(in));
	  String strLine;
	  //Read File Line By Line
	  int i = 0;
	  while ((strLine = br.readLine()) != null)   {
	  // Print the content on the console
		  a[i++] = Integer.valueOf(strLine);
	  }
	  //Close the input stream
	  in.close();
	    }catch (Exception e){//Catch exception if any
	  System.err.println("Error: " + e.getMessage());
	  }
	  //int [] c = {10,2,1,4,3,9,7};
	  int[] b = new Course().sort(a);
	  
	  System.out.println(count);
	  //System.out.println(Arrays.toString(b));
	  }
	int[] sort(int[] a) {
		if (a.length == 1) {
			return a;
		} else {
			int mid = a.length / 2;
			int[] s1 = Arrays.copyOfRange(a, 0, mid);
			int[] s2 = Arrays.copyOfRange(a, mid, a.length);
			int []s3 =  merge(sort(s1), sort(s2));
			return s3;
		}
	}

	int[] merge(int[] s1, int[] s2) {
		int[] s3 = new int[s1.length + s2.length];
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
				if (s1[i] < s2[j]) {
					//count ++;
					s3[l] = s1[i];
					i++;
				} else {
					s3[l] = s2[j];
					count = count + s1.length - i ;
					j++;
				}
			}
			l++;
		}
		return s3;

	}
		
	

}
