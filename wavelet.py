# coding: utf-8



import sys
import array
import os



import pywt
import matplotlib.pyplot as plt
import numpy as np


def storeMatrix(filename,m1):
    mat1 = np.matrix(m1)
    with open(filename,'wb') as f:
        for line in mat1:
                np.savetxt(f, line.real, fmt='%f')

def analyse_data(Sigma, loopNum=20):

    Sig2 = Sigma**2
    SigmaSum = sum(Sig2)
    for i in range(loopNum):
        SigmaI = sum(Sig2[:i+1])
        print 'primary: %s, accumulate: %s%%' % (format(i+1, '2.0f'), format(SigmaI/SigmaSum*100, '4.2f'))



def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split() for line in fr.readlines()]
    print np.shape(stringArr)
   # print stringArr
    datArr = [map(float, line) for line in stringArr]
    return np.mat(datArr)

if __name__ == "__main__":

    filename=sys.argv[1]
    dataMat = loadDataSet(filename)
   # print(np.count_nonzero(dataMat))
   # print coeffs
    coeffs = pywt.dwt2(dataMat, 'haar')
    coeffs = pywt.dwt2(dataMat, 'haar')
    cA, (cH, cV, cD) = coeffs
    coeffsMat=np.row_stack((np.column_stack((cA,cH)),np.column_stack((cV,cD))))
    storeMatrix("coeffsMat.txt",coeffsMat)   
    print(np.count_nonzero(coeffsMat))
    #coeffs_t=coeffs
    #np.where(coeffs_t > 0, coeffs_t, 0)
    #print coeffs_t
    coeffs_td=[]
    for ii in coeffs:
	a=pywt.threshold(ii, 0.01, 'hard')
        coeffs_td.append(a)
    cA1, (cH1, cV1, cD1) = coeffs_td
    coeffsMat_td=np.row_stack((np.column_stack((cA1,cH1)),np.column_stack((cV1,cD1))))
    storeMatrix("coeffsMat_td.txt",coeffsMat_td)
    print(np.count_nonzero(coeffsMat_td))
    print np.shape(coeffsMat_td) 
    #print coeffs_td
    recdata=pywt.idwt2(coeffs_td, 'haar')
    recdata=pywt.idwt2(coeffs_td, 'haar')
    recdata1=recdata[0:np.shape(dataMat)[0],0:np.shape(dataMat)[1]]   
    storeMatrix("recdata.txt",recdata1) 
    delta=recdata1-dataMat
    delta=recdata1-dataMat
    storeMatrix("delta.txt",delta)
