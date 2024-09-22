#!/usr/bin/python3

import argparse
from core.handler import handler


def trigger_handler():
    parser = argparse.ArgumentParser(
        description="zod is simple cli to to manage my dotfiles"
    )

    subparser = parser.add_subparsers(dest="action", help="your action")

    # database commands
    setp = subparser.add_parser(
        "cfg",
        help="set content in database",
    )

    setp.add_argument("-d", "--dir", help="set your wallpaper folder")
    setp.add_argument("-u", "--updatebg-cmd", help="define your wallpaper command")
    setp.add_argument(
        "-a", "--append-app", help="append item to reload list, use this format app,sig"
    )
    setp.add_argument("-r", "--remove-app", help="remove app from reload list")

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

    subparsers = {"cfg": setp, "bg": bgp}
    handler(parser.parse_args(), subparsers)


def main():
    trigger_handler()


if __name__ == "__main__":
    main()
