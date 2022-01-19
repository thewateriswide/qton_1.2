# 
# This code is part of Qton.
# 
# File:   swap.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def swap(self, qubit1, qubit2):
    '''
    Swap operation.
    
    If two input qubits are same, does nothing.

    -In:
        qubit1 --- first qubit index.
            type: int
        qubit2 --- second qubit index.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    if qubit1 == qubit2:
        return None

    if qubit1 > qubit2:
        q1, q2 = qubit1, qubit2
    else:
        q1, q2 = qubit2, qubit1

    stride1 = 2**q1
    stride2 = 2**q2
    for i in range(stride2, 2**self.num_qubits, 2**(q1 + 1)):
        for j in range(i, i + stride1, 2**(q2 + 1)):
            for k in range(j, j + stride2):
                self.statevector[k], \
                self.statevector[k + stride1 - stride2] = \
                    self.statevector[k + stride1 - stride2], \
                    self.statevector[k]
