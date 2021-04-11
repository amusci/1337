package com.company;

public class Main {

    public static void main(String[] args) {
        palindromChecker(1331);
    }


    public static boolean palindromChecker (int x) {


        if (x < 0)
        {
            return false;
        }
        String value = String.valueOf(x);
        int len = value.length() - 1;
        for (int i = 0; i < len / 2 + 1; i++)
        {
            if (value.charAt(i) != value.charAt(len - i))
            {
                System.out.println("Not palindrome!");
                return false;
            }
        }
        System.out.println("Palindrome!");
        return true;
    }
}
