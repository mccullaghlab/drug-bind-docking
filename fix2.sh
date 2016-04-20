#!/bin/bash

for f in /mnt/lustre_fs/users/kavotaw/drugs/mgltools_i86Linux2_1.5.6/MGLToolsPckgs/*/*/*;do sed -i 's/ArrayType/ndarray/g' $f; done
