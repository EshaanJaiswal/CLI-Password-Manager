from crypto import Crypto
from storage import DBM
from commands import CommandHandler
from cli import build_parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    crypto = Crypto()
    storage = DBM()
    handler = CommandHandler(crypto, storage)

    if args.command == "add":
        handler.add(args.account, overwrite=args.overwrite)
    elif args.command == "get":
        handler.get(args.account, quiet=args.quiet)
    elif args.command == "list":
        handler.list_accounts()
    elif args.command == "delete":
        handler.delete(args.account)

if __name__ == "__main__":
    main()
