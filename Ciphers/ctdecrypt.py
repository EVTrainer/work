#!/usr/bin/python3

import sys
import argparse

def columnar_transposition_decrypt(ciphertext, key, block_size):
    extended_key = (key * (block_size // len(key))) + key[:block_size % len(key)]
    num_columns = (len(ciphertext) + block_size - 1) // block_size
    grid = [['' for _ in range(num_columns)] for _ in range(block_size)]

    k = 0
    for j in range(num_columns):
        for i in range(block_size):
            if k < len(ciphertext):
                grid[i][j] = ciphertext[k]
                k += 1
            else:
                break

    key_indices = sorted(range(len(extended_key)), key=lambda k: extended_key[k])
    reordered_grid = [['' for _ in range(num_columns)] for _ in range(block_size)]
    for new_row, old_row in zip(key_indices, grid):
        reordered_grid[new_row] = old_row
        
    plaintext = ''
    for i in range(block_size):
        for j in range(num_columns):
            if reordered_grid[i][j] != '':
                plaintext += reordered_grid[i][j]

    return plaintext.rstrip()

def parse_arguments():
    parser = argparse.ArgumentParser(description='Columnar Transposition Cipher Decryption')
    parser.add_argument('-b', '--blocksize', type=int, default=16, help='Block size (default: 16)')
    parser.add_argument('-k', '--key', help='Decryption key')
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input file')
    args = parser.parse_args()

    if args.key is None:
        print("Error: Decryption key not provided.")
        parser.print_help(sys.stderr)
        sys.exit(1)

    return args

def main():
    args = parse_arguments()

    if args.file is not sys.stdin:
        ciphertext = args.file.read()
        args.file.close()
    else:
        ciphertext = sys.stdin.read()

    plaintext = columnar_transposition_decrypt(ciphertext, args.key, args.blocksize)
    sys.stdout.write(plaintext)

if __name__ == '__main__':
    main()
