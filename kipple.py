"""
> Push left operand onto right stack
< Push right operand onto left stack
+ Push the sum of the right operand and the topmost
    item of the left stack onto the left stack
- Push the topmost left stack item minus the right operand onto the stack
? Takes only one operand; clears the left stack if its topmost item is 0

Control structure and input are not implemented yet.
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
        if self.name == '@':
            value = chr(value)
        if self.name == 'i':
            raise Stack.OnlyInputError()
        self.append(value)


class Kipple(object):
    STACKS_IDENTIFIERS = 'abcdefghijklmnopqrstuvwxyz@'
    OPERATORS = {
        '>': 'push_ltr',
        '<': 'push_rtl',
        '+': 'sum',
        '-': 'sub',
        '?': 'clear',
    }

    def __init__(self):
        self.stacks = {s:Stack(s) for s in self.STACKS_IDENTIFIERS}
        self.pointer = 0

    def execute(self, program):
        self.program = ' '.join(program.split())
        while True:
            try:
                getattr(self, self.OPERATORS[self.next_operator()])()
            except KeyError:
                break
        self.output()

    def last(self, stack):
        return self.stacks[stack][-1]

    def pop(self, stack):
        return self.satcks[stack].pop()

    def push(self, stack, value):
        self.stacks[stack].push(value)

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
        self.push(stack, self.last(stack) + get_value(True))

    def sub(self):
        """
        Push the topmost left stack item minus the
        right operand onto the stack
        """
        stack = self.get_stack(True)
        self.push(stack, self.last(stack) - get_value(True))

    def clear(self):
        """
        Takes only one operand; clears the left
        stack if its topmost item is 0
        """
        stack = self.get_stack(True)
        if not self.last(stack):
            self.stacks[stack].clear()

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
