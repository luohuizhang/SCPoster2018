#!/usr/bin/python

from numpy import *
import matplotlib.pyplot as plt
import sys
import array
import os

if len(sys.argv) < 1 :
    print 'usage: python %s <file.dat' % sys.argv[0]
    sys.exit(0)

print sys.argv[1]




#print(__doc__)


def loadDataSet(fileName, delim='\t'):
    fr = open(fileName)
    stringArr = [line.strip().split() for line in fr.readlines()]
    print shape(stringArr)
   # print stringArr
    datArr = [map(float, line) for line in stringArr]
    return datArr
def storeMatrix(filename,m1):
    mat1 = matrix(m1)
    with open(filename,'wb') as f:
    	for line in mat1:
        	savetxt(f, line.real, fmt='%f')
        


def pca(dataMat, topNfeat=9999999):
    meanVals = mean(dataMat, axis=0)
    # print 'meanVals', meanVals
    meanRemoved = dataMat - meanVals
    # print 'meanRemoved=', meanRemoved
    covMat = cov(meanRemoved, rowvar=0)
    #storeMatrix('covMat',covMat)
    eigVals, eigVects = linalg.eig(mat(covMat))
   # eigVals, eigVects = linalg.eig(mat(covMat))

    # print 'eigVals=', eigVals
    # print 'eigVects=', eigVects
    eigValInd = argsort(eigVals)
    # print 'eigValInd1=', eigValInd

    eigValInd = eigValInd[:-(topNfeat+1):-1]
    # print 'eigValInd2=', eigValInd
    redEigVects = eigVects[:, eigValInd]
    # print 'redEigVects=', redEigVects.T
    # print "---", shape(meanRemoved), shape(redEigVects)
    lowDDataMat = dot(meanRemoved , redEigVects)
    reconMat =dot(lowDDataMat, redEigVects.T) + meanVals
    # print 'lowDDataMat=', lowDDataMat
    # print 'reconMat=', reconMat
    return lowDDataMat, mat(reconMat)


def replaceNanWithMean(filename):
    #datMat = loadDataSet('/home/luo//Luo/PCA/MachineLearning/input/13.PCA/secom.data', ' ')
    datMat = loadDataSet(filename, ' ')
    numFeat = shape(datMat)[1]
    for i in range(numFeat):
        meanVal = mean(datMat[nonzero(~isnan(datMat[:, i].A))[0], i])
        datMat[nonzero(isnan(datMat[:, i].A))[0],i] = meanVal
    return datMat


def show_picture(dataMat, reconMat):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(dataMat[:, 0].flatten().A[0], dataMat[:, 1].flatten().A[0], marker='^', s=90)
    ax.scatter(reconMat[:, 0].flatten().A[0], reconMat[:, 1].flatten().A[0], marker='o', s=50, c='red')
    plt.show()


def analyse_data(dataMat):
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat-meanVals
    covMat = cov(meanRemoved, rowvar=0)
    eigvals, eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigvals)

    topNfeat = 20
    eigValInd = eigValInd[:-(topNfeat+1):-1]
    cov_all_score = float(sum(eigvals))
    sum_cov_score = 0
    for i in range(0, len(eigValInd)):
        line_cov_score = float(eigvals[eigValInd[i]])
        sum_cov_score += line_cov_score
        print '%s, %s%%, %s%%' % (format(i+1, '2.0f'), format(line_cov_score/cov_all_score*100, '4.5f'), format(sum_cov_score/cov_all_score*100, '4.5f'))


if __name__ == "__main__":
   # dataMat = loadDataSet('/home/luo//Luo/PCA/MachineLearning/input/13.PCA/testSet.txt')
    filename=sys.argv[1]
    dataMat = loadDataSet(filename)
#print shape(dataMat)
    #lowDmat, reconMat = pca(dataMat, 1)
    #lowDmat, reconMat = pca(dataMat, 2)
    #print shape(lowDmat)
    #print lowDmat
    #print shape(reconMat)
    #delta=reconMat-dataMat
    #for row in delta :
    #	print row
    #show_picture(dataMat, reconMat)

    # dataMat = replaceNanWithMean(filename)
    #print shape(dataMat)
    #print dataMat
   # analyse_data(dataMat)i
    k=240
    lowDmat, reconMat = pca(dataMat, k)
    #show_picture(dataMat, reconMat)
   # analyse_data(dataMat)
   # m=shape(dataMat)[0]
   # n=shape(dataMat)[1]
   # print m,n
   # print "%f" % (float((m*n))/float((m*k)+(k*n)))
   # storeMatrix("reconMat.dat",reconMat)
   # reconMat= loadDataSet("reconMat.dat")
   # sum_temp=0
   # for i in range (m):
#	for j in range (n):
	#	print reconMat[i][j]
                #float(pic_recon[i][j])
                #float(new[i][j])
#		sum_temp+=(float(dataMat[i][j])-float(reconMat[i][j]))**2

 #   print (sum_temp/n)**0.5
   #print rmse
    #for row in delta :
    #	print row

