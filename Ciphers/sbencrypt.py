#!/usr/bin/python3

import sys
import os
import argparse

class LinearCongruentialGenerator:
    def __init__(self, seed, a, c, m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def generate(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

def generate_keystream(lcg, length):
    keystream = bytearray()
    for _ in range(length):
        keystream.append(lcg.generate() & 0xFF)  
    return keystream

def encrypt(password, input_file, output_file):
    seed = password_to_seed(password)
    lcg = LinearCongruentialGenerator(seed, a, c, m)

    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        iv = bytearray(generate_keystream(lcg, 16))

        previous_ciphertext_block = iv

        while True:
            plaintext_block = bytearray(f_in.read(16))
            if not plaintext_block:
                break

            if len(plaintext_block) < 16:
                padding_size = 16 - len(plaintext_block)
                plaintext_block += bytes([padding_size]) * padding_size

            temp_block = bytearray(a ^ b for a, b in zip(plaintext_block, previous_ciphertext_block))

            keystream = generate_keystream(lcg, 16)

            for i in range(16):
                first = keystream[i] & 0xf
                second = (keystream[i] >> 4) & 0xf
                temp_block[first], temp_block[second] = temp_block[second], temp_block[first]

            ciphertext_block = bytearray(a ^ b for a, b in zip(temp_block, keystream))

            f_out.write(ciphertext_block)

            previous_ciphertext_block = ciphertext_block

def password_to_seed(password):
    return sdbm_hash(password.encode())

def sdbm_hash(str):
    hash = 0
    for i in str:
        hash = i + (hash << 6) + (hash << 16) - hash
    return hash

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: sbencrypt.py password input_file output_file")
        sys.exit(1)

    password = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    
    a = 1103515245 
    c = 12345
    m = 256

    encrypt(password, input_file, output_file)
