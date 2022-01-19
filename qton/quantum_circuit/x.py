# 
# This code is part of Qton.
# 
# File:   x.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def x(self, targ):
    '''
    Pauli-X operation.

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
                self.statevector[j + stride], \
                self.statevector[j]
