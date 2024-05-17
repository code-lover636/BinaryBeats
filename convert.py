import pickle

with open('binary_player.py', 'r', encoding='utf-8') as text_file:
    content = text_file.read()

with open('music.bin', 'wb') as binary_file:
    pickle.dump(content, binary_file)
