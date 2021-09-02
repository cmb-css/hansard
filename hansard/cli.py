import argparse

from hansard.retrieve import retrieve


def cli():
    parser = argparse.ArgumentParser()

    parser.add_argument('command', type=str, help='command to execute')
    parser.add_argument('--search', type=str,
                        help='search term', default=None)
    parser.add_argument('--outdir', type=str,
                        help='output directory', default=None)
    parser.add_argument('--start_date', type=str,
                        help='earliest debate',
                        default='01/01/1970')
    parser.add_argument('--end_date', type=str,
                        help='latest debate date',
                        default='31/08/2021')
    parser.add_argument('--page', type=int,
                        help='search result page to start with',
                        default=1)
    args = parser.parse_args()

    print('search term: {}'.format(args.search))
    print('output directory: {}'.format(args.outdir))
    print('start date: {}'.format(args.start_date))
    print('end date: {}'.format(args.end_date))
    print('page: {}').format(args.page)

    if args.command == 'retrieve':
        retrieve(search_term=args.search,
                 outdir=args.outdir,
                 start_date=args.start_date,
                 end_date=args.end_date,
                 page=args.page)
    else:
        print('Unknown command: {}'.format(args.command))
