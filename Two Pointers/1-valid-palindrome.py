def validPalindrome(word: str) -> bool:
    i, j = 0, len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i += 1
        j += 1
    return True