from __future__ import division
import sys
import array
import os
import numpy as np
import pywt

def storeMatrix(filename,m1):
    mat1 = np.matrix(m1)
    with open(filename,'wb') as f:
    	for line in mat1:
                np.savetxt(f, line.real, fmt='%f')



statinfo=os.stat("Inputdata/FLUT_1_1800_3600.dat")
fsize=statinfo.st_size
print fsize
fin = open("Inputdata/FLUT_1_1800_3600.dat", 'rb')
#vals = array.array('d',(int(fsize/8))*[0])
vals = array.array('f',(int(fsize/4))*[0])
fin.readinto(vals)
fin.close()
        #print vals
	#len_x=int(np.sqrt(len(vals)))
        #print len_x
        #vals_sub=vals[0:len_x*len_x]
        #A=np.reshape(vals_sub,(len_x,len_x))
	#storeMatrix("newdata/"+filename+".dat",vals)
	#print np.shape(vals)
new=np.reshape(vals,(-1,3600))
print np.shape(new)
	#print new



u, sigma, v = np.linalg.svd(new)
m,n=new.shape

#print U
#print sigma
#print V
#print type(V)

#we vary the rank with the loop i
#for i in range(1600,1610,10):
i=230
#pic_ren = U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
#	cr=(m*n)/((m*i)+(i*i)+(i*n))
uk = u[:,:i]
    #storeMatrix("uk.txt",uk)
sigma_k=np.diag(sigma[:i])
vk = v[:i,:]
dot1 = np.dot(uk, sigma_k)
pic_recon= np.dot(dot1,vk)

    #storeMatrix("vk.txt",vk)
print "compression ratio for %d" %i
print "%f" % (float((m*n))/float((m*i)+(i*i)+(i*n))) 
	#plt.imshow(pic_recon, cmap='gray')
	#title = "n = %s" % i
	#plt.title(title)
	#plt.show()
print np.shape(pic_recon)
sum_temp=0
n=1800*3600
for i in range (1800):
	for j in range (3600):
		#print new[i][j]                
		#print pic_recon[i][j]
                #float(pic_recon[i][j])
                #float(new[i][j])
		sum_temp+=(float(pic_recon[i][j])-float(new[i][j]))**2

rmse=(sum_temp/n)**0.5

print(rmse)
   






