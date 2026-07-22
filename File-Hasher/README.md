# File Hasher

A simple Python command-line tool that generates the SHA-256 hash of a file.

## Features

- Generates SHA-256 hashes
- Reads any file in binary mode
- Accepts the filename as a command-line argument
- Displays the hash in hexadecimal format

## Requirements

- Python 3

## Usage

```bash
python3 hasher.py <filename>
```

Example:

```bash
python3 hasher.py test.txt
```

## Example Output

```
135a991634a2a252cf538acba0ec272a5c8322b8d07e65dbde484074977dfec0
```

## What I Learned

While building this project I practised:

- Reading files in binary mode
- Using Python's `hashlib` library
- Working with command-line arguments using `sys.argv`
- Basic terminal navigation
- Organising a project for GitHub

## Future Improvements

- Support multiple hashing algorithms (MD5, SHA-1, SHA-512)
- Hash entire folders
- Compare two files by hash
- Add progress information for large files

## Author

Fraser Scott