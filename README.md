# pokemon-char-encoding-translator
I was stunned to not have found something like this, so I coded a pokemon word decoder in python


The concept is simple, every character map is a csv file divided by \t chars
For now I've only implemented FireRed International map but adding more should be pretty straight forward.

This project was developed in about 2-3hours so it probably has a lot of room for improvements, please feel free to submit pull-requests

## Usage (python3 required):
  - $python3 pk_char_to_ascii.py
  - Select the desired char map
  - Insert the encoded bytes in hex (all of the 10 bytes are required)

## Possibile new features:
  1. Move the csv files in a directory and generate selector array dinamically
  2. Implement a more stable way to select languages and edge cases for pokemon games encodings 
  3. Clean user input to ensure there are no white spaces
  
### ALL THE INFORMATION REGARDING THE CHARACHTERS ENCODING WERE FOUND ON BULBAPEDIA (https://bulbapedia.bulbagarden.net/wiki/Character_encoding_(Generation_III))
