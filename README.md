# ComputationalPoetry

This repo contains several computational poems I've been working on in python. What is a computational poem? Depends on who you ask, but to me it's essentially any form of poetry which is presented with some digital and/or code manupulations. These being python does not imply that someone can't make a poem using a gameboy emulator. Heavily inspired through attending [WordHack NYC events](https://toddwords.com/wordhack/).

## General Note

The poems are slightly obstructed in content to prevent them being experienced in any other way than through the program, meaning, they are put through a simple caesar shift so that the temptation to just read the txt is slightly reduced.

## Elevator

There is a quite famous poem called "Elevator" by Mark Strand. It's perhaps my favorite example of repetition being used in poetry. Oftentimes in poetry, repetition is used for emotional effect, or irony -- but in "Elevator", the meaning of the poem is the repetition itself.

The poem repeats the stanza twice (each time numbered, 1 and 2). This repo remixes this poem and instead makes it repeat an infinite amount of times, the poem is printed at 14.69ms per char, per Demberg & Keller (2008). My current record of running it locally is a measly 226, but I may consider running this on a server at some point. Why? It's a form of art, so why not? 

Note the part that says 'infinite' -- there's a while-true loop in this script, so be mindful if you choose to run it.

_Upon Execution_
It's really just an infinite version of "Elevator" by Mark Strand that prints incremenatally to stdout.

## Infinite Monkies

A play on the ["Infinite Monkey Theorem"](https://en.wikipedia.org/wiki/Infinite_monkey_theorem). The idea is you initialize X monkies that have a 1 in N chance of being freed from typing forever. 

A more formal definition of my variation of the theorem is coming at some point, but a core idea is that the monkies are initialized with root words, and are "forced" to type similar words to the root word with some % chance of typing the word "free". When they type the word, they are released from service.

But what happens to the last monkey remaining?

_Upon Execution_
The beginning of the poem looks like a very very depressing spreadsheet, and changes once the second to last "free" is uttered. Technically, the amount of monkies, the chance to write free, and the root words are all configurable.
![Inf Monkies](https://github.com/user-attachments/assets/3ae07dc4-60f5-4076-9ad3-a9642edf8309)

## Tsunami

This poem was written from a re-occuring nightmare I keep having, so in a sense, it's certainly the most personal of the poems in this repository. It prints the poem at an increasing pace, each line is first proceeded by a series of '.' and '/' representing a ratio of calm ocean, to large waves. 

_Upon Execution_
You can expect about a minute long sequence. The lines are each proceeded by sequences of '.' and '/' with a changing ratio based on some function (as of writing this I am not satisfied with the current one). The output speed increases each line as well.  
![Tsunami Execution](https://github.com/user-attachments/assets/f63fce22-41c2-4260-8bc9-d7ddca81cb81)


# References
Demberg, V., & Keller, F. (2008). Data from eye-tracking corpora as evidence for theories of syntactic processing complexity. Cognition, 109, 193-210.

# Contributions
Not sure why you would want to
