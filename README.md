# Caesar Cipher

A command-line Caesar cipher tool built in Python.

## What it does
- Encrypts and decrypts messages using a shift key
- Preserves case and passes through spaces/punctuation unchanged
- Includes a brute-force breaker that tries all 25 possible shifts

## How to run
python3 cipher.py

You will be prompted to enter:
- Your message
- A shift number (1-25)
- A mode: encrypt, decrypt, or brute

## What it demonstrates
Encryption fundamentals, modular arithmetic for alphabet wraparound, 
and why substitution ciphers are vulnerable to exhaustive key search.
