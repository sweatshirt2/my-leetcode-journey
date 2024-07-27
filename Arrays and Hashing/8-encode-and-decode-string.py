def encodeString(strs: list[str]) -> str:
    encoded = ''
    for word in strs:
        encoded += (str(len(word)) + word)
    return encoded


def decodeString(encoded: str) -> list[str]:
    encoded = '2we3are4back'
    strs = []
    i = 0
    while i < len(encoded):
        span = int(encoded[i]) + 1
        strs.append(encoded[i+1: i+span])
        i += span
    return strs