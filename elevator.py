import time

# Mark Strand, "Elevator"
STANZA = """The elevator went to the basement. The doors opened.
A man stepped in and asked if I was going up.
\"I’m going down,\" I said. \"I won’t be going up.\""""
INTERVAL = 14.69 / 1000
STANZA_NUM = 1

while True:
    print(STANZA_NUM)
    for c in STANZA:
        print(c, end='')
        time.sleep(INTERVAL)
    print('\n')
    STANZA_NUM += 1
