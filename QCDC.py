# This code is created by Georgios-Marios Merkouris and Ioannis Liliopoulos for educational purposes
# QCDC => Quantum Circuit DeComposer

from qiskit.converters import circuit_to_dag, dag_to_circuit
from IPython.display import display
from qiskit.quantum_info import Operator
import numpy as np
from qiskit.quantum_info import Statevector
from qiskit.circuit import QuantumCircuit

def print_submatrices(qc: QuantumCircuit, display_circ: bool = False):
    '''
        Function that allows users to check the Operator matrices at each computational step of their quantum circuit

        Params:
            qc (QuantumCircuit): Quantum Circuit to be used
            display_circ (bool): If true the circuit gates at each step will be printed alongside the corresponding operator

    '''

    np.set_printoptions(precision=3, suppress=True)
    dag = circuit_to_dag(qc)
    index = 1
    state = Statevector.from_int(0, 2**qc.num_qubits)
    state.draw('latex')

    for layer in dag.layers():
        if(layer['graph'].op_nodes()[0].op.name in ['measure', 'barrier']):
            continue
        layer_as_circuit = dag_to_circuit(layer['graph'])
        op=Operator(layer_as_circuit)

        if(display_circ):
            display(layer_as_circuit.draw('mpl',reverse_bits=True))
        
        print(f'Computational Step: {index}')
        print(f'Circuit Matrix: \n{op.data}')

        state=state.evolve(op)
        print("")
        print("Quantum Register Statevector after applying this quantum gate step:")
        print(state.data)
        print("\n")
        index += 1

