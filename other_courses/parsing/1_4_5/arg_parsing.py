import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Quiet one')
    parser.add_argument('name')
    parser.add_argument('-s', '--surname')
    parser.add_argument('-c', '--city', choices=['C', 'M', 'S', 'A'])
    parser.add_argument('-m', '--murmur', action='store_true')
    args = parser.parse_args()
    print(args)