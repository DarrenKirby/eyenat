import argparse

import usrmode


def process_args():
    parser = argparse.ArgumentParser(prog='eyenat', description='CLI for iNaturalist')

    parser.add_argument('mode', choices=['tax', 'obs', 'usr', 'cnt'],
                        help='specify which mode to use')

    parser.add_argument('-u', '--user', help='specify username or userid number')
    # parser.add_argument()
    # parser.add_argument()
    # parser.add_argument()
    # parser.add_argument()
    # parser.add_argument()
    # parser.add_argument()
    args = parser.parse_args()
    return args


def taxon_search(args):
    th = taxon.TaxonData(args.id)
    print(dir(th))
    return


def obs_search(args):
    oh = observation.ObservationData(args.id)
    print(th)
    return


args = process_args()

if args.mode == 'tax':
    taxon_search(args)
    exit(0)
elif args.mode == 'obs':
    obs_search(args)
    exit(0)
elif args.mode == 'usr':
    usrmode.init_user_search(args)
    exit(0)
else:
    print("Nothing to do...")
    exit(0)
