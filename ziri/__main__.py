import argparse
from model import add, update, clear, read, remove, list
if __name__ == '__main__':
    parser = argparse.ArgumentParser('A simple diary')
    subparsers = parser.add_subparsers(
        title='Diary action', dest='action', required=True)

    add_parser = subparsers.add_parser(
        'add', help='Add a new diary or add a new entry to an existing diary')
    add_parser.add_argument('date', type=str,
                            help="Date(yyyy-mm-dd)")
    add_parser.add_argument('text', type=str,
                            help="Text you want to add to the diary")
    add_parser.set_defaults(func=add)

    update_parser = subparsers.add_parser(
        'update', help='Update an entire diary')
    update_parser.add_argument('date', type=str,
                               help="Date(yyyy-mm-dd)")
    update_parser.add_argument('text', type=str,
                               help="Text you want to add to the diary")
    update_parser.set_defaults(func=update)

    clear_parser = subparsers.add_parser(
        'clear', help='Clear the contents of a diary')
    clear_parser.add_argument('date', type=str,
                              help="Date(yyyy-mm-dd)")
    clear_parser.set_defaults(func=clear)

    delete_parser = subparsers.add_parser(
        'remove', help='Delete diary')
    delete_parser.add_argument('date', type=str,
                               help="Date(yyyy-mm-dd)")
    delete_parser.set_defaults(func=remove)

    read_parser = subparsers.add_parser(
        'read', help='Read diary')
    read_parser.add_argument('date', type=str,
                             help="Date(yyyy-mm-dd)")
    read_parser.set_defaults(func=read)

    list_parser = subparsers.add_parser(
        'list', help='List your diary entries')
    list_parser.set_defaults(func=list)

    args = parser.parse_args()

    if args.action in ['add', 'update']:
        args.func(args.date, args.text)
    elif args.action in ['clear', 'remove', 'read']:
        args.func(args.date)
    else:
        args.func()
