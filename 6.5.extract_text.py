text = 'X-DSPAM-Confidence:0.8475'
colon_find = text.find(':')			#find the colon character
number_find = text[colon_find+1:]	#add one to the colon position to extract from 0 to end of string from
print(float(number_find))			#convert&print the extracted number to float
# I feel like I just havwe to add this comment here
