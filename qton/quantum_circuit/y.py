# 
# This code is part of Qton.
# 
# File:   y.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def y(self, targ):
    '''
    Pauli-Y operation.

    -In:
        targ --- target qubit index.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    stride = 2**targ
    for i in range(0, 2**self.num_qubits, 2**(targ + 1)):
        for j in range(i, i + stride):
            self.statevector[j], \
            self.statevector[j + stride] = \
                -1j * self.statevector[j + stride], \
                1j * self.statevector[j]
