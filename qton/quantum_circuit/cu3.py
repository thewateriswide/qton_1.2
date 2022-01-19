# 
# This code is part of Qton.
# 
# File:   cu3.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


def cu3(self, theta, phi, lamda, ctrl, targ):
    '''
    Controlled U3 operation.

    -In:
        theta --- amplitude angle.
            type: float
        phi --- phase angle 1.
            type: float
        lamda --- phase angle 2.
            type: float
        ctrl --- control qubit index.
            type: int
        targ --- target qubit index.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    if ctrl == targ:
        raise Exception('Control and target cannot be the same.')

    if ctrl > targ:
        q1, q2 = ctrl, targ
    else:
        q1, q2 = targ, ctrl

    from numpy import array, matmul, exp, cos, sin

    t = theta * 0.5
    gate = array(
        [[cos(t), -exp(1j * lamda) * sin(t)],
         [exp(1j * phi) * sin(t),
          exp(1j * lamda + 1j * phi) * cos(t)]])

    stride = 2**targ
    for i in range(2**ctrl, 2**self.num_qubits, 2**(q1 + 1)):
        for j in range(i, i + 2**q1, 2**(q2 + 1)):
            for k in range(j, j + 2**q2):
                self.statevector[k], \
                self.statevector[k + stride] = matmul(gate, [
                    self.statevector[k],
                    self.statevector[k + stride]
                    ])
