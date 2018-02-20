#!/usr/bin/env python3

import argparse
import os


def _parse_args():
    # type: () -> object
    parser = argparse.ArgumentParser(description='''
    This is the main argument parser for the hyp3r0pt toolkit
    ''')
    return parser.parse_args()

def _main():
    args = _parse_args()
    print(args)


if __name__ == '__main__':
    _main()
