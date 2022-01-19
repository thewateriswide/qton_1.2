# 
# This code is part of Qton.
# 
# File:   u.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def u(self, theta, phi, lamda, targ):
    '''
    U operation.
    
    -In:
        theta --- amplitude angle.
            type: float
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
    from numpy import array, matmul, exp, cos, sin

    t = theta * 0.5
    gate = array([
        [cos(t), -exp(1j * lamda) * sin(t)],
        [exp(1j * phi) * sin(t), \
            exp(1j * lamda + 1j * phi) * cos(t)]
        ])

    stride = 2**targ
    for i in range(0, 2**self.num_qubits, 2**(targ + 1)):
        for j in range(i, i + stride):
            self.statevector[j], \
            self.statevector[j + stride] = matmul(gate, [
                self.statevector[j],
                self.statevector[j + stride]
                ])
