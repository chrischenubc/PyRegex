def matchOne(pattern, text):
    #Any text matches an empty string
    if not pattern:
        return True
    #if a pattern is not empty, but the text is empty
    #return False
    if not text:
        return False
    #if the pattern is '.', a wildcard, return True
    if pattern == '.':
        return True
    return pattern == text


def match(pattern, text):
    #if pattern is an empty string
    if not pattern:
        return True
    if pattern == '$' and text == '':
        return True
    if len(pattern) > 1 and pattern[1] == '?':
        return matchQuestion(pattern,text)
    if len(pattern) > 1 and pattern[1] == '*':
        return matchStar(pattern,text)
    return matchOne(pattern[0],text[0]) and match(pattern[1:], text[1:])

def matchQuestion(pattern,text):
    if not text and len(pattern) == 2:
        return True
    elif not text:
        return False

    if matchOne(pattern[0],text[0]):
        if match(pattern[2:],text[1:]):
            return True
    else:
        return match(pattern[2:],text)

def matchStar(pattern, text):
    if not text and len(pattern) == 2:
        return True
    elif not text:
        return False
    if matchOne(pattern[0],text[0]):
        if match(pattern,text[1:]):
            return True
    else:
        return matchOne(pattern[2:],text)


def search(pattern, text):
    if pattern[0] == '^' and len(pattern) > 1:
        return match(pattern[1], text)
    if pattern[0] != '?' and len(text) > 1:
        if not matchOne(pattern[0],text[0]):
            return search(pattern,text[1:])

    return match(pattern, text)