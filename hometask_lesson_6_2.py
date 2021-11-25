# Task 2
with open('nginx_logs.txt') as f:
   spam_dictionary ={}
   for line in f:
      splitted = line.split()
      spam_dictionary.setdefault(splitted[0], 0)
      spam_dictionary[splitted[0]] += 1

spam_dictionary = sorted(spam_dictionary.items(), key=lambda x: x[1], reverse=True)
print(spam_dictionary[:5])
