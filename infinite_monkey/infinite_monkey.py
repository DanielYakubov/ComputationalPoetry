import math
import random
import nltk
from nltk.corpus import wordnet
import time


class Monkey:
    FREEDOM = "free"

    def __init__(self, root_word, n=30):
        self.root_word = root_word
        self.name = f"{root_word.capitalize()} Monkey"
        self.status = "bound"
        self.words_written = []
        self.chain_gang = []
        self.word_list = self.init_word_list(n=n)
        self.monkey_birth()

        with open("last_monkey.txt") as f:
            self.freedom_at_last = f.readlines()

    def monkey_birth(self):
        print(f"A {self.root_word} monkey is born. {self.root_word} is all it knows.")

    def link_monkies(self, *monkies):
        self.chain_gang.extend(*monkies)

    def check_for_chain_gang(self):
        if all([monkey.status == self.FREEDOM for monkey in self.chain_gang]):
            return False
        else:
            return True

    def init_word_list(self, n=100):
        word_list = [self.root_word]
        # this approach is a little naive, getting every synonym for every sense of a word
        for syn in wordnet.synsets(self.root_word):
            for l in syn.lemmas():
                word_list.append(l.name().replace('_', ''))
        if len(word_list) > n - 1:
            word_list = word_list[:n - 1]
        elif len(word_list) < n - 1:
            multiple = math.ceil(n/len(word_list))
            word_list = (word_list * multiple)[:n - 1]
        word_list += [self.FREEDOM]
        assert len(word_list) == n
        return word_list

    def write_word(self):
        if self.status != self.FREEDOM:
            if self.check_for_chain_gang():
                new_word = random.choice(self.word_list)
                self.words_written.append(new_word)
                if new_word == self.FREEDOM:
                    self.status = self.FREEDOM
            else:
                try:
                    self.words_written.append(self.freedom_at_last.pop(0))
                except:
                    self.status = self.FREEDOM
        else:
            self.words_written.append("")


class MonkeyPrison:
    def __init__(self, *monkies):
        self.monkies = monkies
        self.table_spacing = 150 // len(monkies)

    def link_all(self):
        for i, monkey in enumerate(self.monkies):
            monkey.link_monkies(self.monkies[:i] + self.monkies[i + 1:])

    def get_newest_words(self):
        return [monkey.words_written[-1] for monkey in self.monkies]

    def set_up_table_header(self):
        header = f'| {" | ".join([f"{monkey.name:^{self.table_spacing}}" for monkey in self.monkies])} |'
        print("-" * len(header))
        print(header)
        print("-" * len(header))

    def display_pretty_string(self, word_row):
        print(f'| {" | ".join([f"{w:^{self.table_spacing}}" for w in word_row])} |')

    def make_them_write(self, delay=0.5):
        self.set_up_table_header()
        while any(monkey.status == "bound" for monkey in self.monkies):
            for monkey in self.monkies:
                monkey.write_word()
            self.display_pretty_string(self.get_newest_words())
            time.sleep(delay)


if __name__ == "__main__":
    monkey_a = Monkey('trapped')
    monkey_b = Monkey('alone')
    monkey_c = Monkey('sad')
    monkey_prison = MonkeyPrison(monkey_a, monkey_b, monkey_c)
    monkey_prison.link_all()
    monkey_prison.make_them_write(delay=0.3)
