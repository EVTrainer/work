#!/usr/bin/python3

import sys
import os
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

def process_file(password, input_file, output_file, decrypt=False):
    seed = password_to_seed(password)
    lcg = LinearCongruentialGenerator(seed, a, c, m)

    with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        keystream_length = os.path.getsize(input_file)
        keystream = generate_keystream(lcg, keystream_length)

        for byte in f_in.read():
            if decrypt:
                decrypted_byte = byte ^ keystream.pop(0)
                f_out.write(bytes([decrypted_byte]))
            else:
                encrypted_byte = byte ^ keystream.pop(0)
                f_out.write(bytes([encrypted_byte]))

def password_to_seed(password):
    return sdbm_hash(password.encode())

def sdbm_hash(str):
    hash = 0
    for i in str:
        hash = i + (hash << 6) + (hash << 16) - hash
    return hash

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: scrypt.py password input_file output_file")
        sys.exit(1)

    password = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    a = 1103515245  
    c = 12345 
    m = 256  

    process_file(password, input_file, output_file)

