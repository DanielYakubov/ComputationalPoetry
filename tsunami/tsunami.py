import time
import os, platform

DROPLET: str = "."
WAVE: str = "/"
INTERVAL: float = 50 / 1000


def clear():
    # https://stackoverflow.com/questions/37071230/trying-to-clear-overwrite-standard-output-using-os-systemcls-in-pycharm-does
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def slow_print(already_printed: str, line: str, interval: float):
    clear()
    print("\n".join(already_printed), flush=True)
    for c in line:
        print(c, end='', flush=True)
        time.sleep(interval)
    print('\n\n\n\n', flush=True)


def stagger(index: int, total_lines: int) -> str:
    offset = total_lines - (index + 1)
    ocean = [DROPLET] * total_lines * 2
    wave_frequency = ((total_lines * 2) - 4) // (index + 1)
    turbulent_ocean = [drop if (j + 1) % wave_frequency or j < offset
                       else WAVE for j, drop in enumerate(ocean)]
    return "".join(turbulent_ocean)


if __name__ == "__TSUNAMI__":
    with open("tsunami.txt", "r") as file:
        tsunami_poem = file.readlines()

    total_lines = len(tsunami_poem)
    already_printed: list[str] = []
    for i, line in enumerate(tsunami_poem):
        line = line.rstrip()
        # I want the printing to get faster each iteration
        new_interval = INTERVAL - (2 / 1000)
        if line:
            slow_print(already_printed, stagger(i, total_lines), new_interval)
            slow_print(already_printed, line, new_interval)
        else:
            print(line)
        already_printed.append(line)
