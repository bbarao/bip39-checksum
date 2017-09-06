#!/usr/bin/env python3

import mnemonic
import sys


words_without_checksum = ' '.join(sys.argv[1:])
mnemo = mnemonic.Mnemonic('english')

for word in sys.argv[1:]:
    if word not in mnemo.wordlist:
        print("Sorry, '%s' is not a valid word" % word)
        sys.exit(1)

for word in mnemo.wordlist:
    if mnemo.check("%s %s" % (words_without_checksum, word)):
        print("possible checksum = %s" % word)

