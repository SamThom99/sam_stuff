with open("spelling_bee/words.txt", 'r') as file:
    words = [line.strip() for line in file.readlines()  if line.strip() != '']

unique_words = set(words)

# Convert the set back to a list and sort it
sorted_words = sorted(unique_words)

with open('spelling_bee/words.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(sorted_words))