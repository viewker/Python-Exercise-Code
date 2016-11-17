import numpy as np
import matplotlib.pyplot as plt
Em = np.linspace(2,8,100)
d = 0.2
s = 0.5
c = 3e2

a_siw = []
f = 20
for i in Em:
    a = c/(2*f)
    ad = a/np.sqrt(i)
    a_siw.append(ad + d**2/(0.95*s))


plt.figure(1,figsize =(16,10))
line1 = plt.plot(Em,a_siw)
##plt.plot(Em,a_siw)
plt.title('Width of cutoff Freqency',fontsize = 30)
plt.xlabel('Em',fontsize = 24)
plt.ylabel('widht (mm)',fontsize = 24)
plt.setp(line1,color = 'red',linewidth = 3,label = 'line1',linestyle = '--')
plt.legend()
plt.show()

   
