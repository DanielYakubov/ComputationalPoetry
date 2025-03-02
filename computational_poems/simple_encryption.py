"""This file implements a caesar cipher. The point isn't to make it impossible to crack (otherwise, this would be
the worst encryption possible) it's just to slightly discourage folks from reading the poems in their text form,
as they are not meant to be read that way"""
from string import ascii_lowercase, ascii_uppercase
import argparse


def caesar_shift(passage: str, shift=3) -> str:
    """Uses a caesar shift to naively encrypt a given passage

    The shift is the amount the text is moved. A text encrypted by shift = n, can subsequently be decrypted by
    shift = -1.

    Args:
        passage (str): a text to be encrypted. Will only work with English at the moment.
        shift (int): the factor which to shift by, set to negative for decryption.

    Returns:
        new_passage (str): a shifted-by-n version of the passage.
    """
    mod = len(ascii_lowercase)  # should be 26, unless English changes
    new_passage: list[str] = []
    for char in passage:
        if char not in ascii_lowercase and char not in ascii_uppercase:
            new_passage.append(char)
        else:
            capital_char = char.isupper()
            idx = (ascii_lowercase.index(char.lower()) + shift) % mod
            if capital_char:
                new_char = ascii_uppercase[idx]
            else:
                new_char = ascii_lowercase[idx]
            new_passage.append(new_char)
    new_passage = ''.join(new_passage)
    return new_passage


def encrypt_file(file_path: str, encrypt_method=caesar_shift, *args, **kwargs):
    """Encrypt a file in-place using a string encyption method

    Args:
          file_path (str): the file_path of the txt file we want to modify

    Returns:
         None, overrides the original file.
   """
    with open(file_path, 'r') as dump:
        file_text = dump.read()
    with open(file_path, 'w') as sink:
        changed_text = encrypt_method(file_text, *args, **kwargs)
        sink.write(changed_text)


if __name__ == "__main__":
    # some basic in module tests
    original_string = "Shall I compare thee to a summer's day?\nThou art more lovely and more temperate."
    three_shift_string = "Vkdoo L frpsduh wkhh wr d vxpphu'v gdb?\nWkrx duw pruh oryhob dqg pruh whpshudwh."
    assert caesar_shift(original_string, shift=3) == three_shift_string
    assert original_string == caesar_shift(three_shift_string, shift=-3)
    assert caesar_shift(original_string, shift=29) == three_shift_string
    assert original_string == caesar_shift(three_shift_string, shift=-29)

    # CLI
    parser = argparse.ArgumentParser(
        prog='SimpleEncrypt',
        description='Encrypts text files'
    )
    parser.add_argument("filename", help="The name of the file you are going to encrypt")
    parser.add_argument("--shift", type=int, required=False, help="The amount to shift by if using a caesar cipher")
    parser.add_argument("--encryption_method", required=False, default=caesar_shift, help="The encryption method to use")
    args = parser.parse_args()

    encrypt_file(args.filename, encrypt_method=args.encryption_method, shift=args.shift)
