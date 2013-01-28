import java.io.IOException;
import java.util.Iterator;
import java.util.StringTokenizer;


import org.apache.hadoop.hbase.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.hbase.client.*;
import java.util.*;
import org.apache.hadoop.hbase.util.*;

public class ExampleClient {
    public static void main(String a[]) throws Exception{
	Configuration config = HBaseConfiguration.create();
	
	HBaseAdmin admin = new HBaseAdmin(config);
	HTableDescriptor htd = new HTableDescriptor("test");
	HColumnDescriptor hcd = new HColumnDescriptor("data");
	htd.addFamily(hcd);
	admin.createTable(htd);
	byte[] tablename = htd.getName();
	HTableDescriptor [] tables = admin.listTables();	
	if (tables.length!= 1 && Bytes.equals(tablename, tables[0].getName())){
	    throw new IOException("Failed create of table");
	}
	
	HTable table  = new HTable(config, tablename);
	byte [] row1 = Bytes.toBytes("row1");
	Put p1 = new Put(row1);
	byte [] databytes = Bytes.toBytes("data");
	p1.add(databytes, Bytes.toBytes("1"), Bytes.toBytes("value1"));
	table.put(p1);

	Get g = new Get(row1);
	Result result = table.get(g);
	System.out.println("Get: " + result);
	Scan scan = new Scan();
	ResultScanner scanner  = table.getScanner(scan);
	try {
	    for (Result scannerResult : scanner) {
		System.out.println("Scan : " +  scannerResult);
	    }
	}
	finally {
	    scanner.close();
	}
	
	admin.disableTable(tablename);
	admin.deleteTable(tablename);
    }
}
