import map_gen
import json

modes = ["FR"]

def main():
    try:
        selected = int(input("Select the charmap that you wnat to use (0->FireRed): "))
    except:
        print("Invalid number inserted")
        return
    
    try:
        char_map = json.loads(map_gen.gen(modes[selected]))
    except:
        print("Could not load map char")

    if  selected > len(modes)-1:
        print("Invalid mode selected")
        return

    pkmn_char = input("Insert the Pokémon's name bytes in hex (10 bytes): ")
    
    if len(pkmn_char) != 20:
        print("Invalid bytes inserted", len(pkmn_char))
        return
    
    buf = ""
    res = ""

    for i in range(20):
        if i%2 == 0:
            buf = pkmn_char[i:i+2]
            first = buf[0:1]
            second = buf[1:2]
            asciiChar = char_map[first.capitalize()+"-"]["-"+second.capitalize()]
            res += asciiChar
    
    print("Result is: "+res)

if __name__ == "__main__":
    main()
