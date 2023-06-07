from collections import defaultdict
def group_anagrams(words):
    d = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        d[sorted_word].append(word)
    return list(d.values())

l = list(map(str, input("Enter a list of words (space-separated): ").split()))
result = group_anagrams(l)

print("Grouped Anagrams:")
for group in result:
    print(group)