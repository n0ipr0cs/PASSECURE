#!/usr/bin/python
# Creado by n0ipr0cs

import string

print	" ____       _      ____    ____    _____    ____   _   _   ____    _____ "
print	"|  _ \     / \    / ___|  / ___|  | ____|  / ___| | | | | |  _ \  | ____|"
print	"| |_) |   / _ \   \___ \  \___ \  |  _|   | |     | | | | | |_) | |  _|"
print	"|  __/   / ___ \   ___) |  ___) | | |___  | |___  | |_| | |  _ <  | |___"
print	"|_|     /_/   \_\ |____/  |____/  |_____|  \____|  \___/  |_| \_\ |_____|" 
print "******************************by n0ipr0cs*********************************"


print ""

from random import*
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters)for x in range(randint(8,16)))
print "Tu password es:" 
print password
print "Ya tienes un password fuerte"
