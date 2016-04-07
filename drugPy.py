'''
Input info:		

Protein XYZ		--------------		---------------		-------------		Drug | KI  |Ligand
Binding			|	Rigid	  | x%	|	Flexible  | y%	|	Thermo	|		-----|-----|-------
	Pocket	-->	|	Docking	  |	-->	|	Docking	  | -->	|	Integr	| -->		 |     |
Drug DB			--------------		---------------		-------------			 |	   |


'''
import sys
import numpy

configFile = ""
flexDockingCriteria = []
thermIntegCriteria = []
results = [[],[],[]]
inProtein = []
bindingPocket = []
drugDb = []

def checkConfig(configFile):
	if (len(sys.argv) > 1):
		configFile = sys.argv[1]
		print ("Config file: {}".format(configFile))
		return True
	else:
		print ("No config file given.")
		return False

def getConfigData(configFile):
	if (checkConfig(configFile)):
		print("Reading in config data...")
		# Get config data
		print("Config data read successfully.")
		return True
	else:
		return False

def rigidDocking():
	print("Rigid Docking...")
	# Apply rigid docking
	print("Rigid Docking applied.")

def flexibleDocking(flexDockingCriteria):
	print("Flexible Docking...")
	# Apply flexible docking
	print("Flexible Docking applied.")

def thermoIntegration(thermIntegCriteria):
	print("Thermodynamic Integration...")
	# Apply thermodynamic integration
	print("Thermodynamic Integration appied.")

def main():
	if (getConfigData(configFile)):
		rigidDocking()
		flexibleDocking(flexDockingCriteria)
		thermoIntegration(thermIntegCriteria)

main()