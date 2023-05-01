# 난수 생성

from random import *

# random - 0 <= x < 10

print(int((random() * 10)))

# random - 1 <= x <= 10

print(int((random() * 10)) + 1)

# randrange(1, 46) - 1 <= x < 46

print(randrange(1, 46))
