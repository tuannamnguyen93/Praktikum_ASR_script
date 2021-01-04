import os
import argparse
import sys
from text  import levenshtein

parser = argparse.ArgumentParser(description='pynn')
parser.add_argument('--hypo', help='hypothesis', required=True)
parser.add_argument('--ref', help='reference', required=True)

if __name__ == '__main__':
    args = parser.parse_args()

    hypos = {}
    i = 0
    with open(args.hypo, 'r') as f:
        for line in f:
            tokens = line.split()
            uid, hypo = str(i), tokens[0:]
            i+=1
            hypos[uid] = hypo
    err = 0
    l = 0
    n = 0
    n10 = 0
    i = 0
    total_sed = 0
    with open(args.ref, 'r') as f:
        for line in f:
            tokens = line.split()
            uid = str(i)
            i+=1
            ref = tokens
            hypo = hypos[uid]

            sed = levenshtein(hypo, ref)
            if len(ref)!= 0:
                wer = float(sed) / len(ref)
            else:
                continue
            err += sed
            l += len(ref)
            if wer > 0.1: n10 += 1
            n += 1
    wer = float(err) / l
    print('Overall WER: %.4f, Error Utter: %0.4f' % (wer, float(n10)/n))

