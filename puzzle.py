import csv
import timeit


def read():
    with open('words4') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        temp = []
        for row in csv_reader:
            temp.append(row[0])
            line_count += 1
        return temp


def miss():
    with open('puzzle4') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        temp = []
        for row in csv_reader:
            temp.append(row[0])
            line_count += 1
        return temp


def findword(words, size):
    for i in range(len(words)):
        if len(words[i]) is size:
            word = words.pop(i)
            return str(word)


def findlen(word, loc):
    count = 0
    i = loc
    while (len(word)) != i and word[i] == '_':
        count += 1
        i += 1
    return count


def fill(words, missing):
    for i in range(len(missing)):
        loc = missing[i].find('_')
        while loc != -1:
            length = findlen(missing[i], loc)
            # print(length)
            word = findword(words, length)
            # print(word)
            missing[i] = missing[i][:loc] + word + missing[i][loc+len(word):]
            loc = missing[i].find('_')
            # print(loc)
    words.pop(-1)


start = timeit.default_timer()
words = read()
missing = miss()
#print("missing\n", missing)

fill(words, missing)
print("\n\n filled\n", missing)

stop = timeit.default_timer()
print('Time: ', stop - start)
