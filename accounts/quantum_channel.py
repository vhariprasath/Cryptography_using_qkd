from .qubit import qubit
from .quantum import quantum_user
from accounts.sender import sender
from accounts.receiver import receiver
from accounts.eve import Eve


def QKD(N,s_idx,r_idx ,verbose = False,eve_present = False):
	
	alice_qubits = sender(N)
	if eve_present:
		alice_qubits = Eve(N,alice_qubits)
	status = receiver(N,alice_qubits,s_idx,r_idx)

	return status
