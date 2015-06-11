# Esolangs
## Some [esoteric programming languages](https://esolangs.org/) interpreters written in Python

Languages rules are written in interpreters files.

The following examples should print "Hello World!".

### Brainfuck

```python
from brainfuck import Brainfuck

Brainfuck().execute("""
	++++++++++[>+++++++>++++++++++>+++>+<
	<<<-]>++.>+.+++++++..+++.>++.<<++++++
	+++++++++.>.+++.------.--------.>+.>.
""")
```
