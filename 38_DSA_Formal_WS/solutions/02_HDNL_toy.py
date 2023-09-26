"""
HDNL Toy

Steve found a new toy to play with. It's called HDNL
(High Definition Native Language). He doesn't know what it is used for,
he just finds it interesting. HDNL works by defining homeomorphic
endofunctors mapping submanifolds of a Hilbert space. Sadly,
when Steve is looking at HDNL, he isn't always able to imagine how
all it would look in the end. Each line of HDNL consists of a letter
and a number and opens a tag (like HTML tag). The letter is important,
though Steve can't remember why. The number defines the level of
nesting. Steve wants to see how he can nest all the tags such that the
level of nesting of inner tags is bigger than that of outer tags.
Your task is to write a program for Steve which shows nicely indented
and closed HDNL tags.
Input

    On the first line of input, a number N is read - the number of
    HDNL lines to follow
    Each of the next N lines will be a Latin letter glued to positive
    number

Output

    There should be N * 2 lines
    Each output line should contain either an opening or a
    closing tag
    Use 1 space for indentation

Constraints

    1 <= N <= 100 000
    1 <= level of nesting <= 1000

Sample tests
Input
4
h1
r5
d2
a0

Output
<h1>
 <r5>
 </r5>
 <d2>
 </d2>
</h1>
<a0>
</a0>

Input

9
a1
b2
c3
d3
e2
f3
g2
h1
i2

Output
<a1>
 <b2>
  <c3>
  </c3>
  <d3>
  </d3>
 </b2>
 <e2>
  <f3>
  </f3>
 </e2>
 <g2>
 </g2>
</a1>
<h1>
 <i2>
 </i2>
</h1>
"""

stack = []
indent = ' '

for _ in range(int(input())):
    next_line = input()
    letter = next_line[0]
    value = int(next_line[1:])
    if len(stack) > 0:
        if value > stack[-1][1]:  # stack.peek()
            print(f'{indent * len(stack)}<{next_line}>')

        else:
            while len(stack) > 0 and value <= stack[-1][1]:  # stack.peek()
                prev_letter, prev_value = stack.pop()
                print(f'{indent * len(stack)}</{prev_letter}{prev_value}>')
            print(f'{indent * len(stack)}<{next_line}>')

    else:
        print(f'<{next_line}>')
    stack.append((letter, value))  # stack.push()
while len(stack) > 0:
    letter, val = stack.pop()
    print(f'{indent * len(stack)}</{letter}{val}>')