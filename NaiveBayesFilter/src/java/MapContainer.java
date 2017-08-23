import java.util.*; 


public class MapContainer{

    protected ArrayList<HashMap<String,Object>> mapList; 
    public final String filepath; 
    public final String instanceID;
    public int size; 
    public MapContainer(String filepath, String instanceID){
        this.filepath = filepath; 
        this.instanceID = instanceID;
        this.mapList = null; 
        this.size = 0; 
    }

    public void appendMapList(HashMap<String,Object> map){
        this.mapList.append(map);
        ++this.size; 
        return;
    }
    public ArrayList<HashMap<String,Object>> getMapList(){
        return this.mapList; 
    }

    public void partition(){
        return; 
    }

}