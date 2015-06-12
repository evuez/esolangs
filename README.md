# Esolangs
## Some [esoteric programming languages](https://esolangs.org/) interpreters written in Python

Basic languages rules are written in interpreters files.

### Brainfuck (non-wrapping)

```brainfuck.py``` includes a ```CyclingInt``` class that can be used to get a wrapping implementation.

```python
from brainfuck import Brainfuck


# prints "Hello World!"
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


# prints "Hello World!"
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


# prints "Hello World!"
Kipple().execute("""
    33>o 100>o 108>o 114>o 111>o 87>o 32>o 111>o 108>o 108>o 101>o 72>o
""")

# prints the first 25 numbers of the Fibonacci sequence
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
```

### DOGO

Nothing done yet.

### Byte Syze

Even less done.

### Meq

See Byte Syze.

### [DCPU-16](http://web.archive.org/web/20121001104346/http://0x10c.com/doc/dcpu-16.txt)

See Meq.

Not esoteric, but thought it would be fun to implement too.
