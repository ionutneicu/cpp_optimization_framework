#!/usr/bin/python3

import sys
import os


def main():
        with open('O1O0diff.txt', 'r') as f_object:
          word_lst = f_object.read().split()
          print( ' '.join(word_lst) )


if __name__ == "__main__" :
    main()
