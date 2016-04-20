#drugPy.py

To run this script, use:
    
    $ python drugPy.py run.cfg <options>
    
1. Edit <configFile> to reflect the relative paths of the .mol2 <library> file and the .pdb <receptor> file.
2. Execute  $ python drugPy.py run.cfg <options>
   
   Options:

	-v		verbose console output
	-vv		all debug info and verbose console output
	-n 		skip splitting of mol2 library if this step has been performed once already (splits by default)
