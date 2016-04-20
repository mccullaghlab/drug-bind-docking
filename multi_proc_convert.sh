#!/bin/bash 
#SBATCH --job-name=adv-multiproc_convert
#SBATCH --output=adv-test.output 
#SBATCH --time=96:00:00 
#SBATCH --nodes=1
#SBATCH --exclusive 
#SBATCH --ntasks-per-node=20

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/gcc-4.9.2/lib64"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/hpcx-v1.2.0-292-gcc-MLNX_OFED_LINUX-2.4-1.0.0-redhat6.6/ompi-mellanox-v1.8/lib"

export PYTHON_EGG_CACHE="./"

me='whoami'
export PYTHONPATH="/mnt/lustre_fs/users/"+me+"/drugs/mgltools_i86Linux2_1.5.6/MGLToolsPckgs"

nproc=20

# create list of ligands and split into number of processors
ls ligands/ > list.dat

tot=`cat list.dat | wc -l`
num=`expr $tot / $nproc`

i=0
j=0

while [ $i -lt $nproc ]
do
i=`expr $i + 1`
j=`expr $j + $num`
head -$j list.dat | tail -$num > lists/list$i.dat
done

k=`expr $tot - $j`
tail -$k list.dat >> lists/list$i.dat

# run python script on each ligand list
i=1
while [ $i -le $nproc ]
do
python convert.py run.cfg $i &
i=`expr $i + 1`
done
wait


#time ./prepare.py run.cfg > preparec.output

