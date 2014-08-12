class List:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __iter__(self):
        x = self
        while x:
            yield x
            x = x.next

    def __len__(self):
        return 1 + len(self.next) if self.next else 1

    def __str__(self):
        return "->".join(map(str, [x.data for x in self]))


def subtract_rec(list):
    def subtract_rec_util(first, last, n):
        if last is None:
            return first, n
        (first, n) = subtract_rec_util(first, last.next, n)

        if n > 0:
            first.data -= last.data

        return first.next, n - 1

    subtract_rec_util(list, list, len(list) / 2)
    return list


def reverse(current):
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def subtract(llist):
    slow, fast = llist, llist
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    first = llist
    second = slow.next
    slow.next = None

    rev_second = reverse(second)
    second = rev_second

    while True:
        first.data -= second.data
        if first.next and second.next:
            first = first.next
            second = second.next
        else:
            break

    slow.next = reverse(rev_second)

    return llist


llist = List(5, List(4, List(3, List(2, List(1, None)))))
llist = List(6, llist)

print llist
print len(llist)

print subtract_rec(llist)


