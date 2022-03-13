import cirq

def bell_state(qubit1, qubit2):
    yield cirq.H(qubit1)
    yield cirq.CNOT(qubit1, qubit2)
