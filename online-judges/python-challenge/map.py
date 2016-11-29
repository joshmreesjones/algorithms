# K -> M
# O -> Q
# E -> G
# Go forward two spots

# character codes go from 97 (a) to 122 (z)


def translate(input_string):
	output_string = ""
	for character in input_string:
		# don't change non-alphanumeric characters
		if (ord(character) < 97 or ord(character) > 122):
			output_string += character
			continue
	
		output_string += chr(((ord(character) - 97 + 2) % 26) + 97)
	
	return output_string

caption = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(translate(caption))

url = "map"
print(translate(url))
