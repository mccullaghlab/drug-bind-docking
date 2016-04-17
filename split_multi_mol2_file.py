#!/mnt/lustre_fs/users/mjmcc/apps/python2.7/bin/python
import os, sys



if __name__ == '__main__':
    import sys
    import getopt


def usage():
    "Print helpful, accurate usage statement to stdout."
    print "Usage: split_multi_mol2_file.py -i filename"
    print
    print "    Description of command..."
    print "         -i     multi_mol2_filename"
    print "    Optional parameters:"
    print "        [-v]    verbose output"


def execute(inFile, outDir, v, vv):

    # initialize required parameters
    multi_mol2_filename = inFile


    #step one: open multiple mol2 file and get all the lines
    fptr = open(multi_mol2_filename)
    alllines = fptr.readlines()
    fptr.close()
    #step two: set up counter for filenames, molecule counter and flag
    molctr = 0
    #inmol = 0
    #step three: process alllines
    in_molecule = False
    for i in range(len(alllines)):
        line = alllines[i]
        #optr.write(line)
        if line.find("@<TRIPOS>MOLECULE")==0: # check for beginning of mol
            if vv: print 'found beginning of molecule ', molctr 
            if in_molecule:
                optr.close()
                if vv: print "closed ", filename
            else:
                in_molecule = True
            zid = alllines[i+1].strip()
            filename = outDir+zid + '.mol2'
            if os.path.exists(filename):
                for i in range(1, 100):
                    filename = outDir+zid + "_" + str(i) + ".mol2"
                    if not os.path.exists(filename):
                        break
            optr = open(filename, 'w')
            molctr += 1
        optr.write(line)
    if v: print 'split %s into %d files' %(multi_mol2_filename, molctr)


        
