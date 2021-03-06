import numpy as np

class fir:
    def __init__(self, width = 0):
        self.width = width
        self._idx = 0
        self._i = 0
        self._prior = np.zeros([self.width],dtype=np.float64)

#FIR simple moving average application
    def apply_sma(self, x):
        self._i+=1
        self._prior = np.insert(self._prior, int(self._idx), x)
        self._prior = np.delete(self._prior, self.width)
        self._idx+=1
        if(self._idx >= self.width):
            self._idx = 0
        s = sum(self._prior)
        return (s/ min(self._i,self.width))

    def freq_resp(self, f):
        if f != 0:
            out = np.sin(np.pi * f * self.width)/(self.width * np.sin(np.pi * f))
            return out
        else:
            return 1
