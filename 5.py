import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(1,8,100)
F_c = np.array([])

Em = [2.2,3.66,4.4]
d = 0.2
s = 0.5
c = 3e2

l_index = 0
for a in Em:
    r_index = 0
    for i in w:
        
        W_d = i - d**2/(0.95*s)
        w_eff = W_d * np.sqrt(a)
        F_c[l_index,r_index] = c/(2*w_eff)
        r_index += 1
    l_index += 1

plt.figure(1,figsize =(16,10),dpi = 100)
plt.plot(W,F_cutoff1,'r--',linewidth = 3,label = r'Em = 2.2')
plt.plot(W,F_cutoff2,'b+',linewidth = 3,label = r'Em = 3.66')
plt.title('Frequency Cutoff',fontsize = 30,family = 'Times New Roman',fontweight = 'bold')
plt.xlabel('Width Of SIW (mm)',fontsize = 24,family = 'Times New Roman')
plt.ylabel('Frequency (GHz)',fontsize = 24,family = 'Times New Roman')
plt.legend()
plt.grid(True)
plt.show()

