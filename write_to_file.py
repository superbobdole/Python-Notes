# read the file and sstore all te lines in list
# reverse the list
# write the list back to the file

with open('../venv/test.txt', 'r') as reader: #flag 'r' to open in read mode
     content = reader.readlines()
     reversed(content)
     with open('../venv/test.txt', 'w') as writer:
         for line in reversed(content):
             writer.write(line)