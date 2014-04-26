"""Functions to parse different things"""

def parse_delim(fname, delim="\n", stripvals = True):
    value = ""
    with open(fname, "r") as f:
        value = f.read()
    tokens = value.split(delim)
    if stripvals:
        for i, val in enumerate(tokens):
            tokens[i] = val.strip()
    print "tokens",tokens
    return tokens

def parse_text(fname, stripvals = True):
    with open(fname, "r") as f:
        return get_tokens(f.read())

def check_periods(builder):
    check = ["Mr.","Mrs.", "Ms.", " .", "No."]

    for elem in check:
        if builder.endswith(elem):
            return True
    return False

def process_string(string):
    space = ['\n','\r', '--']
    unwanted = ['_','"','[',']']
    for elem in space:
        string = string.replace(elem, ' ')
    for elem in unwanted:
        string = string.replace(elem, '')
    return string[:-1].strip()

def get_tokens(complete_file):
    #starting sentence
    builder = ""
    ##completed sentences
    sentences = []
    #go through each character
    check = False
    internal_quote = False
    sp = False
    index = 0
    for c in complete_file:
        index += 1
        #add it
        builder = builder + c
        #if it is a quote, handle options
        if c == '"':
            #if it was preceded by a checked sentence-ender, end sentence
            if sp:
                #check if it was at then end of a quote or not
                #print "checking"
                endindex = index+20
                if index+20 > len(complete_file):
                    endindex = len(complete_file)
                #print endindex
                temp = complete_file[index+1:endindex]
                #print temp
                next_word = temp.strip().split()[0]
                #print next_word
                if next_word != next_word.lower():
                    #print "appended"
                    sp = False
                    sentences.append(process_string(builder))
                    builder = ""
            #if it wasn't, it's part of an internal quote, continue
            if check:
                check = False
            #if it was the first quote, check for the end quote before finishing
            else:
                check = True
        #else if c =="'":
        #    if check:
        #        if internal_quote:
        #            internal_quote = False
        #        else:
        #            internal_quote = True
        #if we expected a quote to end the quoted sentence, but there isn't one
        #we have the end of a sentence contained in the quote, continue
        else:
            if sp:
                sp = False
        #sentence enders
        if c == '.' or c == '?' or c == '!':
            #if inside a quote, check for end quote
            if check:
                sp = True
            # otherwise you have a sentence
            else:
                if len(builder) < 5 or check_periods(builder):
                    continue
                sentences.append(process_string(builder))
                builder = ""
    builder = process_string(builder)
    if builder !="": # and builder != '!' and builder != '.' and builder != '?':
        sentences.append(builder)
    return sentences

def remove_duds(start_tokens):
    for elem in start_tokens:
        #remove elements that don't start with a capital letter
        if elem[0] == elem[0].lower():
            #prt(sorted(elem))
            if elem[0] == "'" and len(elem) > 1:
                if elem[1] != elem[1].lower():
                    continue
            del elem
    return start_tokens
