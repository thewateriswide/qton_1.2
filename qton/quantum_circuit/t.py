# 
# This code is part of Qton.
# 
# File:   t.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def t(self, targ):
    '''
    T operation.

    -In:
        targ --- target qubit index.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    A = (1 + 1j) * pow(0.5, 0.5)
    stride = 2**targ
    for i in range(stride, 2**self.num_qubits, 2**(targ + 1)):
        for j in range(i, i + stride):
            self.statevector[j] *= A
