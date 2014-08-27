__author__ = 'e21349'


def combination(arg):
    if not arg:
        return ['']

    result = []
    for i, c in enumerate(arg):
        result.append(c)
        for postfix in combination(arg[:i] + arg[i+1:]):
            new_word = c + postfix
            if result[-1] != new_word:
                result.append(new_word)
    return result


print combination('abc')
