import java.util.Scanner;


public class my{
    static float convert(int mile){
        float km =(float) (1.6 * mile);
        System.out.println("the req anser is " +  km);
        return km; 
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int miles = in.nextInt();
        float convert = convert(miles);
        System.out.println(convert);
        in.close();
        
    }
}
