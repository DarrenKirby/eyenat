import sys

import argparse

import user
import taxon
import observation


def process_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", choices=["taxon", "obs", "user"],
                        help="Specify which data to retrieve")
    parser.add_argument("-n", "--number", type=int, default=30,
                        help="The number of records to fetch")
    parser.add_argument("-t", "--taxon", help="The taxon name to search")
    parser.add_argument("-i", "--id", help="ID number")
    args = parser.parse_args()
    return args


def taxon_search(args):
    th = taxon.TaxonData(args.id)
    print(dir(th))
    return


def user_search(args):
    uh = user.UserData(args.id)
    print(dir(uh))
    return


def obs_search(args):
    oh = observation.ObservationData(args.id)
    print(th)
    return


args = process_args()

if args.mode == "taxon":
    taxon_search(args)
    exit(0)
elif args.mode == "obs":
    obs_search(args)
    exit(0)
elif args.mode == "user":
    user_search(args)
    exit(0)
else:
    print("Nothing to do...")
    exit(0)
