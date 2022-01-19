# 
# This code is part of Qton.
# 
# File:   u1.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def u1(self, lamda, targ):
    '''
    U1 operation.
    
    -In:
        lamda --- phase angle.
            type: float
        targ --- target qubit index.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    from numpy import exp

    A = exp(1j * lamda)
    stride = 2**targ
    for i in range(stride, 2**self.num_qubits, 2**(targ + 1)):
        for j in range(i, i + stride):
            self.statevector[j] *= A
