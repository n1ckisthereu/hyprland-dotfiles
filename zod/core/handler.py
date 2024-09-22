from argparse import Namespace
from .config import cfg_bg


def handler(args: Namespace):
    if args.action == "cfg":
        bg = cfg_bg()

        if args.dir:
            bg.update_dir(args.dir)

        if args.updatebg_cmd:
            bg.updatebg_cmd(args.updatebg_cmd)

    elif args.action == "bg":
        print(args)
        if args.list_bg and not any([args.name, args.mode]):
            pass
        else:
            print("argument list does not support other arguments")
