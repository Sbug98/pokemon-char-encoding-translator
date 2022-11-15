import map_gen
import json

modes = ["FR"]

def main():
    try:
        selected = int(input("Select the charmap that you want to use (0->FireRed): "))
    except:
        print("Invalid number inserted")
        return
    
    try:
        char_map = json.loads(map_gen.gen(modes[selected]))
    except:
        print("Could not load char map")
        return

    if  selected > len(modes)-1:
        print("Invalid mode selected")
        return

    try:
        pkmn_char = input("Insert the Pokémon char bytes in hex: ")
        int(pkmn_char, 16)
    except:
        print("Invalid hex value")
        return
    
    if len(pkmn_char) % 2 != 0:
        print("Invalid bytes")
        return

    buf = ""
    res = ""

    for i in range(len(pkmn_char)):
        if i%2 == 0:
            buf = pkmn_char[i:i+2]
            first = buf[0:1]
            second = buf[1:2]
            asciiChar = char_map[first.capitalize()][second.capitalize()]
            res += asciiChar
    
    print("Result is: "+res)

if __name__ == "__main__":
    main()
