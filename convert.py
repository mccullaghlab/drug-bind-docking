#!/mnt/lustre_fs/users/mjmcc/apps/python2.7/bin/python
import os
import sys
import numpy
#import rdkit

def ParseConfigFile(cfg_file):
         global inp_lig_dir,lig_file,inp_rec_dir,rec_file,inp_bin_dir,cx,cy,cz,sx,sy,sz,num_modes
         f = open(cfg_file)
         for line in f:
                 # first remove comments
                 if '#' in line:
                         line, comment = line.split('#',1)
                 if '=' in line:
                         option, value = line.split('=',1)
                         option = option.strip()
                         value = value.strip()
                         d = line.split()
                         print "Option:", option, " Value:", value
                         # check value
                         if option.lower()=='ligand_directory':
				 inp_lig_dir = value
                         elif option.lower()=='ligand_file':
                                 lig_file = value
                         elif option.lower()=='receptor_directory':
                                 inp_rec_dir = value
                         elif option.lower()=='receptor_file':
                                 rec_file = value
                         elif option.lower()=='binary_directory':
                                 inp_bin_dir = value
                         elif option.lower()=='center_x':
                                 cx = value
                         elif option.lower()=='center_y':
                                 cy = value
                         elif option.lower()=='center_z':
                                 cz = value
                         elif option.lower()=='size_x':
                                 sx = value
                         elif option.lower()=='size_y':
                                 sy = value
                         elif option.lower()=='size_z':
                                 sz = value
                         elif option.lower()=='num_modes':
				num_modes = value
                         else:
                                 print "Option:", option, " is not recognized"

cfg_file = sys.argv[1]
ParseConfigFile(cfg_file)

# Run Babel (sdf -> mol2)
#os.system("./../babel -i sdf library/* -o mol2 library/*")

# Split mol2 (mol2* -> ligands/.mol2)
#os.system("cd ligands; ./"+inp_bin_dir+"split_multi_mol2_file.py -i ../"+inp_lig_dir+lig_file+";\ls *.mol2 > ../ligand.list")

# Prepare ligands (ligands/.mol2 -> ligands/.pdbqt)
#os.system("cd ..")
#ligands = "ligands/"
#for directory, subdirectories, files in os.walk(ligands):
#    for file in files:
nf = open("lists/list"+sys.argv[2]+".dat","r")
for line in nf:
	d = line.split()
	print d[0]
	os.system("cd ligands/; ./"+inp_bin_dir+"prepare_ligand4.py -l "+d[0]+" -d ../ligand_dict.py")

# Prepare receptor (receptor/.pdb -> receptor/.pdbqt)
#os.system("cd "+inp_rec_dir)
#os.system(inp_bin_dir+"./"+inp_bin_dir+"prepare_receptor4.py -r ../"+inp_rec_dir+rec_file+" -A hydrogens")

