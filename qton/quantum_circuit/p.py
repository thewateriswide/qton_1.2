# 
# This code is part of Qton.
# 
# File:   p.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def p(self, phi, targ):
    '''
    Phase operation.
    
    -In:
        phi --- phase angle.
            type: float
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    from numpy import exp

    A = exp(1j * phi)
    stride = 2**targ
    for i in range(stride, 2**self.num_qubits, 2**(targ + 1)):
        for j in range(i, i + stride):
            self.statevector[j] *= A
