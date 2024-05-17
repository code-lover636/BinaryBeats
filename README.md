# 🎵 Binary Beats: Making Music from Malware 🦠🎶

Welcome to **Binary Beats** this project turns menacing malware binaries into melodious music. 

## What's This All About?

At the heart of this project lies the core idea: what if we used the unique patterns of binaries as music? That's what we're doing here. We take a malware binary, read its bytes, and map them to musical notes.

## How It Works

1. **Read the Binary**: We start by reading the bytes of a malware file.
2. **Map to Musical Notes**: Each byte gets mapped to a musical note. We've got a range from C0 to B8.
3. **Compose the Tune**: These notes are then played in sequence, creating a unique piece of music based on the binary's structure.
4. **Play It Loud (or Soft)**: Finally, our script plays these notes, turning data into tunes!

## Installation

1. Clone this repo

    ```
    git clone https://github.com/LaurieWired/BinaryBeats.git
    ```

2. Linux dependencies
    ```
    sudo yum install -y python3-devel alsa-lib-devel
    ```
    OR
    ```
    sudo apt-get install -y python3-dev libasound2-dev
    ```

3. Install libraries

    ```
    pip install pydub simpleaudio
    ```


