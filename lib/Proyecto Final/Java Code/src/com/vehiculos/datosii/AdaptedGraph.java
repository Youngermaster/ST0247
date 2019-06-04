package com.vehiculos.datosii;

import java.util.ArrayList;

/**
 *  This class is based on the Graph class and its function is
 *  give a utility to handle the program.
 */
public class AdaptedGraph {

    protected int size;
    private int [][] aMGraph;

    public AdaptedGraph(int nodes) {
        size = nodes;
        aMGraph = new int[size][size];
    }

    /**
     * This method allows add a edge to the graph
     * bassed in a place 'from' to another place 'to'
     * with its own weight.
     *
     * @from From.
     * @to To.
     * @weight Edge's weight.
     */
    public void addEdge(int from, int to, int weight) {
        aMGraph[from][to] = weight;
    }

    /**
     * This method returns the ArrayList with the number of all the nodes who have a connection
     * with another one.
     *
     * @node Node number to extract the succesors.
     */
    public ArrayList<Integer> getSuccessors(int node) {

        ArrayList<Integer> succesors = new ArrayList<Integer>();

        for(int i = 0; i < size; i++)
            succesors.add(i);

        return succesors;

    }
    /**
     * This method returns the arc weight between two nodes.
     *
     * @source Desde.
     * @destination Hasta.
     */
    public int getWeight(int source, int destination) {
        return aMGraph[source][destination];
    }

    /**
     *
     * @return Get the graph size.
     */
    public int size() {
        return size;
    }
}