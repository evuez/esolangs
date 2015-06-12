"""
+ Increments the value at the current cell by one.
- Decrements the value at the current cell by one.
> Moves the data pointer to the next cell (cell on the right).
< Moves the data pointer to the previous cell (cell on the left).
. Prints the ASCII value at the current cell (i.e. 65 = 'A').
, Reads a single input character into the current cell.
[ If the value at the current cell is zero, skips to the corresponding ].
    Otherwise, move to the next instruction.
] If the value at the current cell is zero, move to the next instruction.
    Otherwise, move backwards in the instructions to the corresponding [.
"""


import logging


class CyclingInt(int):
    """
    Fill up cells with this instead of ints to have a wrapping implementation
    """

    def __add__(self, other):
        x = super().__add__(other)
        while x > 255:
            x -= 255
        return self.__class__(x)

    def __sub__(self, other):
        x = super().__sub__(other)
        while x < 0:
            x += 255
        return self.__class__(x)


class Brainfuck(object):
    """
    Non-wrapping interpreter
    """

    TOKENS = {
        '+': 'add',
        '-': 'sub',
        '>': 'move_f',
        '<': 'move_b',
        '[': 'skip_f',
        ']': 'skip_b',
        '.': 'disp',
        ',': 'read',
    }

    def __init__(self):
        self.c_pointer = 0 # cells pointer
        self.p_pointer = 0 # program pointer
        self.cells = [0] * 30000 # Non-wrapping
        # self.cells = [CyclingInt()] * 30000 # Wrapping
        self.bracestack = []

    @property
    def cell(self):
        return self.cells[self.c_pointer]
    @cell.setter
    def cell(self, value):
        self.cells[self.c_pointer] = value

    @property
    def token(self):
        return self.program[self.p_pointer]

    def execute(self, program):
        self.program = program
        while True:
            try:
                logging.debug("At %d: %s", self.p_pointer, self.token)
                getattr(self, self.TOKENS[self.token])()
            except KeyError:
                self.next()
            except IndexError:
                break

    def next(self):
        """
        Move to next token
        """
        self.p_pointer += 1
        try:
            return self.token
        except IndexError:
            pass

    def goto(self, pointer):
        """
        Goto token at pointer
        """
        self.p_pointer = pointer
        try:
            return self.token
        except IndexError:
            pass

    def add(self):
        """
        Increment current cell
        """
        self.cell += 1
        self.next()

    def sub(self):
        """
        Decrement current cell
        """
        self.cell -= 1
        self.next()

    def move_f(self):
        """
        Move forward
        """
        self.c_pointer += 1
        self.next()

    def move_b(self):
        """
        Move backward
        """
        self.c_pointer -= 1
        self.next()

    def skip_f(self):
        """
        Skip forward
        """
        self.bracestack.append(self.p_pointer)
        if self.cell:
            return self.next()
        self.goto(self.p_pointer + self.program[self.p_pointer:].find(']'))

    def skip_b(self):
        """
        Skip backward
        """
        brace = self.bracestack.pop()
        if not self.cell:
            return self.next()
        self.goto(brace)

    def disp(self):
        """
        Print current cell
        """
        print(chr(self.cell), end='')
        self.next()

    def read(self):
        """
        Read input into current cell
        """
        self.cell = int(input())
        self.next()


if __name__ == '__main__':
    Brainfuck().execute("""
        ++++++++++[>+++++++>++++++++++>+++>+<
        <<<-]>++.>+.+++++++..+++.>++.<<++++++
        +++++++++.>.+++.------.--------.>+.>.
    """)
