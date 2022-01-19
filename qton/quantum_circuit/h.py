# 
# This code is part of Qton.
# 
# File:   h.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def h(self, targ):
    '''
    Hadamard operation.

    -In:
        targ --- target qubit index.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    from numpy import array, sqrt, matmul

    gate = sqrt(0.5) * array([[1.0, 1.0], [1.0, -1.0]], complex)
    stride = 2**targ
    for i in range(0, 2**self.num_qubits, 2**(targ + 1)):
        for j in range(i, i + stride):
            self.statevector[j], \
            self.statevector[j + stride] = matmul(gate, [
                self.statevector[j], 
                self.statevector[j + stride]
                ])
