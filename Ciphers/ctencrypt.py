#!/usr/bin/python3

import sys
import argparse

def columnar_transposition_encrypt(plaintext, key, block_size):
    extended_key = (key * (block_size // len(key))) + key[:block_size % len(key)]
    num_columns = (len(plaintext) + block_size - 1) // block_size
    grid = [['' for _ in range(num_columns)] for _ in range(block_size)]

    for i, char in enumerate(plaintext):
        row = i % block_size
        col = i // block_size
        grid[row][col] = char

    key_indices = sorted(range(len(extended_key)), key=lambda k: extended_key[k])
    reordered_grid = [['' for _ in range(num_columns)] for _ in range(block_size)]
    for new_row, old_row in zip(key_indices, grid):
        reordered_grid[new_row] = old_row

    ciphertext = ''.join(''.join(row) for row in reordered_grid)

    return ciphertext

def parse_arguments():
    parser = argparse.ArgumentParser(description='Columnar Transposition Cipher Encryption')
    parser.add_argument('-b', '--blocksize', type=int, default=16, help='Block size (default: 16)')
    parser.add_argument('-k', '--key', help='Encryption key')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input file')
    args = parser.parse_args()

    if args.key is None:
        print("Error: Encryption key not provided.")
        parser.print_help(sys.stderr)
        sys.exit(1)

    return args

def main():
    args = parse_arguments()

    if args.file is not sys.stdin:
        plaintext = args.file.read()
        args.file.close()
    else:
        plaintext = sys.stdin.read()

    ciphertext = columnar_transposition_encrypt(plaintext, args.key, args.blocksize)
    sys.stdout.write(ciphertext)

if __name__ == '__main__':
    main()
