from __future__ import division
import sys
import array
import adios as ad
import scipy.stats as stats
import os


import numpy as np
import matplotlib.pyplot as plt
import os
import array

def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split() for line in fr.readlines()]
    print np.shape(stringArr)
   # print stringArr
    datArr = [map(float, line) for line in stringArr]
    return np.mat(datArr)
def storeMatrix(filename,m1):
    mat1 = np.matrix(m1)
    with open(filename,'wb') as f:
        for line in mat1:
                np.savetxt(f, line.real, fmt='%f')
	

err=2

print "*******************"
print "*******************"
        
        
row=1800
col=3600
szcmpresscmd = '/home/luo/Tao/LossyCompressStudy/SZ/example/testfloat_compress sz.config Inputdata/FLUT_1_1800_3600.dat '+str(row)+" "+ str(col) 
szdecmp = '/home/luo/Tao/LossyCompressStudy/SZ/example/testfloat_decompress sz1.config Inputdata/FLUT_1_1800_3600.dat.sz '+str(row)+" "+ str(col)
#print szcmpresscmd
#print szdecmp 
os.system(szcmpresscmd)

os.system(szdecmp)

statinfo=os.stat("Inputdata/FLUT_1_1800_3600.dat")
fsize1=statinfo.st_size
statinfo=os.stat("Inputdata/FLUT_1_1800_3600.dat.sz")
fsize2=statinfo.st_size
print float(fsize1)/float(fsize2)


fin = open('Inputdata/FLUT_1_1800_3600.dat', 'rb')
vals_0= array.array('f', row*col*[0])

fin.readinto( vals_0)
fin.close()
vals_0=np.array(vals_0)
fin = open('Inputdata/FLUT_1_1800_3600.dat.sz.out', 'rb')
reconVals_sz = array.array('f', row*col*[0])

fin.readinto(reconVals_sz)
fin.close()
reconVals_sz=np.array(reconVals_sz)
RMSE_final_sz= np.sqrt(((reconVals_sz - vals_0) ** 2).mean())

print RMSE_final_sz

zfpcmpresscmd="/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp -s -a 2 -f -2 1800 3600 -i Inputdata/FLUT_1_1800_3600.dat -z Inputdata/FLUT_1_1800_3600.dat.zfp"
zfpdecmp="/home/luo/Tao/LossyCompressStudy/zfp/examples/zfp  -a 2 -f -2 1800 3600 -z Inputdata/FLUT_1_1800_3600.dat.zfp -o Inputdata/FLUT_1_1800_3600.dat.zfp.out"
os.system(zfpcmpresscmd)

os.system(zfpdecmp)

fin = open('Inputdata/FLUT_1_1800_3600.dat.zfp.out', 'rb')
reconVals_zfp = array.array('f', row*col*[0])

fin.readinto(reconVals_zfp)
fin.close()
reconVals_zfp=np.array(reconVals_zfp)
RMSE_final_zfp= np.sqrt(((reconVals_zfp - vals_0) ** 2).mean())

print RMSE_final_zfp
