# https://www.youtube.com/watch?v=nqE4HOtZt1Y&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=21
my_test_file = open('Test.txt', 'w')
try:
    my_test_file.write("Testing file handling")
finally:
    my_test_file.close()
    
# short hand method 
with open('Youtube.txt', 'w') as my_yt_file:
    my_yt_file.write("No need of try block or closing the file mannualy")
    