import collections
def groupAnagram(s: list[str]) -> list[list[str]]:
    tracker = collections.defaultdict(list)
    for word in s:
        counter = [0] * 26
        for letter in word:
            counter[ord(letter) - ord('a')] += 1
        tracker[tuple(counter)].append(word)
    return tracker.values()