# Read a file

file = open('ramnath.txt','r')
#content = file.Read() Read the entire file
#line = file.readline() Read the first line
lines = file.readlines()
print (lines)


# write a file

file = open('ramnath.txt','w') # write mode will overwrite the file ie it will overwrite entirely
#file = open('ramnath.txt','a') # Append mode will add the content to the existing file
file.write("\nMy Name is Ramnath\n \nI am a Devops Engineer in a Private company \n \nI am from Madurai\n") 
#content = file.read()
#print (content)
file.close()
