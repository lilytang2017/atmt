
from collections import defaultdict
import sys

infile = sys.argv[1]

def distinctN_calc(filename): # task 2.4: calculate distinct n-grams at token level, for each system's predictions

    r = defaultdict(lambda: [])
    linecount = defaultdict(lambda: 0)

    scores = []
    #read in file
    with open(filename, "r") as fh:
        #print(file[:1000])
        content = fh.read()
    lines = content.split('\n')
    print("  Lines found:", len(lines))

    distinctN = []

    allNgrams = defaultdict(lambda: [])
    allNgrams_count = defaultdict(lambda: 0)
    uniNgrams_count = defaultdict(lambda: 0)

    for line in lines:
        #print("- line:", line)
        line = line.replace('.', '')
        line = line.replace(',', '')
        line = line.replace('?', '')
        line = line.replace('!', '')
        #print("- line2:", line)
        tokens = line.split(' ')
        for n in range(1,3):
            allNgrams[n] = []
            le = len(tokens)
            lasti = le + 1 - n
            #print(" -n-gram:", n, " last:", lasti)
            for i in range(0,lasti):
                j = i + n
                ngram = tuple(tokens[i:j])
                #print("  - ngram:", i, " = ", ngram)
                allNgrams[n].append(ngram)
        for n in range(1,3):
            #print("\nall", n, "grams:", len(allNgrams[n]), allNgrams[n])
            allNgrams_count[n] += len(allNgrams[n])
            unique = []
            for ngram in allNgrams[n]:
                #print("- ngram:", ngram)
                if ngram not in unique:
                    unique.append(ngram)
                    #print("    #### unique!")
            #print("\n- unique:", len(unique), unique)
            uniNgrams_count[n] += len(unique)
    for n in range(1,3):
        percentUnique = round(uniNgrams_count[n] / allNgrams_count[n] * 100, 2)
        #print("All", n, "grams:", allNgrams_count[n], "   uni", n, uniNgrams_count[n], "->", percentUnique, "%")
        distinctN.append(percentUnique)

    return(distinctN)

print("Calculating distinct1 and distinct2 scores, in %. \n  Input in:", infile)

distinct1, distinct2 = distinctN_calc(infile)
print("Results: distinct1:", distinct1, "  distinct2:", distinct2)
