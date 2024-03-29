/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package javaproject;

import java.util.Arrays;

public class App {
   private int[] array;
    public App(int[] array) {
        this.array = array;
    }

    public int comptarElements() {
        if (array!= null) {
            return array.length;
        } else {
            return 0;
        }
    }
    public int retornarPrimer() throws Exception {
        if (array == null || array.length == 0)
            throw new Exception("S'array es nul");
        return array[0];
    }
    public int retornarDarrer() throws Exception {
        if (array == null || array.length == 0)
            throw new Exception("S'array es nul");
        return array[array.length - 1];
    }
    public int retornarTercer() throws Exception {
        if (array == null || array.length == 0 || array.length < 3)
            throw new Exception("S'array es nul");
        return array[2];
    }
    public int sumaElements() throws Exception {
        if (array == null || array.length == 0)
            throw new Exception("S'array es nul");
        return Arrays.stream(array).sum();
    }
    public double mitjanaElements() throws Exception {
        if (array == null || array.length == 0)
            throw new Exception("S'array es nul");
        return (double) sumaElements() / array.length;
    }
}

