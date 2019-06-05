package com.vehiculos.datosii;

import javax.swing.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.PrintWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;

/**
 * Implementation of a algorithm to assign shared vehicles.
 * Data Structure: Graph with adyacence matrix.
 * Complexity: Better and worse case O(n*n).
 *
 * @author Abraham Miguel Lora Vargas
 * @author Juan Manuel Young Hoyos
 * @version 3.1
 *
 */
public class FastPath {

    /**
     * Method to read a file with the vehicle owners and the company.
     * Complexity: Better and worse case O(n*n), where 'n' are the vehicle owners and the company.
     *
     * @param pointsNumber The company number is '1' and the vehicle owners are 'n - 1'.
     * @return A complete graph with the shortest distance between all the vertices.
     *
     */
    public static AdaptedGraph readFile(int pointsNumber, float p){

        final String fileName = "dataset-ejemplo-U=" + pointsNumber + "-p=" + p + ".txt";
        AdaptedGraph graph = new AdaptedGraph(pointsNumber);

        try {

            BufferedReader br = new BufferedReader(new FileReader(fileName));
            String currentlyLine = br.readLine();

            for (int i = 1; i <= 3; i++) // Discard the first 3 lines.
                currentlyLine = br.readLine();

            currentlyLine = br.readLine();

            for (int i = 1; i <= pointsNumber; i++) // Discard the names and coordinates of the vertices.
                currentlyLine = br.readLine();

            for (int i = 1; i <= 3; i++) //  Discard the first 3 lines.
                currentlyLine = br.readLine();

            while (currentlyLine != null){ // As long as it does not reach the end of the file. Read the information of the edges.

                String[] partitionedChain = currentlyLine.split(" ");

                if(partitionedChain[0] == "")
                    continue;

                if(partitionedChain.length >= 2 && partitionedChain[1] == "")
                    continue;

                if(partitionedChain.length >= 3 && partitionedChain[2] == "")
                    continue;

                graph.addEdge(
                        Integer.parseInt(partitionedChain[0]) - 1,
                        Integer.parseInt(partitionedChain[1]) - 1,
                        Integer.parseInt(partitionedChain[2]));

                currentlyLine = br.readLine();
            }

        }
        catch(IOException ioe) {
            System.out.println("Error reading the input file: " + ioe.getMessage());
        }
        return graph;
    }

    /**
     * First part of the merge sort method which is implemented to order the graph,
     * through the weights of the arcs of each event with the "pos" point.
     *
     * @param input Successors of a vertex.
     * @param graph complete graph with the shortest distance between all vertices.
     * @param pos Origin vertex or reference.
     *
     */
    public static void sort(ArrayList<Integer> input, AdaptedGraph graph, int pos) {

        if(input.size() < 2)  // If it is less than 2 the size does not need to be organized.
            return;

        int mid = input.size() / 2;

        ArrayList<Integer> left = new ArrayList<>(mid);
        ArrayList<Integer> right = new ArrayList(input.size() - mid);

        for(int i = 0; i < mid; i++) // copy left
            left.add(i, input.get(i));

        for(int i = 0; i < input.size() - mid; i++) // copy right
            right.add(i, input.get(mid+i));

        sort(left, graph, pos);
        sort(right, graph, pos);
        merge(left, right, input, graph, pos);
    }

    /**
     * Second part of the merge sort method in which the successor arrangement
     * divides two arrangements until it is located from minor to major.
     *
     * @param a
     * @param b
     * @param all
     * @param graph
     * @param pos
     *
     */
    private static void merge(ArrayList<Integer> a, ArrayList<Integer> b, ArrayList<Integer> all, AdaptedGraph graph, int pos){

        int i = 0, j = 0, k = 0;

        while(i < a.size() && j < b.size()) { // merge back

            if(graph.getWeight(pos, a.get(i)) < graph.getWeight(pos, b.get(j))) { // a.get(i) < b.get(j)
                all.set(k, a.get(i));//[k] = a[i];
                i++;
            } else {
                all.set(k, b.get(j));//[k] = b[j];
                j++;
            }

            k++;

        }

        while(i < a.size()) // left remaining
            all.set(k++, a.get(i++)); //all[k++] = a[i++];

        while(j < b.size()) // right remaining
            all.set(k++, b.get(j++)); //all[k++] = b[j++];

    }

    public static float closingTime(AdaptedGraph graph,int ver,float p){
        return graph.getWeight(0, ver) * p;
    }

    /**
     * Method that finds the minimum number of cars, starting from the
     * beginning that is going to try to find a shorter path to the vertex that is
     * further from the company through other vertices;
     * once grouped the vertex are eliminated from the arrangement of the vertices of the company 
     * so the complexity in the worst case is O (n).
     *
     * @param graph complete graph with the shortest distance between all the vertices.
     * @param vertexList List of ArrayList in which they contain each of their arcs ordered from least to greatest.
     * @return A list of the lists with the minimum number of cars.
     *
     */
    public static LinkedList<ArrayList<Integer>> generateSolution(AdaptedGraph graph,LinkedList<ArrayList<Integer>> vertexList, float p){

        LinkedList<ArrayList<Integer>> sharedCars = new LinkedList<>();

        boolean[] visited = new boolean[vertexList.size()];
        int pathCost = 0;

        while(vertexList.get(0).size() > 1){ // List of vertices that arrive at the company ordered from lowest to highest.

            int major = vertexList.get(0).get(vertexList.get(0).size() - 1); // Vertex farthest from the company.

             /**
              * Add the list of possible vehicle shared with other vertices starting from the vertex farthest from the company.
              */
             sharedCars.add(sharedPath(graph, major, visited, vertexList, pathCost, p));

             /**
              * Remove the vertices that were used in the previous vehicle from the vertexList list in order to decrease the cycle.
              */
             for (int i = 0; i < sharedCars.get(sharedCars.size() - 1).size(); i++)
                 vertexList.get(0).remove(vertexList.get(0).indexOf(sharedCars.get(sharedCars.size() - 1).get(i)));

        }

        return sharedCars;
    }

    /**
     * Method that groups the vertices that have the lowest cost to 
     * other vertices until it reaches the maximum limit (5) or until
     * it reaches the universe without looking at the car.
     *
     * @param graph complete graph with the shortest distance between all the vertices.
     * @param major Vertex farthest from the company..
     * @param visited Boolean fix (true-> if it was already visited or false-> if it has not been visited).
     * @param vertexList List of ArrayList in which they contain each of their arcs ordered from minor to major.
     * @param pathCost
     * @return A list of vertices.
     */
    public static ArrayList<Integer> sharedPath(AdaptedGraph graph, int major, boolean[] visited, LinkedList<ArrayList<Integer>> vertexList, int pathCost, float p){

        ArrayList<Integer> path = new ArrayList<>();

        int pos = 1;
        float ownerPath = closingTime(graph, vertexList.get(0).get(vertexList.get(0).size() - 1), p);
        float minorOrigin = ownerPath;

        int pathToMajor = 0;
        int major_origen = 0;

        float pathWithMajor = 0;

        for(int i = 0; i < vertexList.get(0).size(); i++) {

            if (path.size() == 5 && pathCost <= ownerPath) {

                return path;

            } else {

                pathToMajor = graph.getWeight(major, vertexList.get(major).get(pos));
                pathCost += pathToMajor;
                major_origen = graph.getWeight(0, vertexList.get(major).get(pos)) + pathToMajor;

                if(major != vertexList.get(major).get(pos) && // so you do not go to yourself
                        pathCost <= ownerPath && // so that it does not exceed the maximum time of the first vertex.
                        !visited[vertexList.get(major).get(pos)] && // so that it does not return to previously selected vertices.
                        0 != vertexList.get(major).get(pos) && // so you do not write down that you can get to the university.
                        major_origen <= minorOrigin) {

                    path.add(major);
                    visited[major] = true;
                    i = 0; // restart the cycle.

                    major = vertexList.get(major).get(pos);
                    pathWithMajor = closingTime(graph, major, p);
                    minorOrigin = Math.min(minorOrigin - graph.getWeight(major, vertexList.get(major).get(pos)), pathWithMajor);

                    pos = 1; // Restart the search from the minor.

                } else {
                    pathCost -= graph.getWeight(major,vertexList.get(major).get(pos++));
                }
            }

        }

        pathCost += graph.getWeight(0, major);

        if (!visited[major] && pathCost <= ownerPath) {

            path.add(major);
            visited[major] = true;

        }

        return path;
    }

    /**
     * Method to write a file with the answer.
     * Complexity: Better and worst case is O (n), where n are the owners of the vehicle and the company.
     *
     * @param  permutations is a list of lists with the permutation for each subset of the vehicle owners' partition.
     */
    public static void generateFile(LinkedList<ArrayList<Integer>> permutations,int pointsNumber, float p){

        try {

            PrintWriter writer = new PrintWriter(
                    "respuesta-ejemplo-U=" + pointsNumber + "-p=" + p + ".txt",
                    "UTF-8");

            for (ArrayList<Integer> permutation : permutations) {

                for (Integer vehicleOwner : permutation)
                    writer.print((vehicleOwner + 1) + " ");

                writer.println();

            }

            writer.close();

        } catch(IOException ioe) {
            System.out.println("Error writing the output file " + ioe.getMessage() );
        }

    }

    public static void main(String[] args) {

        System.out.println("[ALGORITHM] Starting FastPath...");
        System.out.println("[ALGORITHM] Starting reading arguments...");

        // Receive the number of vehicle owners and the company, and the value of p for the main.
        int pointsNumber = args.length == 0 ? 205 : Integer.parseInt(args[0]); // 205
        float latencyTime = args.length < 2 ? 1.3f : Float.parseFloat(args[1]);

        SELECTOR : if(args.length == 0) {

            Object[] option = { "Yes", "No" };

            int selection = JOptionPane.showOptionDialog(null,
                    "Do you want to enter the number of nodes and the percentage of latency?",
                    "Choose an option:",
                    JOptionPane.DEFAULT_OPTION,
                    JOptionPane.QUESTION_MESSAGE,
                    null,
                    option,
                    option[0]);

            if(selection == 0) {

                JTextField uField = new JTextField(5);
                JTextField pField = new JTextField(5);

                JPanel myPanel = new JPanel();

                myPanel.add(new JLabel("Number of Nodes (U):"));
                myPanel.add(uField);
                myPanel.add(Box.createHorizontalStrut(15));

                myPanel.add(new JLabel("Latency Percentage (p):"));
                myPanel.add(pField);

                int result = JOptionPane.showConfirmDialog(
                        null,
                        myPanel,
                        "Please select the data-set attributes",
                        JOptionPane.OK_CANCEL_OPTION);

                if (result == JOptionPane.OK_OPTION) {

                    pointsNumber = Integer.parseInt(uField.getText());
                    latencyTime = Float.parseFloat(pField.getText());

                    System.out.println("[ALGORITHM] The maximum latency has been defined to: " + latencyTime);
                    System.out.println("[ALGORITHM] The number of vertices has been defined to: " + pointsNumber);

                }

            }

        }

        System.out.println("[ALGORITHM] Reading file...");

        // Read the file with the distances between the owners of the vehicle and the company.
        AdaptedGraph graph = readFile(pointsNumber, latencyTime);
        LinkedList<ArrayList<Integer>> vertexList = new LinkedList<>();

        // long startTime = System.currentTimeMillis();
        for (int i = 0; i < graph.size; i++){
            ArrayList<Integer> succesors = graph.getSuccessors(i);
            sort(succesors, graph, i);
            vertexList.add(succesors);
        }

        // Assign shared vehicles.
        long startTime = System.currentTimeMillis();
        LinkedList<ArrayList<Integer>> permutations = generateSolution(graph, vertexList, latencyTime); // Start ALGORITHM.

        long estimatedTime = System.currentTimeMillis() - startTime;
        System.out.println("[ALGORITHM] El ALGORITHM tomo un tiempo de: " + estimatedTime + "ms");

        // Print total memory consumed.
        System.out.println("[ALGORITHM] Memoria total consumida: " + (Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory()) / 1000000);

        // Generate answer file.
        generateFile(permutations, pointsNumber, latencyTime);
    }
}