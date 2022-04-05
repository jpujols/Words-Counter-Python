#Word Counter
def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)
 
print(count_words("words1.txt"))

'''
The function here takes as input a file path. If the file path is in the same directory as your Python script, you can pass in the file name as in the above script. If your text file is somewhere else, then you need to pass the full path when calling the function. 

The rest of the script consists of opening the file in read  mode, loading the text into a string using read  and then splitting and counting the number of words.

'''