# q1] Vowels and consonants and count them
def check_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    for i in s:
        if i.lower() in vowels:
            print(i+ '-vowel')
            # i is for current character and + is for concatenation used in string
            vowel_count = vowel_count + 1

        else:
            print(i+ '- consonant')
            consonant_count = consonant_count + 1
    return vowel_count, consonant_count


ip_given = input('enter a string:')
vowel_count, consonant_count = check_count(ip_given)
print('number of vowels:', vowel_count)
print('number of consonants',consonant_count)
