


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
    return datArr

if __name__ == "__main__":

    filename=sys.argv[1]
    dataMat = loadDataSet(filename)
   # print(np.count_nonzero(dataMat))
   # print coeffs
    coeffs = pywt.dwt2(dataMat, 'haar')
    coeffs = pywt.dwt2(dataMat, 'haar')
    cA, (cH, cV, cD) = coeffs
    coeffsMat=np.row_stack((np.column_stack((cA,cH)),np.column_stack((cV,cD))))
    print(np.count_nonzero(coeffsMat))
    #coeffs_t=coeffs
    #np.where(coeffs_t > 0, coeffs_t, 0)
    #print coeffs_t
    coeffs_td=[]
    for ii in coeffs:
	a=pywt.threshold(ii, 372, 'hard')
        coeffs_td.append(a)
    cA1, (cH1, cV1, cD1) = coeffs_td
    coeffsMat_td=np.row_stack((np.column_stack((cA1,cH1)),np.column_stack((cV1,cD1))))
    #print coeffs_td
    reconMat=pywt.idwt2(coeffs_td, 'haar')
    m=np.shape(dataMat)[0]
    n=np.shape(dataMat)[1]
    print m,n
    sum_temp=0
    print  float(m*n)/float (np.count_nonzero(coeffsMat_td))
     
    for i in range (m):
        for j in range (n):
                #print reconMat[i][j]
                #float(pic_recon[i][j])
                #float(new[i][j])
                sum_temp+=(float(dataMat[i][j])-float(reconMat[i][j]))**2
    rmse=(sum_temp/n)**0.5

    print(rmse)
