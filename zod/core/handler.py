from argparse import ArgumentParser, Namespace
from typing import Dict
from .config import cfg_bg
from .theme import theme


def handler(args: Namespace, subparser: Dict[str, ArgumentParser]):
    try:
        current_subparser = subparser[args.action]

        user_provided = [
            action.dest
            for action in current_subparser._actions
            if action.dest != "help" and getattr(args, action.dest) != action.default
        ]
    except Exception:
        user_provided = []

    if args.action == "cfg":
        bg = cfg_bg()

        if args.dir:
            bg.update_dir(args.dir)

        if args.updatebg_cmd:
            bg.updatebg_cmd(args.updatebg_cmd)

        if args.append_app:
            if "remove_app" in user_provided:
                print("you cannot use argument remove app with append")
            else:
                app, sig = args.append_app.split(",")
                bg.add_app_reload(app, sig)

        if args.remove_app:
            if "append_app" in user_provided:
                print("you cannot use argument append app with remove")
            bg.remove_app_reload(args.remove_app)

    elif args.action == "bg":
        theme_manager = theme()

        if args.name:
            theme_manager.gen_full(args.name, args.mode)
            exit(0)

        if args.list and len(user_provided) == 1:
            print(*theme_manager.available(), sep="\n")
        else:
            print("argument list does not support other arguments")
