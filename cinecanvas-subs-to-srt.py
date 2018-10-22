#!/usr/bin/env python3

# Copyright (c) 2018 by Jarno Elonen <elonen@iki.fi>
# Licensed under the MIT license. See LICENSE for details.

from lxml import etree
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Convert CineCanvas DCP subtitle XML to SRT.')
    parser.add_argument("infile", help="CineCanvas XML file to read")
    args = parser.parse_args()

    with open(args.infile, 'rb') as myfile:
        xml_bin = myfile.read()
        root = etree.fromstring(xml_bin)
        for e in root.findall('.//Subtitle'):
            print( e.get('SpotNumber'))
            time_in, time_out = e.get('TimeIn'), e.get('TimeOut')
            in_parts = time_in.split(':')
            out_parts = time_out.split(':')
            assert(len(in_parts) == 4)
            assert(len(out_parts) == 4)
            #print(time_in, ' --> ' , time_out)
            in_parts[-1] = '%03d' % (int(in_parts[3]) * 4) # convert 4 msec CineCanvas "ticks" to milliseconds
            out_parts[-1] = '%03d' % (int(out_parts[3]) * 4)
            print( ':'.join(in_parts[:3]) + ',' + in_parts[3] + ' --> ' + ':'.join(out_parts[:3]) + ',' + out_parts[3]  )
            for t in e.findall('.//Text'):
                if t.text is not None:
                    print(t.text, end='')
                for f in t.findall('.//Font'):
                    if f.text is not None:
                        if f.get('Italic') == 'yes':
                            print( '<i>' + f.text + '</i>', end='')
                        else:
                            print(f.text, end='')
                print('') # linefeed
            print('')
