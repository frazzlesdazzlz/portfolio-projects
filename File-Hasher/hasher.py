import hashlib
import sys

# Check that the user supplied exactly one filename
if len(sys.argv) != 2:
    print("Usage: python3 hasher.py <filename>")
    sys.exit(1)

# Get the filename from the command line
file_name = sys.argv[1]

# Open the file in binary mode
with open(file_name, "rb") as file:
    # Read all of the bytes from the file
    file_contents = file.read()

    # Create a SHA-256 hash object
    file_hash = hashlib.sha256(file_contents)

# Display the hash as hexadecimal
print(file_hash.hexdigest())
