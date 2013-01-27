import sys

def usage(progName):
	print "\tUsage: python " + progName + " oldHeader.h newHeader.h"

def collectThings(filename):
	file = open(filename,'r')
	methods = []
	variables = []
	properties = []
	lines = file.readlines()
	incomment = False
	for line in lines:
		commentIndex = 0
		try:
			commentIndex = line.index("//")
			line = line[:commentIndex]
		except:
			pass
		if not incomment:
			try:
				line.index("/*")
				incomment = True
			except:
				pass
		if incomment:
			try:
				line.index("*/")
				incomment = False
				continue
			except:
				pass
		if incomment:
			continue
		#line = line.replace(" ", "")
		if  "#" in line:
			continue
		if "-" in line:
			methods.append(line.strip())
			continue
		if "+" in line:
			methods.append(line.strip())
			continue
		if "@property" in line:
			properties.append(line.strip())
			continue
		if "@" in line:
			continue
		if ";" in line:
			variables.append(line.strip())
			continue
	return [methods, variables, properties]

def main():
	if len(sys.argv) < 2:
		usage(sys.argv[0])
		return
	file1 = collectThings(sys.argv[1])
	file2 = collectThings(sys.argv[2])
	file1methods = file1[0]
	file1variables = file1[1]
	file1properties = file1[2]
	file2methods = file2[0]
	file2variables = file2[1]
	file2properties = file2[2]
	for method in file1methods:
		if not method in file2methods:
			print "Method: " + method + " has been removed from the new implementation"
	for method in file2methods:
		if not method in file1methods:
			print "Method: " + method + " has been added to the new implementation"
	for variable in file1variables:
		if not variable in file2variables:
			print "Variable: " + variable + " has been removed from the new implementation"
	for variable in file2variables:
		if not variable in file1variables:
			print "Variable: " + variable + " has been added to the new implementation"
	for proprty in file1properties:
		if not proprty in file2properties:
			print "Property: " + proprty + " has been removed from the new implementation"
	for proprty in file2properties:
		if not proprty in file1properties:
			print "Property: " + proprty + " has been added to the new implementation"


if __name__ == "__main__":
    main()