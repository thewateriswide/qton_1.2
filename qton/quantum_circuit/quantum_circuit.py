# 
# This code is part of Qton.
# 
# File:   quantum_circuit.py
# Author: Yunheng Ma
# Date :  2022-01-19
#


import numpy as np


__all__ = ['Quantum_circuit']



class Quantum_circuit(object):
    '''
    Create quantum circuit object.

    Example:

        Create an instance:
            qc = Quantum_circuit(num_qubits)
            
        Invoke the number of qubits:
            qc.num_qubits
            
        Apply CX gate, qubit 0 controls qubit 1:
            qc.cx(0, 1)
        Qubits are indexed by integers start from 0.
        
        Invoke the instance's state:
            qc.statevector
            
        Take a measurement on on qubit 2:
            bit = qc.measure([2, 3])
        Which induces a random collapsing of state and retruns a bit value.

        Sample a state:
            counts = qc.sample()
        returns a dict like "{'00':510,'01':514}"
    '''
    num_qubits = 0
    statevector = np.array([1.], complex)


    from .i import i
    from .h import h
    from .x import x
    from .y import y
    from .z import z
    from .s import s
    from .sdg import sdg
    from .t import t
    from .tdg import tdg
    from .p import p
    from .u import u
    from .rx import rx
    from .ry import ry
    from .rz import rz
    from .u1 import u1
    from .u2 import u2
    from .u3 import u3

    from .swap import swap
    from .ch import ch
    from .cx import cx
    from .cy import cy
    from .cz import cz
    from .cs import cs
    from .ct import ct
    from .cp import cp
    from .cu import cu
    from .crx import crx
    from .cry import cry
    from .crz import crz
    from .cu1 import cu1
    from .cu2 import cu2
    from .cu3 import cu3


    def __init__(self, num_qubits=1):
        '''
        -In:
            num_qubits --- number of qubits.
                type: int
        
        -Influenced:
            self.num_qubits --- number of qubits.
                type: int
            self.statevector --- qubit state vector.
                type: numpy.ndarray, complex
        '''
        self.num_qubits = num_qubits
        self.statevector = np.zeros(2**num_qubits, complex)
        self.statevector[0] = 1.


    def _single_qubit_manipulatoin_(self, gate, targ):
        '''
        Apply a single-qubit gate on a given qubit.

        -In:
            gate --- single-qubit gate matrix.
                type: numpy.ndarray, complex
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
                self.statevector[j + stride] = np.matmul(gate, [
                    self.statevector[j],
                    self.statevector[j + stride]
                    ])


    def _double_qubit_manipulation_(self, gate, qubit1, qubit2):
        '''
        Apply a double-qubit gate on two given qubits.

        -In:
            gate --- double-qubit gate matrix.
                type: numpy.ndarray, complex
            qubit1 --- first qubit index.
                type: int
            qubit2 --- second qubit index.
                type: int

        -Influenced:
            self.statevector --- qubit state vector.
                type: numpy.ndarray, complex
        '''
        if qubit1 == qubit2:
            raise Exception('Cannot be same qubits.')

        if qubit1 > qubit2:
            q1, q2 = qubit1, qubit2
        else:
            q1, q2 = qubit2, qubit1

        L1, L2, L3 = 2**qubit2, 2**qubit1, 2**qubit2 + 2**qubit1

        for i in range(0, 2**self.num_qubits, 2**(q1 + 1)):
            for j in range(0, 2**q1, 2**(q2 + 1)):
                for k in range(0, 2**q2):
                    step = i + j + k
                    self.statevector[step], \
                    self.statevector[step + L1], \
                    self.statevector[step + L2], \
                    self.statevector[step + L3] = np.matmul(gate, [
                        self.statevector[step],
                        self.statevector[step + L1],
                        self.statevector[step + L2],
                        self.statevector[step + L3]
                        ])


    def _triple_qubit_manipulation_(self, gate, qubit1, qubit2, qubit3):
        '''
        Apply a triple-qubit gate on three given qubits.

        -In:
            gate --- triple-qubit gate matrix.
                type: numpy.ndarray
            qubit1 --- first qubit index.
                type: int
            qubit2 --- second qubit index.
                type: int
            qubit3 --- third qubit index.
                type: int

        -Influenced:
            self.statevector --- qubit state vector.
                type: numpy.ndarray, complex
        '''
        q = [qubit1, qubit2, qubit3]
        if len(set(q)) < 3:
            raise Exception('Cannot be same qubits.')

        L = np.zeros(2**3, int)
        for i in range(2**3):
            s = format(i, '03b')
            for j in range(3):
                L[i] += int(s[j]) * 2**q[j]

        q.sort(reverse=True)
        q1, q2, q3 = q

        for i in range(0, 2**self.num_qubits, 2**(q1 + 1)):
            for j in range(0, 2**q1, 2**(q2 + 1)):
                for k in range(0, 2**q2, 2**(q3 + 1)):
                    for l in range(0, 2**q3):
                        step = i + j + k + l
                        self.statevector[step + L[0]], \
                        self.statevector[step + L[1]], \
                        self.statevector[step + L[2]], \
                        self.statevector[step + L[3]], \
                        self.statevector[step + L[4]], \
                        self.statevector[step + L[5]], \
                        self.statevector[step + L[6]], \
                        self.statevector[step + L[7]] = np.matmul(gate, [
                            self.statevector[step + L[0]],
                            self.statevector[step + L[1]],
                            self.statevector[step + L[2]],
                            self.statevector[step + L[3]],
                            self.statevector[step + L[4]],
                            self.statevector[step + L[5]],
                            self.statevector[step + L[6]],
                            self.statevector[step + L[7]]
                            ])


    def measure(self, qubit):
        '''
        Projective measurement on a given qubit.

        For clarity, only one qubit will be measured.
        
        -In:
            qubit --- index of measured qubit.
                type: int

        -Influenced:
            self.svec --- qubit statevector.
                type: numpy.ndarray, 1D, complex
                
        -Return:
            bit --- final state of the given qubit, 0 or 1.
                type: int
        '''
        wgt = 2**qubit
        probability0 = 0.
        for i in range(2**self.num_qubits):
            if int(i/wgt)%2 == 0:
                probability0 += abs(self.statevector[i])**2

        if np.random.random() < probability0:
            bit = 0
            stride = 2**qubit
            for i in range(0, 2**self.num_qubits, 2**(qubit + 1)):
                for j in range(i, i + stride):
                    self.statevector[j + stride] = 0.
            self.statevector /= np.sqrt(probability0)
        else:
            bit = 1
            stride = 2**qubit
            for i in range(0, 2**self.num_qubits, 2**(qubit + 1)):
                for j in range(i, i + stride):
                    self.statevector[j] = 0.
            self.statevector /= np.sqrt(1 - probability0)
        return bit


    def sample(self, shots=1024):
        '''
        Sample a statevector, sampling with replacement.
        
        -In:
            shots --- sampling times.
                type: int
                
        -Return:
            --- samples.
                type: dict
        '''
        distribution = self.statevector * self.statevector.conj()

        from random import choices
        N = self.statevector.shape[0]
        memory = choices(range(N), weights=distribution, k=shots)

        counts = {}
        for i in memory:
            key = format(i, '0%db'%self.num_qubits)
            if key in counts:
                counts[key] += 1
            else:
                counts[key] = 1
        return counts