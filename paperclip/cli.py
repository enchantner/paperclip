#!/usr/bin/env python3

import argparse
import os.path

import yaml


def load_config(fname):
    with open(fname, "r") as conf_file:
        return yaml.safe_load(conf_file.read())


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config', dest='config', action='store', type=str,
        help='path to custom config',
        default=os.path.join(os.path.dirname(__file__), "config.yaml")
    )
    return parser


def main():
    parser = build_parser()
    params, other_params = parser.parse_known_args()
    conf = load_config(params.config)
    print(conf)


if __name__ == "__main__":
    main()
