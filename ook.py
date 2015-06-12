"""
Ook. Ook?  Move the pointer to the right
Ook? Ook.  Move the pointer to the left
Ook. Ook.  Increment the memory cell under the pointer
Ook! Ook!  Decrement the memory cell under the pointer
Ook! Ook.  Output the character signified by the cell at the pointer
Ook. Ook!  Input a character and store it in the cell at the pointer
Ook! Ook?  Jump past the matching Ook? Ook! if the cell under the pointer is 0
Ook? Ook!  Jump back to the matching Ook! Ook?
"""


from re import sub
from brainfuck import Brainfuck


class Ook(Brainfuck):
    MAP = {
        'Ook.Ook.': '+',
        'Ook!Ook!': '-',
        'Ook.Ook?': '>',
        'Ook?Ook.': '<',
        'Ook!Ook?': '[',
        'Ook?Ook!': ']',
        'Ook!Ook.': '.',
        'Ook.Ook!': ',',
    }

    def execute(self, program):
        super().execute(self.to_brainfuck(program))

    def to_brainfuck(self, program):
        program = sub(r'[^Ook\.\?!]', '', program)
        return ''.join([
            self.MAP[program[i:i + 8].strip()]
            for i in range(0, len(program), 8)
        ])


if __name__ == '__main__':
    Ook().execute("""
        Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
        Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook? Ook. Ook. Ook. Ook. Ook.
        Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook?
        Ook! Ook! Ook? Ook! Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook. Ook. Ook.
        Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook? Ook.
        Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook! Ook! Ook? Ook!
        Ook? Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
        Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook. Ook. Ook. Ook. Ook.
        Ook. Ook. Ook! Ook. Ook. Ook? Ook. Ook? Ook. Ook? Ook. Ook. Ook. Ook.
        Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook?
        Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook! Ook!
        Ook? Ook! Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook? Ook. Ook? Ook. Ook.
        Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
        Ook. Ook. Ook. Ook. Ook! Ook? Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook.
        Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook?
        Ook! Ook! Ook? Ook! Ook? Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
        Ook? Ook. Ook? Ook. Ook? Ook. Ook? Ook. Ook! Ook. Ook. Ook. Ook. Ook.
        Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
        Ook! Ook! Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
        Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook? Ook. Ook? Ook. Ook.
        Ook! Ook.
    """)
