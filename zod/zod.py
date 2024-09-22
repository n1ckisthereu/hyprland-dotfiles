#!/usr/bin/python3

import argparse
from core.handler import handler


def trigger_handler():
    parser = argparse.ArgumentParser(
        description="zod is simple cli to to manage my dotfiles"
    )

    parser.add_argument("-s", "--skip", type=int, help="skip itens", default=0)
    parser.add_argument("-t", "--take", type=int, help="take itens", default=10)
    parser.add_argument("-c", "--count", action="store_true", help="count itens")

    subparser = parser.add_subparsers(dest="action", help="your action")

    # database commands
    setp = subparser.add_parser(
        "cfg",
        help="set content in database",
    )

    setp.add_argument("-d", "--dir", help="set your wallpaper folder")
    setp.add_argument("-uc", "--updatebg-cmd", help="define your wallpaper command")

    # background subcommands
    bgp = subparser.add_parser(
        "bg", help="define your background and system color schema"
    )

    bgp.add_argument(
        "-l", "--list", action="store_true", help="list avaliable backgrounds"
    )
    bgp.add_argument("-n", "--name", help="name of your wallpaper")

    bgp.add_argument(
        "-m",
        "--mode",
        choices=["dark", "light"],
        help="your system style",
        default="dark",
    )

    handler(parser.parse_args())


def main():
    trigger_handler()


if __name__ == "__main__":
    main()
