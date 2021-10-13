import numpy as np
import matplotlib.pyplot as plt


## Input truss material properties
E = 29e3 # Units: ksi
A = 2    # Units: sq in

nodes = [] # Node coordinates
elems = [] # Element connections

## Assemble nodal coordinates array (Units: ft)
nodes.append([0, 0])
nodes.append([10, 10])
nodes.append([20, 10])
nodes.append([10, 0])

## Assemble element connections array
elems.append([1, 2])
elems.append([2, 3])
elems.append([3, 4])
elems.append([1, 3])
elems.append([4, 2])


## Format the output
nodes = np.array(nodes).astype(float)
elems = np.array(elems)

## Convert the node coordinates from ft to in
nodesInFt = nodes * 12


## Assemble the global force vector - units: k
# f1, f2, f7, & f8 are unknown support reactions
F = np.zeros_like(nodes)


## F[2, 0] Applied: node 2 in x-direction OR
# F[2, 1] Applied: node 2 in y-direction
F[2, 1] = -30 # Units: kips


""" 
## Test the outputs thus far:

print(nodes)
print(" ")
print(testConvert)
print(" ")
print(elems)
print(" ")
print(F)
"""


# Support displacements
Ur = [0, 0, 0, 0] # Global dof's 1, 2, 7, & 8

# Note: Global dof's 3, 4, 5, & 6 are unknown, non-zero displacements

DofConn = np.ones_like(nodes).astype(int)
DofConn[0, :] = 0


### Truss structural analysis

def TrussAnalysis():
  NN = len(nodes)
  NE = len(elems)
  DOF = 2
  NDOF = DOF * NN
  
  # Structural analysis
  d = nodes[elems[:, 1], :] - nodes[elems[:, 0], :]



