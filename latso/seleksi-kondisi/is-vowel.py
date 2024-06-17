def is_vowel(char):
    if char in "aeiou":
        return True
    else:
        return False
    
char = input("Masukkan salah satu huruf abjad: ")
print(char, "huruf vokal?", is_vowel(char))