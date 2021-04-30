# Determine distance between bonded atoms in Angstrom.
# Input is water.xyz
#
import os
import numpy as np
#
# set up data
#
xyz_data = os.path.abspath ('C:\\Users\\agrif\\Desktop\\Comp Chem\\geometry_analysis\\water.xyz')
#print(xyz_data)
data = numpy.genfromtxt(fname=xyz_data, skip_header=2, dtype='unicode')
symbols = data[:,0]
coords = data[:,1:]
coords_f = coords.astype(numpy.float)
#print(coords_f)
atoms = len(symbols)
for atom_1 in range(0, atoms):
    for atom_2 in range(0,atoms):
        X = ((coords_f[atom_1,0]-coords_f[atom_2,0])**2)
        Y = ((coords_f[atom_1,1]-coords_f[atom_2,1])**2)
        Z = ((coords_f[atom_1,2]-coords_f[atom_2,2])**2)
        BL = numpy.sqrt(X + Y + Z)
        BL_round = (F'{BL:.3f}')
        #print(BL_round)
        print(symbols[atom_1], 'to', symbols[atom_2], '=', BL_round)
