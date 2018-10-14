#!/usr/bin/python
from sys import stdin, stdout

def analyse_prob(expression):
    return expression


def prob(nb_line):
    res = ""
    listres = []
    while nb_line != 0:
        expression = stdin.readline()
        #analyse_template(expression).split(' ')
        listres.append(analyse_prob(expression))
        nb_line -= 1
    res = res.join(listres)
    stdout.write(res)


def main():
    analyse_prob(1)

if __name__ == "__main__":
    main()

