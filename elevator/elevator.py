import time

# from Mark Strand, "Elevator"
with open("stanza.txt", "r") as f:
    STANZA = f.read()
INTERVAL = 14.69 / 1000
STANZA_NUM = 1

while True:
    print(STANZA_NUM)
    for c in STANZA:
        print(c, end='', flush=True)
        time.sleep(INTERVAL)
    print('\n')
    STANZA_NUM += 1
