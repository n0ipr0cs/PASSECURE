#!/usr/bin/python
# Creado by n0ipr0cs

import string

from random import*
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters)for x in range(randint(8,16)))
print "Tu password es:"
print password
print "Ya tienes un password fuerte"
print "************************************"
print "P A S S E C U R E  by n0ipr0cs"
print "************************************"
