#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import argparse
import pathlib
import colorama
from colorama import Fore, Style


def tree(directory: pathlib.Path) -> None:
    print(Fore.RED + f">>> {directory}")
    for path in sorted(directory.rglob("*")):
        d = len(path.relative_to(directory).parts)
        sp = " " * d
        print(Fore.GREEN + Style.BRIGHT + f"{sp} >> {path.name}")
        for new_path in sorted(directory.joinpath(path).glob("*")):
            d = len(new_path.relative_to(directory.joinpath(path)).parts)
            sp = "\t" * d
            print(Fore.BLUE + f"{sp} > {new_path.name}")


def main(command_line: None) -> None:
    colorama.init()
    cur = pathlib.Path.cwd()
    file_parser = argparse.ArgumentParser(add_help=False)

    # Создаем основной парсер командной строки
    parser = argparse.ArgumentParser("tree")

    parser.add_argument(
        "--version", action="version", help="The main parser", version="%(prog)s 0.1.0"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Создаем субпарсер для создания новой папки
    makedir = subparsers.add_parser("mkdir", parents=[file_parser])
    makedir.add_argument("filename", action="store")

    # Субпарсер для удаления папок
    makedir = subparsers.add_parser("rmdir", parents=[file_parser])
    makedir.add_argument("filename", action="store")

    # Субпарсер для создания файлов
    makedir = subparsers.add_parser("touch", parents=[file_parser])
    makedir.add_argument("filename", action="store")

    # Субпарсер для удаления файлов
    makedir = subparsers.add_parser("rm", parents=[file_parser])
    makedir.add_argument("filename", action="store")

    args = parser.parse_args(command_line)

    if args.command == "mkdir":
        directory_path = cur / args.filename
        directory_path.mkdir()
        tree(cur)
    elif args.command == "rmdir":
        directory_path = cur / args.filename
        directory_path.rmdir()
        tree(cur)
    elif args.command == "touch":
        directory_path = cur / args.filename
        directory_path.touch()
        tree(cur)
    elif args.command == "rm":
        directory_path = cur / args.filename
        directory_path.unlink()
        tree(cur)
    else:
        tree(cur)


if __name__ == "__main__":
    main(command_line=None)
