#!/usr/bin/env python

import couchdb
import argparse
import os
import yaml

import LIMS2DB.utils as lutils

def main(args):

    with open(os.path.expanduser('~/opt/config/post_process.yaml')) as conf_file:
        conf=yaml.load(conf_file)
    couch=lutils.setupServer(conf)
    db=couch['projects']
    view=db.view('samples/customer_names')
    d=None
    for row in view[args.project]:
        d=row.value

    if not d:
        print "Project not found"
        return 0

    print '<table class="table table-striped">'
    print '<tr><th>NGI Name</th><th>Customer Name</th></tr>'
    for sample in sorted(d.keys()):
        print "<tr><td>{}</td><td>{}</td></tr>".format(sample, d[sample])

    print "</table>"

if __name__ == "__main__":

    desc = ("Prints internal sample names and customer names side by side")
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-p', '--project', dest="project",
                        help=('print samples for the given project'))
    args=parser.parse_args()
    main(args)

