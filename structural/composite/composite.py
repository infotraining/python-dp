
class Leaf:
    def __init__(self, name):
        self.name = name

    def display(self, alignment = 0):
        print(' ' * alignment + '+ ' + self.name)


class Composite(Leaf):

    def __init__(self, name, *children):
        super().__init__(name)
        self.children = [] + list(children)

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def display(self, alignment = 0):
        super().display(alignment)
        for child in self.children:
            child.display(alignment + 2)

    def __iter__(self):
        for child in self.children:
            yield child
            if isinstance(child, Composite):
                yield from child


def main():

    root = Composite('root')
    root.add_child(Leaf('Leaf A'))
    root.add_child(Leaf('Leaf B'))

    xa = Composite('Composite XA')
    xa.add_child(Leaf('Leaf C'))
    xa.add_child(Leaf('Leaf D'))

    xb = Composite('Composite XB')
    xb.add_child(Leaf('Leaf E'))

    xa.add_child(xb)

    root.add_child(xa)
    root.add_child(Leaf('Leaf F'))

    root.display()

    root.remove_child(xa)

    print("-" * 40)

    root.display()

    print("-" * 40)

    for child in root:
        print('{} - {}'.format(child, child.name))

    print("-" * 40)

    C = Composite
    L = Leaf

    root2 = C('root2',
                L('l1'),
                L('l2'),
                C('c1',
                    L('l3'),
                    L('l4'),
                    C('c2',
                      L('l5'))),
                L('l5'),
                L('l6')
              )

    root2.display()

    print([n.name for n in root2])


if __name__ == '__main__':
    main()