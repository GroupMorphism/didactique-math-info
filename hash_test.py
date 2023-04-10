# test py file
import hashlib

import hashlib

m = hashlib.sha256()
text = b"Irenka is the best"

m.update(text)

print('Texte:'+str(text))
print('Hash:'+m.hexdigest())







