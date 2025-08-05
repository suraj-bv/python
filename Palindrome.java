import java.util.Scanner;

class Palindrome {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a String: ");
        String str = sc.nextLine();
        int n = str.length();
        Boolean isPalindrome = true;
        for(int i = 0; i < n/2; i++){
            if (str.charAt(i) != str.charAt(n -i -1)){
                isPalindrome = false;
            }
        }
        if (isPalindrome){
            System.out.println("The given string is a PALINDROME");
        } else {
            System.out.println("The given string is NOT a PALNDROME");
        }
        sc.close();
    }

}