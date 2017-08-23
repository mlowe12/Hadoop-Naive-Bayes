import java.util.*;
import java.io.*; 
import java.lang.*;
import org.apache.hadoop.io.*; 
import org.apache.hadoop.conf.*; 
import org.apache.hadoop.mapreduce.*;  



public class WordMap{

    public static class Map extends Mapper<LongWritable, Text, Text, IntWritable>{

        public void map(LongWritable key, Text value, Context context) throws InterruptedException, IOException{
            String observedLined = value.toString(); 
            StringTokenizer tok = new StringTokenizer(observedLine); 
            while(tok.hasMoreTokens()){
                value.set(tok.nextToken()); 
                context.write(value, new IntWritable());

            }
        }
    }

    public static void main(String[] args){
        //System.out.println("Success");
    }
}
