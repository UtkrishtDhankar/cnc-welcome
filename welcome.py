#! /usr/bin/env python3

import argparse

text = "@{user} I see you're new around here. Welcome! Make sure you read #welcome and message @wizards for problems, and fear their awesome moderator powers. Know, however, that I am the true power holder of this place, but do keep that a secret."


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('user', help='The name of the user to be welcomed.')

    args = parser.parse_args()
    print (args)
    print (text.format(user=args.user))


if __name__ == '__main__':
    main()
