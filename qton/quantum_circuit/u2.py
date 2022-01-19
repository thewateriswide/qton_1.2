# 
# This code is part of Qton.
# 
# File:   u2.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def u2(self, phi, lamda, targ):
    '''
    U2 operation.
    
    -In:
        phi --- phase angle 1.
            type: float
        lamda --- phase angle 2.
            type: float
        targ --- target qubit index.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    from numpy import array, matmul, exp, sqrt

    gate = array([
        [1, -exp(1j * lamda)],
        [exp(1j * phi), exp(1j * lamda + 1j * phi)]
        ]) * sqrt(0.5)

    stride = 2**targ
    for i in range(0, 2**self.num_qubits, 2**(targ + 1)):
        for j in range(i, i + stride):
            self.statevector[j], \
            self.statevector[j + stride] = matmul(gate, [
                self.statevector[j], 
                self.statevector[j + stride]
                ])
