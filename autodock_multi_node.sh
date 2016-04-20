#!/bin/bash 
#SBATCH --job-name=advr-multiproc-zinc98
#SBATCH --output=adv-full.outpu2
#SBATCH --time=96:00:00 
#SBATCH --nodes=4
#SBATCH --exclusive 
#SBATCH --ntasks-per-node=20

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/gcc-4.9.2/lib64"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/software/usr/hpcx-v1.2.0-292-gcc-MLNX_OFED_LINUX-2.4-1.0.0-redhat6.6/ompi-mellanox-v1.8/lib"

export PYTHON_EGG_CACHE="./"

#export PYTHONPATH="/mnt/lustre_fs/users/kavotaw/drugs/mgltools_i86Linux2_1.5.6/MGLToolsPckgs"

#time ./Traj_writing.py ../../../../../AMBER_ssrna_adp_pi/truncated.pdb ../../../../../ 7system_backbone.dcd > traj_writing.output

#time ./RMSD.avg_structures.py ../../../../Avg_structure/ reference_structure.pdb 7system_backbone.dcd > rmsd_calc.output

#time bash VS02.bash conf.txt > autodock1.output
#for f in ligands/*.pdbqt; do  b=`basename $f .pdbqt`; echo Processing ligand $b; mkdir -p data03
#srun -N3 -n60 vina --config conf.txt --ligand $f --out data03/$f.pdbqt --log data03/$f.txt --cpu 60 
#srun -N3 -n60 vina --config conf.txt --ligand ligands/*.pdbqt --out data03/$f.pdbqt --log data03/$f.txt --cpu 60 
#./vina --config conf.txt --ligand $f --out data03/$f.pdbqt --log data03/$f.txt
#done
#wait
i=1
while [ $i -le 4 ]
do
./autodock_multi_node.py $i &
i=`expr $i + 1`
done
wait

#result analysis
cd data03/ligands_energies
grep "   1 " *.txt | cut -c1-100,150-200 > ../result.txt
#cat result.txt | sort
sort -k 3,3 ../result.txt > ../result_sorted.txt
