alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(message, shift):
    result = ""
    for letter in message:
        if letter in alphabet or letter.lower() in alphabet:
            original_case_upper = letter.isupper()
            letter = letter.lower()
            position = alphabet.index(letter)
            shifted_position = (position + shift) % 26
            new_letter = alphabet[shifted_position]
            if original_case_upper:
                new_letter = new_letter.upper()
            result = result + new_letter
        else:
            result = result + letter
    return result

def decrypt(message, shift):
    return encrypt(message, -shift)

def brute_force(message):
    for i in range(1, 26):
        print(i, decrypt(message, i))
message = input("Enter your message: ")
shift = int(input("Enter shift number: "))
mode = input("Mode (encrypt/decrypt/brute): ")

if mode == "encrypt":
    print(encrypt(message, shift))
elif mode == "decrypt":
    print(decrypt(message, shift))
elif mode == "brute":
    brute_force(message)