"""
# Quantum Hello World
[Documentation](https://docs.quantum.ibm.com/start/hello-world)

Implement a 2 Qubit gate where the first qubit is transformed first with an Hadamard operator.
"""

from qiskit import QuantumCircuit


# Create a quantum circuit with n qubits
n = 2
qc = QuantumCircuit(n)

# add Hadamard gate to qbit 0
qc.h(0)

# Perform a controlled-X gate on qubit 1, controlled by qubit 0
qc.cx(0, 1)

# Return a drawing of the circuit using MatPlotLib ("mpl"). This is the
# last line of the cell, so the drawing appears in the cell output.
# Remove the "mpl" argument to get a text drawing.
qc.draw("mpl", style="iqp")

from qiskit.quantum_info import Pauli
 
ZZ = Pauli('ZZ')
ZI = Pauli('ZI')
IZ = Pauli('IZ')
XX = Pauli('XX')
XI = Pauli('XI')
IX = Pauli('IX')

Z = Pauli('Z')
Z.to_matrix()
