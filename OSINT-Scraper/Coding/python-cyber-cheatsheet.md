# Python & Cybersecurity Cheat Sheet
*Built from projects, not copied from the internet.*
# Python & Cybersecurity Cheat Sheet

Purpose:

- Record concepts I have genuinely understood.
- Act as a quick reference while building projects.
- Help me revise before interviews.
- Keep explanations short and practical.
---

# Terminal

## pwd
Print Working Directory.
Shows where I currently am.

## ls
Lists files and folders in the current directory.

## cd folder
Changes into a folder.

## cd ..
Moves up one folder.

## mkdir folder
Creates a new folder.

## touch file.txt
Creates a new empty file.

---

# Running Python

Run a program:

```bash
python3 main.py
```

Run a program and give it information:

```bash
python3 hasher.py test.txt
```

---

# sys.argv

How a Python program receives information from the terminal.

Example:

```bash
python3 hasher.py test.txt
```

Python receives:

```python
sys.argv = [
    "hasher.py",
    "test.txt"
]
```

Therefore:

```python
sys.argv[1]
```

is

```
test.txt
```

---

# Variables

```
=
```

Store a value.

Example:

```python
name = "Fraser"
```

---

# Equality

```
==
```

Ask:

"Is this equal to this?"

Example:

```python
response.status_code == 404
```

---

# API Response

```python
response.status_code
```

Returns the HTTP status.

```python
response.json()
```

Returns the JSON sent back by the API.

---

# HTTP Status Codes

200
Success.

404
Not found.

401
Unauthorized.

403
Forbidden.

429
Too many requests.

---

# SHA-256

A fingerprint of a file.

If one byte changes, the fingerprint changes.

Rename a file → same hash.

Change the contents → different hash.

---

# Dictionaries

A dictionary stores information as:

key → value

Example:

```python
person = {
    "name": "Fraser",
    "age": 45
}
```

Read a value:

```python
person["name"]
```

returns

```
Fraser
```

---

# JSON

JSON is just a dictionary sent across the internet.

Example:

```json
{
    "name": "Fraser",
    "age": 45
}
```

After:

```python
response.json()
```

Python turns JSON into a dictionary so I can do:

```python
response.json()["name"]
```

---

# if / else

Ask a question.

If True:

do this.

Otherwise:

do something else.

Example:

```python
if response.status_code == 404:
    print("VirusTotal has no record of this file hash.")
else:
    print(response.json())
```

---

# VirusTotal Workflow

File

↓

SHA-256 fingerprint

↓

Send fingerprint to VirusTotal

↓

VirusTotal searches its database

↓

Returns JSON

↓

My program decides what to do.

---

# File Hasher

Input:

```bash
python3 hasher.py test.txt
```

Process:

Open file

↓

Read bytes

↓

Calculate SHA-256

↓

Print fingerprint

Output:

```
c87e2ca771...
```

---

# OSINT Scraper

Input:

SHA-256 hash

↓

Build URL

↓

Add API key

↓

Send request

↓

Receive response

↓

Check status code

↓

Display result


---

# Functions

A function is a reusable block of code.

Instead of writing the same code over and over:

```python
def greet():
    print("Hello")
```

Run it:

```python
greet()
```

---

# Parameters

Parameters let me pass information into a function.

```python
def greet(name):
    print(f"Hello {name}")
```

Call it:

```python
greet("Fraser")
```

---

# return

`return` sends a value back from a function.

```python
def add(a, b):
    return a + b
```

Example:

```python
answer = add(3, 4)
```

`answer` becomes:

```
7
```

---

# Reading Files

Open a file:

```python
with open(file_name, "rb") as file:
```

Read everything:

```python
data = file.read()
```

For hashing we use:

```python
"rb"
```

because SHA-256 hashes the raw bytes of a file.

---

# Environment Variables

Never put secret API keys directly into code.

Load them:

```python
load_dotenv()
```

Read them:

```python
api_key = os.getenv("VT_API_KEY")
```

---

# HTTP Request

Send a GET request:

```python
response = requests.get(url, headers=headers)
```

Meaning:

```
Ask this URL for information.
Include my API key.
Wait for the reply.
```

---

# f-Strings

An `f` string lets Python insert variables into text.

Example:

```python
name = "Fraser"

print(f"Hello {name}")
```

Output:

```
Hello Fraser
```

Used in the scraper:

```python
url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
```

Python replaces:

```
{file_hash}
```

with the real hash.

---

# Programmer's Mindset

Most programs follow the same pattern:

Input

↓

Process

↓

Decision

↓

Output

Keep asking:

- What is the input?
- What is the program doing?
- What decision is it making?
- What is the output?


---

# Python Objects

Everything in Python is an object.

Objects store both:

- Data
- Things they can do (methods)

Example:

```python
response
```

The response object contains:

```python
response.status_code
response.json()
response.headers
```

---

# Methods

Methods are things an object knows how to do.

Example:

```python
response.json()
```

means

"Response, turn yourself into a Python dictionary."

Another example:

```python
file.read()
```

means

"File, read yourself."

---

# Modules

Modules are libraries of code written by someone else.

Import them:

```python
import os
import requests
import hashlib
```

Then use them:

```python
hashlib.sha256()
```

---

# Import

Import means:

"Bring someone else's code into my program."

---

# Program Flow

A program is just instructions executed from top to bottom.

Example:

Load API key

↓

Create URL

↓

Create headers

↓

Send request

↓

Receive response

↓

Make decision

↓

Print output

---

# Common Mistakes

Forgetting :

```python
if something:
```

Using

```python
=
```

instead of

```python
==
```

Trying to access a dictionary key that doesn't exist.

Running Python from the wrong folder.

Forgetting to save before running.

---

# Debugging Checklist

Read the error carefully.

What line failed?

What object am I using?

What type is it?

What value does it currently contain?

Can I print it?

Never guess.

Investigate.

---

# Analyst Mindset

Always ask:

What do I know?

What don't I know?

What assumptions am I making?

What evidence supports this?

What evidence would change my mind?

---

# Developer Mindset

Programs are built from small steps.

Input

↓

Variables

↓

Functions

↓

Decisions

↓

Output

If I don't understand a program:

Break it into one line at a time.

Ask:

"What is this line trying to achieve?"



# Aha Moments

## 2026-07-30

- sys.argv is how a program receives information from the terminal.
- response.status_code tells me if the request succeeded.
- response.json() gives me the data returned by the API.
- A SHA-256 hash is a fingerprint, not the file itself.
- VirusTotal searches for the fingerprint, not the file.
- if/else lets my program make decisions based on the response.




---

# Reading Code

When I see code, I don't read it left to right first.

I ask four questions.

## 1. What is the input?

Examples:

```python
sys.argv
```

```python
response.json()
```

```python
open(file)
```

---

## 2. What is happening to the input?

Examples:

Hashing

Filtering

Sorting

Searching

Looping

Making a request

---

## 3. Is there a decision?

Example:

```python
if response.status_code == 200:
```

The program decides what to do next.

---

## 4. What is the output?

Examples:

```python
print()
```

Write to a file

Return a value

Send data to an API

---

# Data Types

String

```python
"hello"
```

Integer

```python
42
```

Float

```python
3.14
```

Boolean

```python
True
False
```

List

```python
["apple", "banana"]
```

Dictionary

```python
{
    "name": "Fraser"
}
```

---

# Loops

Repeat code.

```python
for item in items:
    print(item)
```

Ask:

"What changes each time?"

---

# Errors

Errors are information.

Read:

- What happened?
- Where?
- Why?

Fix one error at a time.

---

# Before Asking for Help

1. Read the error.
2. Read the line above it.
3. Print the variable.
4. Check the type.

```python
print(variable)

print(type(variable))
```

5. Think for two minutes.

Only then ask for help.

---

# Golden Rule

Don't memorise code.

Understand:

- Why it exists.
- What problem it solves.
- What goes in.
- What comes out.




# Response Object

When I send a request:

```python
response = requests.get(url, headers=headers)
```

Python stores the server's reply in a **Response object**.

A Response object contains:

- `response.status_code` → HTTP status (200, 404, etc.)
- `response.headers` → Information about the response.
- `response.text` → The raw text returned by the server.
- `response.json()` → Converts the JSON body into Python objects (usually dictionaries and lists).

The **response object is NOT a dictionary.**

It is a container holding everything the server sent back.

Only when I call:

```python
response.json()
```

does Python convert the JSON data into a dictionary or list that I can work with.

Example:

```python
data = response.json()

print(data["data"])
```




# Objects

Everything in Python is an object.

An object stores:

- Data (attributes)
- Actions it can perform (methods)

Examples:

```python
response
file
hash_object
```

Examples of attributes:

```python
response.status_code
response.headers
```

Examples of methods:

```python
response.json()
file.read()
```

Think:

**Attributes describe an object.**

**Methods do something.**

---

# Attributes

Attributes are pieces of information stored inside an object.

Examples:

```python
response.status_code
```

returns:

```
404
```

Another example:

```python
person.name
```

Attributes do **not** use brackets `()`.

---

# Methods

Methods are functions that belong to an object.

Examples:

```python
response.json()

file.read()

text.upper()
```

Methods almost always use brackets:

```python
()
```

because they perform an action.

---

# Classes

A class is the blueprint for creating objects.

Example:

A blueprint for a house is not a house.

A class is not an object.

An object is created from the class.

Example:

```
Class
    ↓
Object
```

Python creates a Response object from the Response class.

You don't normally create Response objects yourself.

The `requests` library creates one for you.

---

# Libraries

A library is a collection of code written by other programmers.

Instead of writing everything yourself:

```python
import requests
```

or

```python
import hashlib
```

You import their code and use it.

---

# Module vs Library

A module is a single Python file.

A library is a collection of modules.

Most people use the words interchangeably, but technically they are different.

Example:

```
Library
    ↓
Module
        ↓
Functions
```

---

# Mental Model

Program

↓

Imports libraries

↓

Creates objects

↓

Objects contain attributes and methods

↓

Methods perform actions

↓

Program produces output