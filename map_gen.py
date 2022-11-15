def clean_hex(n):
    return n.replace("0x", "").capitalize()

def gen(name):
    char_csv = open(name+".csv", "r")
    char_map = char_csv.readlines()
    char_csv.close()

    res = '{'

    for i in range(16):
        line = char_map[i]
        line_chars = line.split("\t")
        res += '"'
        first_hex_cipher = clean_hex(hex(i))
        res += first_hex_cipher + '": {'
        for j in range(16):
            ascii_char = line_chars[j].replace("\n", "")
            res += '"'
            second_hex_cipher = clean_hex(hex(j))
            if ascii_char == '"':
                ascii_char = '\"'
            res += second_hex_cipher+'": "'+ascii_char+'", '
            if j==15:
                res = res[0:len(res)-2]
        res += "}, "

    res = res[0:len(res)-2]+"}"
    return res

if __name__ == "__main__":
    gen("FR")
