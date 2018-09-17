#! /usr/bin/env python

import argparse


def box_detection(input_dir, output_dir):
    # Implement your logic to detect boxes here.
    # You can choose to implement it in a different class and
    # import it here.
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lets detect boxes')
    parser.add_argument('input_directory', help='Location of input images')
    parser.add_argument('output_directory', help='Location of output images')
    args = parser.parse_args()
    box_detection(input_dir=args.input_directory,
                  output_dir=args.output_directory)
