from numpy import array
from numpy import matmul
from numpy import sqrt
from qiskit.quantum_info import Statevector
from qiskit.quantum_info import Operator
from qiskit.visualization import plot_histogram
from qiskit import QuantumCircuit
from IPython.display import Latex, display, display_latex

ket0 = array([1, 0])
ket1 = array([0, 1])

M1 = array([[1, 1], [0, 0]])

display(matmul(M1, ket1))

# Statevectors

u = Statevector([1 / sqrt(2), 1 / sqrt(2)]) # x.ket0 + y.ket1
v = Statevector([(1 + 2.0j) / 3, -2 / 3])
w = Statevector([1 / 3, 2 / 3])

print("State vector u can be represented as:")
display(v.draw("latex")) # mathematical representation in the for of ket0 and ket1
display(v.draw("text")) # matrix representation
display(v.isValid(), w.isValid()) #is it a valid quantum vector state
display(v.measure()) # probabilistic outcome, can vary with each execution

statistics = v.sample_counts(1000) # ,easuring 1000 times
display(statistics)
plot_histogram(statistics)

# Operators

X = Operator([[0, 1], [1, 0]])
Y = Operator([[0, -1.0j], [1.0j, 0]])
Z = Operator([[1, 0], [0, -1]])
H = Operator([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]])
S = Operator([[1, 0], [0, 1.0j]])
T = Operator([[1, 0], [0, (1 + 1.0j) / sqrt(2)]])

v = Statevector([1, 0])

v = v.evolve(H)
v = v.evolve(T)
v = v.evolve(H)
v = v.evolve(T)
v = v.evolve(Z)

display(v.draw("latex"))
display(v.draw("text"))

# Circuits

circuit = QuantumCircuit(1)

circuit.h(0)
circuit.t(0)
circuit.h(0)
circuit.t(0)
circuit.z(0)

circuit.draw()

ket0 = Statevector([1, 0])
v = ket0.evolve(circuit)
v.draw("text")

statistics = v.sample_counts(4000)
plot_histogram(statistics)
