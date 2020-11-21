import java.util.Scanner;

public class myLifeStory {

    public static void main(String[] args) {

        int totalDays = 0 ;

        int m1 ;
        int d1 ;
        int m2 ;
        int d2 ;

        Scanner input = new Scanner(System.in);

        m1 = input.nextInt();
        d1 = input.nextInt();
        m2 = input.nextInt();
        d2 = input.nextInt();

        if (m2-m1 != 0)
        {
            for (int i = m1 ; i < m2; i++) {
                int day = witchMonth(i);
                totalDays += day;
            }
        }

        totalDays = totalDays - d1 + d2 ;

        System.out.print(totalDays);
    }

    private static int witchMonth(int month)
    {
        int days;

        if ( month == 12)
        {days = 29;}
        else if ( month>=7 )
        {days = 30;}
        else { days = 31;}

        return days;
    }
}
