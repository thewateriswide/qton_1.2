# 
# This code is part of Qton.
# 
# File:   rx.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def rx(self, theta, targ):
    '''
    Rotation along X axis.
    
    -In:
        theta --- rotation angle.
            type: float
        targ --- target qubit index.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    from numpy import array, matmul, cos, sin

    t = theta * 0.5
    gate = array([[cos(t), -1j * sin(t)], [-1j * sin(t), cos(t)]])

    stride = 2**targ
    for i in range(0, 2**self.num_qubits, 2**(targ + 1)):
        for j in range(i, i + stride):
            self.statevector[j], \
            self.statevector[j + stride] = matmul(gate, [
                self.statevector[j], 
                self.statevector[j + stride]
                ])
