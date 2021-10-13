import numpy as np
import matplotlib.pyplot as plt

# Input truss material properties
E = 29e3 # Units: ksi
A = 2    # Units: sq in

nodes = [] # Node coordinates
elems = [] # Element connections

# Assemble nodal coordinates array
nodes.append([0, 0])
nodes.append([10, 10])
nodes.append([20, 10])
nodes.append([10, 0])

# Assemble element connections array
elems.append([1, 2])
elems.append([2, 3])
elems.append([3, 4])
elems.append([1, 3])
elems.append([4, 2])

# Format the output
nodes = np.array(nodes).astype(float)
elems = np.array(elems)

F = [] # Global force vector

# Assemble the global force vector - units: k
# f1, f2, f7, & f8 are unknown support reactions
F.append([f1])
F.append([f2])
F.append([0])
F.append([-30])
F.append([0])
F.append([0])
F.append([f7])
F.append([f8])


