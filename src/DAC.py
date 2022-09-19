from cProfile import label
from operator import ne
from turtle import color
import numpy as np

class DAC():
    def __init__(self, t, a, Tsenal, N, SPAN=5, Tsample=1e-2):
        self.t = t
        self.a = a
        self.Tsenal = Tsenal
        self.Tsample = Tsample
        self.N = N
        self.SPAN = SPAN
        self.q = SPAN/(2**N)
        self.act = self.check_data()
        
    def check_data(self):
        for u in a:
            if u < 0:
                print("data below minimum")
                new_a = self.a + SPAN/2
                break
            else:
                new_a = self.a
            
        return new_a

    def sampler(self):
        num_samples = int(self.Tsenal/self.Tsample/5)
        print("num_samples=",num_samples)
        a_samp = self.act[0::num_samples]
        print(len(self.act))
        print(len(a_samp))

        t_samp = self.t[0::num_samples]

        return t_samp, a_samp


    def DAC_code(self):
        t, signal = self.sampler()
        bin = []
        for i in signal:
            for j in range(2**N+1):
                if i <= (j+1)*self.q:
                    if j > 2**N:
                        bin.append(hex(2**N))
                    else:
                        bin.append(hex(j))
                    break

        return bin
    
    def plot(self):
        import matplotlib.pyplot as plt
        t_s, a_s = self.sampler()
        t_dac=[]
        a_dac=[]
        for i in t_s:
            t_dac.append(i)
            t_dac.append(i)
        
        for j in a_s:
            a_dac.append(j)
            a_dac.append(j)

        t_dac=t_dac[1:]
        a_dac=a_dac[:-1]

        fig, ax= plt.subplots(4,1)
        ax[0].plot(self.t, self.a, label="Input")
        ax[1].plot(t_s, a_s, color="orange", label="Sampled")
        ax[2].plot(t_dac, a_dac, label="DAC")
        ax[3].plot(self.t, self.a, label="Input")
        ax[3].plot(t_s, a_s, label="Sampled")
        ax[3].plot(t_dac, a_dac, label="DAC")
        ax[0].legend(loc="upper right")
        ax[1].legend(loc="upper right")
        ax[2].legend(loc="upper right")
        ax[3].legend(loc= "upper right")
        plt.show()
    

if __name__=="__main__":
    Tsamp = 1e-3    #1ms
    nCyl = 5
    T_senal = 5
    t = np.arange(0, nCyl, Tsamp)
    a = np.sin(2*np.pi*t) + 1
    
    N = 8 
    SPAN = 2 

    dac = DAC(t, a, T_senal, N, SPAN, 0.004)    #4 ms

    print(dac.DAC_code())
    dac.plot()
    