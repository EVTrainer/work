#!/usr/bin/python3

import sys
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

def decrypt(password, input_file, output_file):
    seed = password_to_seed(password)
    lcg = LinearCongruentialGenerator(seed, a, c, m)

    try:
        with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:

            iv = bytearray(f_in.read(16))
            if len(iv) != 16:
                print("Error: Unable to read IV from the ciphertext file.")
                return

            previous_ciphertext_block = iv

            while True:
                ciphertext_block = bytearray(f_in.read(16))
                if len(ciphertext_block) < 16:
                    break  

                temp_block = bytearray(a ^ b for a, b in zip(ciphertext_block, generate_keystream(lcg, 16)))

                keystream = generate_keystream(lcg, 16)
                for i in range(15, -1, -2):
                    first = keystream[i] & 0xf
                    second = (keystream[i] >> 4) & 0xf
                    temp_block[first], temp_block[second] = temp_block[second], temp_block[first]

                plaintext_block = bytearray(a ^ b for a, b in zip(temp_block, previous_ciphertext_block))

                f_out.write(plaintext_block)

                previous_ciphertext_block = ciphertext_block

    except Exception as e:
        print("Error:", e)

def password_to_seed(password):
    return sdbm_hash(password.encode())

def sdbm_hash(str):
    hash = 0
    for i in str:
        hash = i + (hash << 6) + (hash << 16) - hash
    return hash

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: sbdecrypt.py password input_file output_file")
        sys.exit(1)

    password = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    
    a = 1103515245 
    c = 12345  
    m = 256 

    decrypt(password, input_file, output_file)