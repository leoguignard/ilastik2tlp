#!/usr/bin/env/python

import argparse

def write_tlp_from_lin_tree(name, lin_tree):
    """
    Write a lineage tree into an understable tulip file
    name : path to the tulip file to create
    lin_tree : lineage tree to write
    properties : dictionary of properties { 'Property name': [{c_id: prop_val}, default_val]}
    """
    nodes=set(lin_tree.keys()).union(set([v for values in lin_tree.values() for v in values]))

    f=open(name, "w")
    inv_lin_tree={v:k for k, vals in lin_tree.iteritems() for v in vals}
    f.write("(tlp \"2.0\"\n")
    f.write("(nodes ")
    id_corres = {}
    for i, n in enumerate(nodes):
        id_corres[n] = i
        f.write(str(i)+ " ")
    f.write(")\n")

    count_edges=0
    for m, ds in lin_tree.iteritems():
        count_edges+=1
        for d in ds:
            f.write("(edge " + str(count_edges) + " " + str(id_corres[m]) + " " + str(id_corres[d]) + ")\n")
    f.write(")")
    f.close()

def main():
    parser = argparse.ArgumentParser(description='Convert ilastik manual lineage into tulip lineage.')
    parser.add_argument('-i', '--input', help='input ilastik .csv file', required=True)
    parser.add_argument('-o', '--output', help='output tulip file (has to end with .tlp)', required=True)
    parser.add_argument('-at', '--added-time', help='number of added time points at the end (default: 1)', type = int, default = 1, required=False)
    parser.add_argument('-pb', '--prolonge-branches',
            help=('whether or not the branches will be continued to end at the same time point (0=No, 1=Yes, default: No)'),
            type = int, default = 0, required=False)
    parser.add_argument('-mt', '--max-time',
        help='last time point to consider, if -1 all time points are (default: -1)', type = int, default = -1, required=False)
    
    args = parser.parse_args()

    f = open(args.input)
    lines = f.readlines()
    f.close()

    succ = {}
    pred = {}
    time_end = {}
    time_start = {}
    for l in lines[1:]:
        split_l = l.split(',')
        t = int(split_l[0])
        id_ = int(split_l[1])
        d1 = int(split_l[2])
        d2 = int(split_l[3])
        if args.max_time == -1 or t <= args.max_time:
            succ[(id_, t)] = [(d1, t+1), (d2, t+1)]
            pred[(d1, t+1)] = [(id_, t)]
            pred[(d2, t+1)] = [(id_, t)]
            time_end[id_] = t
            time_start[d1] = t+1
            time_start[d2] = t+1
    final_time = max(time_start.values()) + args.added_time

    for c, t_s in time_start.iteritems():
        if args.prolonge_branches == 1:
            t_e = time_end.get(c, final_time)
        else:
            t_e = time_end.get(c, time_start[c] + args.added_time)
        for t_i in range(t_s, t_e):
            succ[(c, t_i)] = [(c, t_i + 1)]
            pred[(c, t_i + 1)] = [(c, t_i)]


    write_tlp_from_lin_tree(args.output, succ)


if __name__ == '__main__':
    main()
