package org.example;

import java.util.Scanner;
public class imputs {


    public static void  main(String[] args) {

        String name;
        int age;
        String mesage = "Hola %s, tu edad es %s";

        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el nombre: ");
        name = sc.nextLine();

        System.out.println("Ingrese el edad: ");
        age = sc.nextInt();

        sc.close();
        String finaMesssage = String.format(mesage, name, age);
        System.out.println(finaMesssage);
    }
}
