"""
> Push left operand onto right stack
< Push right operand onto left stack
+ Push the sum of the right operand and the topmost
    item of the left stack onto the left stack
- Push the topmost left stack item minus the right operand onto the stack
? Takes only one operand; clears the left stack if its topmost item is 0

Input is not implemented yet.
"""


class Stack(list):

    class OnlyInputError(Exception):
        pass

    def __init__(self, name, iterable=[]):
        super().__init__(iterable)
        self.name = name

    def pop(self, index=-1):
        try:
            return super().pop(index)
        except IndexError:
            return 0

    def push(self, value):
        if not isinstance(value, int):
            raise TypeError
        if self.name == 'i':
            raise Stack.OnlyInputError()
        if self.name != '@':
            return self.append(value)
        [self.append(ord(v)) for v in str(value)]


class Kipple(object):
    STACKS_IDENTIFIERS = 'abcdefghijklmnopqrstuvwxyz@'
    OPERATORS = {
        '>': 'push_ltr',
        '<': 'push_rtl',
        '+': 'sum',
        '-': 'sub',
        '?': 'clear',
        '(': 'loop_start',
        ')': 'loop_end',
    }

    def __init__(self):
        self.stacks = {s:Stack(s) for s in self.STACKS_IDENTIFIERS}
        self.pointer = 0
        self.loopstack = []

    def execute(self, program):
        self.program = ' '.join(program.split())
        while True:
            try:
                getattr(self, self.OPERATORS[self.next_operator()])()
            except KeyError:
                break
        self.output()

    def last(self, stack):
        try:
            return self.stacks[stack][-1]
        except IndexError:
            return 0

    def pop(self, stack):
        return self.stacks[stack].pop()

    def push(self, stack, value):
        self.stacks[stack].push(value)

    def goto(self, pointer):
        self.pointer = pointer

    def get_value(self, from_right=False):
        """
        Get value next to pointer.
        Get value from the left if `from_right` is False,
        from the right otherwise.
        """
        step = 1 if from_right else -1
        values = [self.program[self.pointer + step]]
        try:
            values = [int(values[0])]
            for v in self.program[self.pointer + step * 2::step]:
                try:
                    values.append(int(v))
                except ValueError:
                    break
            return int(''.join([str(v) for v in values[::step]]))
        except ValueError:
            return self.pop(values[0])

    def get_stack(self, from_left=False):
        """
        Get stack next to pointer.
        Get stack from the right if `from_left` is False,
        from the left otherwise.
        """
        step = -1 if from_left else 1
        stack = self.program[self.pointer + step]
        if stack in self.stacks:
            return stack
        raise IndexError

    def push_ltr(self):
        """
        Push left operand onto right stack
        """
        self.push(self.get_stack(), self.get_value())

    def push_rtl(self):
        """
        Push right operand onto left stack
        """
        self.push(self.get_stack(True), self.get_value(True))

    def sum(self):
        """
        Push the sum of the right operand and the
        topmost item of the left stack onto the left stack
        """
        stack = self.get_stack(True)
        self.push(stack, self.last(stack) + self.get_value(True))

    def sub(self):
        """
        Push the topmost left stack item minus the
        right operand onto the stack
        """
        stack = self.get_stack(True)
        self.push(stack, self.last(stack) - self.get_value(True))

    def clear(self):
        """
        Takes only one operand; clears the left
        stack if its topmost item is 0
        """
        stack = self.get_stack(True)
        if not self.last(stack):
            self.stacks[stack].clear()

    def loop_start(self):
        self.loopstack.append((self.pointer, self.get_stack()))

    def loop_end(self):
        loop = self.loopstack[-1]
        if self.last(loop[1]):
            self.goto(loop[0] + 1)
        else:
            self.loopstack.pop()

    def output(self):
        print(''.join(chr(v) for v in self.stacks['o'][::-1]))

    def next_operator(self):
        if self.program[self.pointer] in self.OPERATORS:
            self.pointer += 1
        for token in self.program[self.pointer:]:
            if token in self.OPERATORS:
                return token
            self.pointer += 1


if __name__ == '__main__':
    Kipple().execute("""
        33>o 100>o 108>o 114>o 111>o 87>o 32>o 111>o 108>o 108>o 101>o 72>o
    """)
    Kipple().execute("""
        24>n 0>t 1>a
        (n-1
          a+0
          t<a>b+a
          c<b>a<c
          n?
        )
        (t>@
          (@>o)
          32>o
        )
    """)
