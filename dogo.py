"""
Operators

SIT       If the value of the current memory cell is 0, jump to STAY.
STAY      If the value of the current memory cell is not 0, jump to SIT.
ROLL-OVER Select the next operation in the operation list.
HEEL      Execute the currently selected operation.

Operations

0: increment current memory cell
1: decrement current memory cell
2: move to the next memory cell
3: move to the previous memory cell
4: input a byte and store it in the current memory cell
5: output the current memory cell as ASCII
"""


from brainfuck import Brainfuck


class DOGO(Brainfuck):
	OPERATORS = {
		'SIT': '[',
		'STAY': ']',
		'ROLL-OVER': '',
		'HEEL': '',
	}
	OPERATIONS = {
		'0': '+',
		'1': '-',
		'2': '>',
		'3': '<',
		'4': ',',
		'5': '.',
	}
