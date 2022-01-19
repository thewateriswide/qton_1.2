# Qton

**Qton** is slight, written in Python. By **Qton** you can test quantum algorithms, learn how quantum simulators work. 

You are encouraged to reuse code or idea of **Qton** to build your own project.



## Version

Current version = `1.2.0`

_This version is for special purpose._

Compare to `Qton 1.1.0`:

- qubit index starts from the **rightmost** in a basis

- quantum gate matrices are removed
- 3-qubit gate methods are removed
- the **initialize** method is removed
- the **\_inner_swap\_**  method is removed
- kernel methods have been rewritten
- redefined the **measure** method, which behaves differently
- added the **sample** method
- others



## Install

Place the `qton` folder in your working directory, then import it as 

```python
from qton import *
```

which is same as

```python
from qton import Quantum_circuit
```



## Requirement

**Qton** is based on _NumPy_.

Almost every array-like object is realized by _numpy.ndarray_ type and operated by related NumPy functions.

This could help to fix most type errors you encounter.



## Example

Let's see how to make a 3-bit GHZ state ![1](http://latex.codecogs.com/svg.latex?\frac{|000\rangle + |111\rangle}{\sqrt 2}).

```python
from qton import Quantum_circuit

# initialize a circuit with 3 qubits.
# always starts from |000> state.
qc = Quantum_circuit(3)

# show the number of qubits in this circuit
print(qc.num_qubits)
```
```
3
```

Apply gates on qubits.

```python
# apply Hadamard gate on qubit 0
qc.h(0)

# apply CX gate, quibt 0 controls qubit 1
qc.cx(0, 1)

# apply CX gate, quibt 1 controls qubit 2
qc.cx(1, 2)

# this circuit is in GHZ state now
# show the statevector
print(qc.statevector)
```
```
[0.70710678+0.j 0.        +0.j 0.        +0.j 0.        +0.j
 0.        +0.j 0.        +0.j 0.        +0.j 0.70710678+0.j]
```

For most cases, getting this vector is enough for your research.

The vector basis for each component are

![2](http://latex.codecogs.com/svg.latex?|000\rangle, |001\rangle, |010\rangle, |011\rangle, |100\rangle, |101\rangle, |110\rangle, |111\rangle)

The qubit index in a basis starts to count from rightmost to leftmost, as

![](http://latex.codecogs.com/svg.latex?|q_2q_1q_0\rangle)


---

A measurement on a qubit will result a random collapsing of the vector and return the final state of this qubit.

```python
# take a measurement on qubit 0
bit = qc.measure(0)

# print the final state of qubit 0
print(bit)
```
```
1
```

You can check that the state vector has changed accordingly. 

```python
# show the statevector
print(qc.statevector)
```
```
[0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 0.+0.j 1.+0.j]
```

To be concise, you can only measure one qubit each time. To measure all qubits you can do

```python
bit = []
for i in range(3):
	bit.append(qc.measure(i))
```



---

Repeating above process to build a statistical sampling is not necessary. Instead, there is a much easy way.

```python
# build a sampling according to the state vector
sample = qc.sample(1024)

# show the counts for each basis
print(sample)
```
```
{'111': 1024}
```



## Gate

For convenience, all gate methods in this version of **Qton** are listed below, with instances.

 ```python
q0, q1 = 0, 1
pi = 3.14
angle1, angle2, angle3, angle4 = pi, pi/2, pi/4, pi/8

qc.i(q0)
qc.h(q0)
qc.x(q0)
qc.y(q0)
qc.z(q0)
qc.s(q0)
qc.t(q0)
qc.sdg(q0)
qc.tdg(q0)

qc.rx(angle1, q0)
qc.ry(angle1, q0)
qc.rz(angle1, q0)
qc.p(angle1, q0)
qc.u1(angle1, q0)
qc.u2(angle1, angle2, q0)
qc.u3(angle3, angle2, angle3, q0)
qc.u(angle1, angle2, angle3, q0)

qc.swap(q0, q1)
qc.ch(q0, q1)
qc.cx(q0, q1)
qc.cy(q0, q1)
qc.cz(q0, q1)
qc.cs(q0, q1)
qc.ct(q0, q1)

qc.crx(angle1, q0, q1)
qc.cry(angle1, q0, q1)
qc.crz(angle1, q0, q1)
qc.cp(angle1, q0, q1)
qc.cu1(angle1, q0, q1)
qc.cu2(angle1, angle2, q0, q1)
qc.cu3(angle3, angle2, angle3, q0, q1)
qc.cu(angle1, angle2, angle3, angle4, q0, q1)
 ```

The information of each gate can be easily found in the source code.

