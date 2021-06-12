#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import argparse


class Main:
    def main(self, args):
        self.execute()

    def execute(self):
        return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--version',
        action='version', version=f'{__version__}'
    )
    parser.add_argument('--option', default='option')
    Main().main(parser.parse_args())
