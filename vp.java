import java.util.Scanner;

public class vp {

    public static void main(String[] args) {

        String pass;
        int turnsCount = 0;

        Scanner input = new Scanner(System.in);
        String[] num = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};

        int k = input.nextInt();

        String[] rollers = new String[k];
        String[][] rollersNum = new String[k][9];
        String[] passNum;

        pass = input.next();
        int passi = Integer.parseInt(pass);

        passNum = pass.split("");

        for (int i = 0; i < k; i++) {
            
            String roll = input.next();
            int roller = Integer.parseInt(roll);
            rollers[i] = roll;

        }

        for (int o = 0; o < k; o++) {
            String[] a = rollers[o].split("");
            rollersNum[o] = a;
        }

        for (int i = 0; i < k; i++) {
            int index = index(passNum[i], rollersNum[i]);
            int smaller = smaller(index, 9 - index);
            turnsCount = turnsCount + smaller;
        }

        System.out.println(turnsCount);

    }

    private static int getDigitsCount(int number) {
        int count = 0;
        do {
            number = number / 10;
            count += 1;
        } while (number > 0);
        return count;
    }

    private static int smaller(int x, int y) {
        int smaller;
        if (x <= y) {
            smaller = x;
        } else {
            smaller = y;
        }
        return smaller;
    }

    private static int index(String s, String[] ss) {
        int index = 0;

        for (int i = 0; (i < ss.length); i++) {
            if (s.equals(ss[i])) {
                index = i;
            }
        }
        return index;
    }
}
