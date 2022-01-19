# 
# This code is part of Qton.
# 
# File:   rz.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def rz(self, theta, targ):
    '''
    Rotation along Z axis.
    
    -In:
        theta --- rotation angle.
            type: float
        targ --- target qubit index.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    from numpy import exp

    t = theta * 0.5
    A = exp(-1j * t)
    B = exp(1j * t)

    stride = 2**targ
    for i in range(0, 2**self.num_qubits, 2**(targ + 1)):
        for j in range(i, i + stride):
            self.statevector[j], \
            self.statevector[j + stride] = \
                A * self.statevector[j], \
                B * self.statevector[j + stride]
