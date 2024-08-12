#A function that counts the number of times a substring occurs in a string

test_sub_str = "st"
test_str = "Stop staring at my test stranger!"

count = 0
test_str = test_str.lower()

#For loop
for char in range(len(test_str)):
    if test_str[char] == "s" and test_str[char + 1] == "t":
    	count += 1
    
    #return count

#if "st" in test_str:
    #count += 1

#While loop
"""idx = 0
while idx < len(test_str):
	if test_str[idx] == "s":
		if test_str[idx + 1] == "t":
			count +=1
	idx += 1"""

print(count)
	
