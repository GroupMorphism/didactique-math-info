# test py file
import hashlib

import hashlib

m = hashlib.sha256()
print(b"Nobody inspects")
m.update(b"Nobody inspects")

print(m.hexdigest())

m.update(b" the spammish repetition")

print(m.hexdigest())

m.update(b"Nobody inspects the spammish repetition")

print(m.hexdigest())