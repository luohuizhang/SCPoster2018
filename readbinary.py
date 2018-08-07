import numpy as np
import array
import sys

def storeMatrix(filename,m1):
    mat1 = np.matrix(m1)
    with open(filename,'wb') as f:
    	for line in mat1:
                np.savetxt(f, line.real, fmt='%f')


fin = open("Inputdata/FLUT_1_1800_3600.dat", 'rb')
vals = array.array('f',(1800*3600)*[0])
#print vals
fin.readinto(vals)
fin.close()
new=np.reshape(vals,(-1,3600))
storeMatrix("Data.dat",new)
