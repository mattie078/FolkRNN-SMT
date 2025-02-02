from __future__ import print_function

import os
import sys
import time
import importlib
import cPickle as pickle

from folk_rnn_lobotomized import Folk_RNN
# from folk_rnn import Folk_RNN
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('metadata_path')
parser.add_argument('--rng_seed', type=int)
parser.add_argument('--temperature', type=float)
parser.add_argument('--ntunes', type=int, default=1)
parser.add_argument('--seed')
parser.add_argument('--terminal', action="store_true")
parser.add_argument('--nobars', action="store_true")

args = parser.parse_args()

metadata_path = args.metadata_path
rng_seed = args.rng_seed
temperature = args.temperature
ntunes = args.ntunes
seed = args.seed
nobars = args.nobars

print('seed', seed)

with open(metadata_path, "rb") as f:
    metadata = pickle.load(f)

config = importlib.import_module('configurations.%s' % metadata['configuration'])

# samples dir
if not os.path.isdir('samples'):
        os.makedirs('samples')
target_path = "samples/%s-s%d-%.2f-%s.txt" % (
    metadata['experiment_id'], rng_seed, temperature, time.strftime("%Y%m%d-%H%M%S", time.localtime()))

if config.one_hot:
    config.embedding_size = None

folk_rnn = Folk_RNN(
    metadata['token2idx'],
    metadata['param_values'], 
    config.num_layers, 
    config.rnn_size,
    config.grad_clipping,
    config.dropout, 
    config.embedding_size, 
    rng_seed, 
    temperature
    )
folk_rnn.seed_tune(seed)
for i in xrange(ntunes):
    tune = 'X:{}\n{}\n'.format(i, folk_rnn.compose_tune(nobars))
    if args.terminal:
        print(tune)
    else:
        with open(target_path, 'a+') as f:
            f.write(tune)
        print('Saved to {}'.format(target_path))
    
    
