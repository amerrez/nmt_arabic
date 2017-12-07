file_name = "testtext.txt"
test_file_name = "testdataset.txt"
f = open(file_name,"r")
lines = f.readlines()
print len(lines)
f.close()
print "starting"
f = open(file_name,"w")
lineNum = 0
print "opening tes_File"
test_file = open(test_file_name,"w")
print "test file openned"
for line in lines:
    if lineNum % 10 != 0:
        f.write(line)
    else:
        test_file.write(line)
    lineNum+=1
f.close()
test_file.close()
