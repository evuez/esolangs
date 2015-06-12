# Esolangs
## Some [esoteric programming languages](https://esolangs.org/) interpreters written in Python

Basic languages rules are written in interpreters files.

### Brainfuck (non-wrapping)

```brainfuck.py``` includes a ```CyclingInt``` class that can be used to get a wrapping implementation.

```python
from brainfuck import Brainfuck


# print "Hello World!"
Brainfuck().execute("""
    ++++++++++[>+++++++>++++++++++>+++>+<
    <<<-]>++.>+.+++++++..+++.>++.<<++++++
    +++++++++.>.+++.------.--------.>+.>.
""")
```

### Ook! (non-wrapping)
Brainfuck. With "Ook"s.

```python
from ook import Ook


# print "Hello World!"
Ook().execute("""
    Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
    Ook. Ook. Ook. Ook. Ook! Ook? Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
    Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook! Ook! Ook? Ook! Ook? Ook.
    Ook! Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
    Ook. Ook. Ook! Ook? Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook?
    Ook! Ook! Ook? Ook! Ook? Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook.
    Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook! Ook. Ook. Ook. Ook. Ook.
    Ook. Ook. Ook! Ook. Ook. Ook? Ook. Ook? Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook.
    Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook? Ook. Ook. Ook.
    Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook! Ook! Ook? Ook! Ook? Ook. Ook! Ook.
    Ook. Ook? Ook. Ook? Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
    Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook? Ook. Ook. Ook.
    Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook.
    Ook. Ook? Ook! Ook! Ook? Ook! Ook? Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
    Ook? Ook. Ook? Ook. Ook? Ook. Ook? Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook.
    Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook.
    Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook!
    Ook! Ook. Ook. Ook? Ook. Ook? Ook. Ook. Ook! Ook.
""")
```

### Smallfuck
Reduced Brainfuck operating on bits. Since there is no print operator, the execution won't print anything.

```python
from smallfuck import Smallfuck


sfi = Smallfuck()
sfi.execute("""
    *>*>*[>*<*]*>*>
""")
print(sfi.cells)
```


### Kipple (based on the [3rd version of the spec](http://web.archive.org/web/20070224040559/http://rune.krokodille.com/lang/kipple/kipple.html))

Not fully implemented yet, input is missing. You can fill ```Kipple().stacks['i']``` before execution to use it later in the program.

```python
from kipple import Kipple


# print "Hello World!"
Kipple().execute("""
    33>o 100>o 108>o 114>o 111>o 87>o 32>o 111>o 108>o 108>o 101>o 72>o
""")
```

### DOGO

Nothing done yet.

### Byte Syze

Even less done.

### Meq

See Byte Syze.
