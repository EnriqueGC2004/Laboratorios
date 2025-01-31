package org.example;

public class ElselfStatement {


    public static void main(String[] args) {

        int age = 16;

        if (age <= 12) {
            System.out.println("Eres un niño");
        } else if (age < 17) {
            System.out.println("Eres un adolescente");
        } else if (age < 38) {
            System.out.println("Eres un adulto joven");
        } else {
            System.out.println("Eres un adulto");
        }
    }
}
