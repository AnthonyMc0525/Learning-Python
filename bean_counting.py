def counr_char(word, char):
    total = 0
    for letter in word:
        if letter == char:
            total += 1

    return total

print(count_char('BBC', 'B'))
print(count_char('kakkerlak', 'k'))
