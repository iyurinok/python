

def rec_power_set(arg):
    if arg == '':
        return [arg]

    ps = rec_power_set(arg[:-1])
    new_ps = []
    for s in ps:
        new_ps.append(s)
        new_ps.append(s + arg[-1])

    return new_ps


def iter_power_set(arg):
    power_set = ['']

    for c in arg:
        new_ps = []

        for subset in power_set:
            new_ps.append(subset)
            subset += c
            new_ps.append(subset)
        power_set = new_ps

    return power_set


def bin_power_set(arg):
    power_set = []
    for bi in range(2 ** len(arg)):
        set = ''
        i = len(arg) - 1
        while bi > 0:
            if bi & 1:
                set = arg[i] + set
            i -= 1
            bi >>= 1

        power_set.append(set)
    return power_set


print iter_power_set("abcd")
print rec_power_set("abcd")
print bin_power_set("abcd")
