# QCDC
A tool for inspecting quantum circuits step by step. It displays each gate layer as a matrix operator acting on the current system state, and then shows the resulting state after the operation. This makes it easy to trace, debug, and understand the evolution of a quantum system layer by layer.
<br>
The repository contains two files:
<br>
#
QCDC.py: Provides the ready-to-use print_submatrices function, which implements the core functionality.It has 2 parameters:
<br>
            qc (QuantumCircuit): Quantum Circuit to be used
            <br>
            display_circ (bool): If true the circuit gates at each step will be printed alongside the              corresponding operator
            <br>
#
Use_Case.ipynb: A simple example notebook demonstrating how to use print_submatrices on a sample quantum circuit.
