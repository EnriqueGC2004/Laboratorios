package org.example;

import java.sql.SQLOutput;
import java.util.Scanner;

public class FoorLoop {

    public static void main(String[] args) {

        int loops = 0;
        Scanner sc = new Scanner(System.in);

        System.out.println("Ingresa el número de ciclos requeridos: ");
        loops = sc.nextByte();

        for (int count = 0; count < loops; count++) {

            System.out.println("Número actual de iteración: " + count );
        }

    }
}
