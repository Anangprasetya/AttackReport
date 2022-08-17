
def affine_decrypt(cipher):
    text = []
    for t in cipher:
        b = ord(t) - ord('A')
        for x in range(0, 26):
            result = (65 + x*89 - b) % 26
            if result == 0:
                text.append(chr(x + ord('A')))
                break

    print(''.join(text))
        

if __name__ == '__main__':
    affine_encrypted_text = "FAJSRWOXLAXDQZAWNDDVLSU"
    affine_decrypt(affine_encrypted_text)