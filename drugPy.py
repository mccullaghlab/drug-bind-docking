'''
Input info:		

Protein XYZ		--------------		---------------		-------------		Drug | KI  |Ligand
Binding			|	Rigid	  | x%	|	Flexible  | y%	|	Thermo	|		-----|-----|-------
	Pocket	-->	|	Docking	  |	-->	|	Docking	  | -->	|	Integr	| -->		 |     |
Drug DB			--------------		---------------		-------------			 |	   |


'''
import sys
import os
import numpy
from split_mol2_convert_receptor import parseConfigFile
from split_mol2_convert_receptor import split_mol2

configFile = ""
flexDockingCriteria = []
thermIntegCriteria = []
results = [[],[],[]]
inProtein = []
bindingPocket = []
drugDb = []
v = False
vv = False

# Give program usage
def usage():
	print("    drugPy Usage\n\n\t$ python drugPy.py <config file> <options>")
	print("\n\t -v\t\tverbose console output\n\t-vv\t\tall debug info + verbose console output\n")

# Check input for selected options
def options():
	global v, vv
	if ((len(sys.argv) != 2) & (len(sys.argv) != 3)):
		usage()
	elif (len(sys.argv) == 3):
		if (sys.argv[2] == "-v"):
			v = True
		elif (sys.argv[2] == "-vv"):
			v = True
			vv = True
	return True

# Establish that a config file is present
def checkConfig():
	global configFile
	if (len(sys.argv) > 1):
		configFile = sys.argv[1]
		if v:
			print ("Config file: {}".format(configFile))
		return True
	else:
		print ("No config file given.")
		return False

# Parse config file for program data
def getConfigData():
	options()
	if (checkConfig()):
		if vv:
			print("Reading in config data...")
		# Get config data
		parseConfigFile(configFile, vv)
		split_mol2(v, vv)
		if vv:
			print("Config data read successfully.")
		return True
	else:
		return False

#def prepareData():

# Execute rigid docking sequence
def rigidDocking():
	print("Rigid Docking...")
	# Apply rigid docking
	print("Rigid Docking applied.")

# Execute flexible docking sequence
def flexibleDocking(flexDockingCriteria):
	print("Flexible Docking...")
	# Apply flexible docking
	print("Flexible Docking applied.")

# Execute thermodynamic integration sequence
def thermoIntegration(thermIntegCriteria):
	print("Thermodynamic Integration...")
	# Apply thermodynamic integration
	print("Thermodynamic Integration appied.")

# Exectue main drugPy sequence
def main():
	if (getConfigData()):
		rigidDocking()
		flexibleDocking(flexDockingCriteria)
		thermoIntegration(thermIntegCriteria)

main()