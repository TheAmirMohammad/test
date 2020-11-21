import java.util.Scanner;

public class jamZirBaze {
    static Scanner input = new Scanner(System.in);
    // static Scanner input2 = new Scanner(System.in);
    public static void main(String[] args) {

        int sum = 0 ;

        int n = input.nextInt();
        int[] li = new int[n];

        for (int i=0 ; i<n ; i++)
        {
            int an = input.nextInt();
            li[]
        }
        // String[] li = an.split(" ");

        for (int i=0 ; i<n/2 ; i++)
        {
            int n2 = n -1 -i ;
            int tedad = count(i , n);
            int x1 = Integer.parseInt(li[i]);
            int x2 = Integer.parseInt(li[n2]);
            sum += tedad*(x1+x2);
        }

        if (isOdd(n))
        {
            int n2 = (n/2);
            int tedad = count(n2 , n);
            sum += tedad*(Integer.parseInt(li[n2]));
        }
        
        System.out.println(sum);
    }

    static boolean isOdd(int num)
    {
        if (num%2 == 0)
        {
            return false;
        }else
        {
            return true;
        }
    }

    static int count(int i , int n)
    {
        return (n-i)*(i+1);
    }
}