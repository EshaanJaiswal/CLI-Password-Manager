import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Simple CLI password manager")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new account password")
    p_add.add_argument("account", help="Account name")
    p_add.add_argument("--overwrite", action="store_true", help="Overwrite if exists")

    p_get = sub.add_parser("get", help="Get a password")
    p_get.add_argument("account", help="Account name")
    p_get.add_argument("--quiet", action="store_true", help="Only print the password")

    sub.add_parser("list", help="List stored accounts")

    p_del = sub.add_parser("delete", help="Delete an account")
    p_del.add_argument("account", help="Account name")

    return parser
