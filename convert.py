# Run this file if u need to convert any text file to binary file

import pickle

# CHANGE THESE VALUES
INPUT_FILE = "README.md"  # Path to the input text file
OUTPUT_FILE = "music.bin" # Path to the output binary file

with open(INPUT_FILE, 'r', encoding='utf-8') as text_file:
    content = text_file.read()

with open(OUTPUT_FILE, 'wb') as binary_file:
    pickle.dump(content, binary_file)

https://github.com/code-lover636/BinaryBeats.git