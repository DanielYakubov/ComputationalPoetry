import time
import os

from computational_poems.simple_encryption import caesar_shift

# from Mark Strand, "Elevator"
text_file = f"{os.path.dirname(os.path.abspath(__file__))}/stanza.txt"
with open(text_file, "r") as f:
    stanza_encoded = f.read()
    STANZA = caesar_shift(stanza_encoded, shift=-3)
INTERVAL = 14.69 / 1000
STANZA_NUM = 1

while True:
    print(STANZA_NUM)
    for c in STANZA:
        print(c, end='', flush=True)
        time.sleep(INTERVAL)
    print('\n')
    STANZA_NUM += 1
