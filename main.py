# print("hello world")
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
words = file_contents.split()
# print(len(words))
lower_contents = file_contents.lower()
letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
# print(letters.keys())

for i in range(0, len(lower_contents)):
    if lower_contents[i] in letters.keys():
        letters[lower_contents[i]] += 1
# print(letters)
sortedDict = sorted(letters.items(), key=lambda x:x[1], reverse=True)
# print(sortedDict[0][0])
print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} were found in the document")
print()
for i in range(0, len(sortedDict)):
    print(f"The {sortedDict[i][0]} character was found {sortedDict[i][1]} times")
print("--- End report ---")