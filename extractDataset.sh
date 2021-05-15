#! /bin/bash

read -p "Network Name: " netname

# make networks dir if doesnt already exist and move into it
mkdir -p Networks
cd Networks

# TODO: directly download these with a wget to save even compressed data in the git
# extract from compressed data dir
tar -xvf ../Compressed_Networks/download.tsv.$netname.tar.bz2

## remove header entry from edgelist for networkx
cd $netname
FILE=out.$netname
tail -n +2 "$FILE" > "$FILE.tmp" && mv "$FILE.tmp" "$FILE"