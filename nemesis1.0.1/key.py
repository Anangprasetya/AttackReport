import sys

def affine_encrypt(text, key):
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ])




if __name__ == '__main__':  
    affine_text="FUN"
    for key0 in range(65, 91):
        for key1 in range(65, 91):
            encrypt_text = affine_encrypt(affine_text, [key0, key1])
            if encrypt_text == "QZA":
                print(key0,key1)
                sys.exit(0)