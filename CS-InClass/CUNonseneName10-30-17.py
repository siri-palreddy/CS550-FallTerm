import sys




newFirstNames = {
	"b" : "lumpy",
	"c" : "buttercup",
	"d" : "gidget",
	"e" : "crusty",
	"f" : "greasy",
	"g" : "fluffy",
	"h" : "cheeseball",
	"i" : "chim-chim",
	"j" : "poopsie",
	"k" : "flunky",
	"l" : "booger",
	"m" : "pinky",
	"n" : "zippy",
	"o" : "goober",
	"p" : "doofus",
	"q" : "slimy",
	"r" : "loopy",
	"s" : "snotty",
	"t" : "falafel",
	"u" : "dorkey",
	"v" : "squeezit",
	"w" : "oprah",
	"x" : "skipper",
	"y" : "dinky",
	"z" : "zsa-zsa"
}

newLastName1 = {
    "a" : "diaper",
    "b" : "toilet",
    "c" : "giggle",
    "d" : "bubble",
    "e" : "girdle",
    "f" : "barf",
    "g" : "lizard",
    "h" : "waffle",
    "i" : "cootie",
    "j" : "monkey",
    "k" : "potty",
    "l" : "liver",
    "m" : "banana",
    "n" : "rhino",
    "o" : "burger",
    "p" : "hamster",
    "q" : "toad",
    "r" : "gizzard",
    "s" : "pizza",
    "t" : "gerbil",
    "u" : "chicken",
    "v" : "pickle",
    "w" : "chuckle",
    "x" : "tofu",
    "y" : "gorilla",
    "z" : "stinker"
}

newLastName2 = {
"a" : "head",
"b" : "mouth",
"c" : "face",
"d" : "nose",
"e" : "tush",
"f" : "breath",
"g" : "pants",
"h" : "shorts",
"i" : "lips",
"j" : "honker",
"k" : "butt",
"l" : "brain",
"m" : "tushie",
"n" : "chunks",
"o" : "hiney",
"p" : "biscuits",
"q" : "toes",
"r" : "buns",
"s" : "fanny",
"t" : "sniffer",
"u" : "sprinkles",
"v" : "kisser",
"w" : "squirt",
"x" : "humperdinck",
"y" : "brains",
"z" : "juice"
}

while True:
    try:
        firstName = input('Please enter your first name: ').lower()
        lastName = input('Please enter your last name: ').lower()
        newLastName = newLastName1[lastName[0]] +  newLastName2[lastName[-1]]
        print(newFirstNames[firstName[0]]," ",newLastName)
        break
    except KeyError:
        print('Enter your real name!!!')