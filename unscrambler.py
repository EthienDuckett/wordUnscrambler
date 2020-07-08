#python3 because python doesn't like to work???????????????!!!!!!!
aword = str("filler")
unscramble = []
counter = 0
typo = "filler"
newlinec = 0
char = ""
wad = ""
wordlist = {}
end = []



dir = input("please enter the directory of the word list (if the word list is in the same folder just state the name of the word list)\n")
print("Please wait...\n")
def buildabc(word):
    abclist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# I wasn't sure what the most efficient way of gathering the number of letters was, the only ideas I had was a large if-else statement and iterating through the alphabet each time
# one nice thing about if elif statements is they will stop elifing once a single condition is true
    for c in word:
        if c == "a":
            abclist[0] += 1
        elif c == "b":
            abclist[1] += 1
        elif c == "c":
            abclist[2] += 1
        elif c == "d":
            abclist[3] += 1
        elif c == "e":
            abclist[4] += 1
        elif c == "f":
            abclist[5] += 1
        elif c == "g":
            abclist[6] += 1
        elif c == "h":
            abclist[7] += 1
        elif c == "i":
            abclist[8] += 1
        elif c == "j":
            abclist[9] += 1
        elif c == "k":
            abclist[10] += 1
        elif c == "l":
            abclist[11] += 1
        elif c == "m":
            abclist[12] += 1
        elif c == "n":
            abclist[13] += 1
        elif c == "o":
            abclist[14] += 1
        elif c == "p":
            abclist[15] += 1
        elif c == "q":
            abclist[16] += 1
        elif c == "r":
            abclist[17] += 1
        elif c == "s":
            abclist[18] += 1
        elif c == "t":
            abclist[19] += 1
        elif c == "u":
            abclist[20] += 1
        elif c == "v":
            abclist[21] += 1
        elif c == "w":
            abclist[22] += 1
        elif c == "x":
            abclist[23] += 1
        elif c == "y":
            abclist[24] += 1
        elif c == "z":
            abclist[25] += 1
    return "a{0}b{1}c{2}d{3}e{4}f{5}g{6}h{7}i{8}j{9}k{10}l{11}m{12}n{13}o{14}p{15}q{16}r{17}s{18}t{19}u{20}v{21}w{22}x{23}y{24}z{25}".format(abclist[0], abclist[1], abclist[2], abclist[3], abclist[4], abclist[5], abclist[6], abclist[7], abclist[8], abclist[9], abclist[10], abclist[11], abclist[12], abclist[13], abclist[14], abclist[15], abclist[16], abclist[17], abclist[18], abclist[19], abclist[20], abclist[21], abclist[22], abclist[23], abclist[24], abclist[25])
#opens the file when 'read' is called
with open(dir, "r") as list:
    read = list.read()
# counts the number of '\n' also known as 'enter'
    for c in read:
        if c == "\n":
            newlinec += 1
# iterates by using enters in between words in the word list
    for c in range(newlinec):
        wad = ""
# compiles singular words
        while char != "\n":
            wad += char
            char = read[counter]
            counter += 1
# I need to check if the dictonary already has a key that is the same as the one about to be added, if it does then the values need to be added together

        try:
            check = wordlist[buildabc(wad)]
        except:
            check = wad

# basically check asks buildabc for any values associated with the current key, then those values are compared to wad, which is the current word. Even simpler, it checks if wordlist has the key that is about to be added
        if check == wad:
            wordlist[buildabc(wad)] = wad
        else:
            wordlist[buildabc(wad)] = wad + "-" + check
# char needs to be reset because it is still equal to '\n' after the while loop closes
        char = ""
    counter = 0


    print("please enter words seperately and press enter to input a entry (just press enter to advance)")
# this while loop takes your input and puts it into an array
    while(aword != ""):
        counter += 1
        unscramble.append(aword.lower())
        aword = input("enter word {0}:\n".format(counter))
    del unscramble[0]
# the while loop checks if you have entered nothing, if you entered something, that info is taken to the if loop which fixes the typo
    while typo != "":
        typo = input("if you made a typo enter what number it was entered as followed by the corrected version\n").lower()
        if typo != "":
            unscramble[int(typo[0])-1] = typo[1:len(typo)]

    # for c in range(len(unscramble)):
    #     unscramble.append(buildabc(unscramble[c]))
# I decided halfway through that instead of using factorials to generate a word out of 14 characters which would have 87178291200 combinations and would take a few hours (or days) and take like 1220 gigabytes of ram/disk space I would use my own method which was probably invented already
# I will take the number of letters in a word and compare them to a dictonary of the number of letters in real words it will be harder to make work but it sounds like fun!



for c in unscramble:
    print(c)
    try:
        print(wordlist[buildabc(c)])
        open("unscrambled.txt", "a").write(wordlist[buildabc(c)] + "\n")
    except:
        end.append(c)
for c in end:
    open("unscrambled.txt", "a").write("the word could not be unscrambled:  " + c + "\n")

print("your text file with everything unscrambled is ready! Delete your file or rename it if you don't want a mess...")
