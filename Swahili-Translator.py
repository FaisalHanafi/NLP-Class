#Muhammad Syazmi bin Suhaidi 1814573
#Mohamad Faisal Bin Mohd. Hanafi 1915045

from nltk.nltk_contrib.fst.fst import *

class myFST(FST):    
    def recognize(self, iput, oput):

        # insert your codes here
        #self.inp = iput.split()
        #self.outp = oput.split()
        self.inp = list(iput)
        self.outp = list(oput)
        #f.transduce("abc")        
        
        if list(oput) == f.transduce(list(iput)):
            #print(" ".join(f.transduce(iput.split())))        
            return True
        else:
            return False

def write_file(result):
    f = open("Swahili-trans.dat", "a")
    for i in result:
        f.write("".join(i) + "\n")
    f.close()

def mapping(inp, outp):
    if f.recognize(inp, outp):
        result = "accept: " + inp + " --> " + outp
    else:
        result = "reject: " + inp + " --> " + outp
    print(result)
    return result

# or this more verbose way
f = myFST('example')
# first add the states in the FST
for i in range(1,9):
    f.add_state(str(i)) # add states '1' .. '5'

# add one initial state
f.initial_state = '1' 

# add all transitions
f.add_arc('1', '1', ('sifuri'), ('zero'))
f.add_arc('1', '1', ('moja'), ('one'))
f.add_arc('1', '1', ('mbili'), ('two'))
f.add_arc('1', '1', ('tatu'), ('three'))
f.add_arc('1', '1', ('nne'), ('four'))
f.add_arc('1', '1', ('tano'), ('five'))
f.add_arc('1', '1', ('sita'), ('six'))
f.add_arc('1', '1', ('saba'), ('seven'))
f.add_arc('1', '1', ('nane'), ('eight'))
f.add_arc('1', '1', ('tisa'), ('nine'))
f.add_arc('1', '1', ('kumi'), ('ten'))
f.add_arc('1', '1', ('ishrini'), ('twenty'))
f.add_arc('1', '1', ('thalathini'), ('thirty'))
f.add_arc('1', '1', ('arubaini'), ('forty'))
f.add_arc('1', '1', ('hamsini'), ('fifty'))
f.add_arc('1', '1', ('sitini'), ('sixty'))
f.add_arc('1', '1', ('sabini'), ('seventy'))
f.add_arc('1', '1', ('thamanini'), ('eighty'))
f.add_arc('1', '1', ('tisini'), ('ninety'))
f.add_arc('1', '1', ('mia'), ('hundred'))
f.add_arc('1', '1', ('elfu'), ('thousand'))
f.add_arc('1', '1', ('nusu'), ('half'))
f.add_arc('1', '1', ('robo'), ('quarter'))

f.add_arc('1', '1', (' '), (' '))
f.add_arc('1', '8', (' '), (' '))

f.add_arc('1', '2', ('-'), ('-'))
f.add_arc('1', '2', (' '), (' '))

f.add_arc('2', '2', (' '), (' '))
f.add_arc('2', '2', ('na'), ('and'))
f.add_arc('2', '2', ('moja'), ('one'))
f.add_arc('2', '2', ('mbili'), ('two'))
f.add_arc('2', '2', ('tatu'), ('three'))
f.add_arc('2', '2', ('nne'), ('four'))
f.add_arc('2', '2', ('tano'), ('five'))
f.add_arc('2', '2', ('sita'), ('six'))
f.add_arc('2', '2', ('saba'), ('seven'))
f.add_arc('2', '2', ('nane'), ('eight'))
f.add_arc('2', '2', ('tisa'), ('nine'))

f.add_arc('2', '8', (''), (''))

f.add_arc('2', '3', ('-'), ('-'))
f.add_arc('2', '3', (' '), (' '))

f.add_arc('3', '3', ('na'), ('and'))
f.add_arc('3', '3', ('moja'), ('one'))
f.add_arc('3', '3', ('mbili'), ('two'))
f.add_arc('3', '3', ('tatu'), ('three'))
f.add_arc('3', '3', ('nne'), ('four'))
f.add_arc('3', '3', ('tano'), ('five'))
f.add_arc('3', '3', ('sita'), ('six'))
f.add_arc('3', '3', ('saba'), ('seven'))
f.add_arc('3', '3', ('nane'), ('eight'))
f.add_arc('3', '3', ('tisa'), ('nine'))
f.add_arc('3', '3', ('kumi'), ('ten'))
f.add_arc('3', '3', ('ishrini'), ('twenty'))
f.add_arc('3', '3', ('thalathini'), ('thirty'))
f.add_arc('3', '3', ('arubaini'), ('forty'))
f.add_arc('3', '3', ('hamsini'), ('fifty'))
f.add_arc('3', '3', ('sitini'), ('sixty'))
f.add_arc('3', '3', ('sabini'), ('seventy'))
f.add_arc('3', '3', ('thamanini'), ('eighty'))
f.add_arc('3', '3', ('tisini'), ('ninety'))
f.add_arc('3', '3', ('mia'), ('hundred'))
f.add_arc('3', '3', ('nusu'), ('half'))
f.add_arc('3', '3', ('robo'), ('quarter'))

f.add_arc('3', '8', (''), (''))

f.add_arc('3', '4', ('-'), ('-'))
f.add_arc('3', '4', (' '), (' '))

f.add_arc('4', '4', ('na'), ('and'))
f.add_arc('4', '4', ('moja'), ('one'))
f.add_arc('4', '4', ('mbili'), ('two'))
f.add_arc('4', '4', ('tatu'), ('three'))
f.add_arc('4', '4', ('nne'), ('four'))
f.add_arc('4', '4', ('tano'), ('five'))
f.add_arc('4', '4', ('sita'), ('six'))
f.add_arc('4', '4', ('saba'), ('seven'))
f.add_arc('4', '4', ('nane'), ('eight'))
f.add_arc('4', '4', ('tisa'), ('nine'))
f.add_arc('4', '4', ('kumi'), ('ten'))
f.add_arc('4', '4', ('ishrini'), ('twenty'))
f.add_arc('4', '4', ('thalathini'), ('thirty'))
f.add_arc('4', '4', ('arubaini'), ('forty'))
f.add_arc('4', '4', ('hamsini'), ('fifty'))
f.add_arc('4', '4', ('sitini'), ('sixty'))
f.add_arc('4', '4', ('sabini'), ('seventy'))
f.add_arc('4', '4', ('thamanini'), ('eighty'))
f.add_arc('4', '4', ('tisini'), ('ninety'))

f.add_arc('4', '8', (''), (''))

f.add_arc('4', '5', ('-'), ('-'))
f.add_arc('4', '5', (' '), (' '))

f.add_arc('5', '5', ('na'), ('and'))
f.add_arc('5', '5', ('moja'), ('one'))
f.add_arc('5', '5', ('mbili'), ('two'))
f.add_arc('5', '5', ('tatu'), ('three'))
f.add_arc('5', '5', ('nne'), ('four'))
f.add_arc('5', '5', ('tano'), ('five'))
f.add_arc('5', '5', ('sita'), ('six'))
f.add_arc('5', '5', ('saba'), ('seven'))
f.add_arc('5', '5', ('nane'), ('eight'))
f.add_arc('5', '5', ('tisa'), ('nine'))
f.add_arc('5', '5', ('kumi'), ('ten'))
f.add_arc('5', '5', ('ishrini'), ('twenty'))
f.add_arc('5', '5', ('thalathini'), ('thirty'))
f.add_arc('5', '5', ('arubaini'), ('forty'))
f.add_arc('5', '5', ('hamsini'), ('fifty'))
f.add_arc('5', '5', ('sitini'), ('sixty'))
f.add_arc('5', '5', ('sabini'), ('seventy'))
f.add_arc('5', '5', ('thamanini'), ('eighty'))
f.add_arc('5', '5', ('tisini'), ('ninety'))

f.add_arc('5', '8', (''), (''))

f.add_arc('5', '6', ('-'), ('-'))
f.add_arc('5', '6', (' '), (' '))

f.add_arc('6', '6', ('na'), ('and'))
f.add_arc('6', '8', (''), (''))

f.add_arc('6', '7', ('-'), ('-'))
f.add_arc('6', '7', (' '), (' '))

f.add_arc('7', '7', ('na'), ('and'))
f.add_arc('7', '7', ('moja'), ('one'))
f.add_arc('7', '7', ('mbili'), ('two'))
f.add_arc('7', '7', ('tatu'), ('three'))
f.add_arc('7', '7', ('nne'), ('four'))
f.add_arc('7', '7', ('tano'), ('five'))
f.add_arc('7', '7', ('sita'), ('six'))
f.add_arc('7', '7', ('saba'), ('seven'))
f.add_arc('7', '7', ('nane'), ('eight'))
f.add_arc('7', '7', ('tisa'), ('nine'))

f.add_arc('7', '8', (''), (''))

# add final/accepting state(s)
#f.set_final('3')
f.set_final('8')

# use the nltk transduce function
#print(" ".join(f.transduce("a b a b b".split())))

# use the recognize function defined in myFST
#if f.recognize("a b a b b", "1 1 - 1 1"):
inp = ["elfu-mbili", "thalathini-na-saba","embili-elfu","mia-sita-sabini-na-tisa","mia-tano-hamsini-na-mbili"
       ,"elfu-nne-mia-moja-ishrini-na-tatu"]
outp = ["thousand-two", "thirty-and-seven","thousand-two","hundred-six-seventy-and-nine","hundred-five-forty-and-two",
        "thousand-four-hundred-one-twenty-and-three"]

result = []
for i in range(len(inp)):
    result.append(mapping(inp[i], outp[i]))
    
write_file(result)

disp = FSTDisplay(f)
