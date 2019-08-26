#!/usr/bin/python3
import re


class Parser(object):
    pattern = re.compile(r'"(?P<a>.+?)" -> "(?P<b>.+?)"')

    def __init__(self):
        self.nodes = set()
        self.deps = set()

    @property
    def roots(self):
        return self.nodes - self.deps

    def add(self, line):
        match = self.pattern.match(line)
        if match is None:
            return
        self.nodes.add(match.group('a'))
        self.deps.add(match.group('b'))

    def __call__(self, lines):
        for line in lines:
            self.add(line)
        return self.roots

    def __str__(self):
        return '\n'.join(sorted(self.roots))


def main_stdin():
    parser = Parser()
    try:
        while True:
            parser.add(input())
    except EOFError:
        pass
    print(parser)


def main_file(filename):
    with open(filename) as f:
        parser = Parser()
        parser(f)
        print(parser)


def main():
    from sys import argv
    if len(argv) == 1:
        main_stdin()
    else:
        main_file(argv[1])


if __name__ == '__main__':
    main()
