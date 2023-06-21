

# This program  that saves my data to a file
poem = 'I like Python and I am not very good at poems'
with open('poem.txt', 'w') as poem_file:   #opens a new file called "poem.txt" and add and alias.
    poem_file.write(poem)
print("done")
'''
'w' =>  we will be *writing* to the file, meaning if the file already exists, it will be overwritten. 
       * to ensure* that the file is automatically closed when we're done with it
        we don't have to worry about closing it ourselves.
poem_file.write() writes the content of the poem variable to the "poem.txt" file.
   
'''
