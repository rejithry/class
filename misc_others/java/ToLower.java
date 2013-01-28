package com.hadoopbook.pig;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.pig.EvalFunc;
import org.apache.pig.FuncSpec;
import org.apache.pig.backend.executionengine.ExecException;
import org.apache.pig.data.DataType;
import org.apache.pig.data.Tuple;
import org.apache.pig.impl.logicalLayer.FrontendException;
import org.apache.pig.impl.logicalLayer.schema.Schema;

public class ToLower extends EvalFunc<String> {

  @Override
      public String exec(Tuple input) throws IOException {
      if (input == null || input.size() == 0) {
	  return null;
      }
      try {
	  Object object = input.get(0);
	  if (object == null) {
	      return null;
	  }
	  return ((String) object).toLowerCase();
      } catch (ExecException e) {
	  throw new IOException(e);
      }
  }

  @Override
      public List<FuncSpec> getArgToFuncMapping() throws FrontendException {
      List<FuncSpec> funcList = new ArrayList<FuncSpec>();
      funcList.add(new FuncSpec(this.getClass().getName(), new Schema(
								      new Schema.FieldSchema(null, DataType.CHARARRAY))));

      return funcList;
  }
}
