"""
* Flip the bit in the current cell.
> Moves the data pointer to the next cell (cell on the right).
< Moves the data pointer to the previous cell (cell on the left).
[ If the value at the current cell is zero, skips to the corresponding ].
    Otherwise, move to the next instruction.
] If the value at the current cell is zero, move to the next instruction.
    Otherwise, move backwards in the instructions to the corresponding [.
"""


from brainfuck import Brainfuck


class Smallfuck(Brainfuck):
    TOKENS = {
        '*': 'flip',
        '>': 'move_f',
        '<': 'move_b',
        '[': 'skip_f',
        ']': 'skip_b',
    }

    def __init__(self):
        super().__init__()
        self.cells = [False] * 30000

    def flip(self):
        """
        Flip current bit
        """
        self.cell = not self.cell
        self.next()


if __name__ == '__main__':
    sfi = Smallfuck()
    sfi.execute("""
        *>*>*[>*<*]*>*>
    """)
    print(sfi.cells)
