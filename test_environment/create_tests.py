from sys import argv
import random
r = random.randint #rename random number generator for convenience
random.seed(1000) # seed the random number generator so we all have the same tests
alphabet="qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP"
digits = "1234567890"


def gen_x_digits(x):
    dig = str(r(1,9))
    for i in range(0,x-1):
        dig+=digits[random.randint(0,9)]
    return dig

def gen_x_letters(x):
    dig = ''
    for i in range(0,x):
        dig+=alphabet[random.randint(0,len(alphabet)-1)]
    return dig


from os import path
for eachTest in range(0,5):
    input_filename = path.join(argv[1],"test{0}".format(eachTest))
    solution_filename = path.join(argv[2],"test{0}".format(eachTest)) 
    test_file = open(input_filename, "w")
    number_of_lines_in_file = 10+pow(10,eachTest)
    for i in range(0, number_of_lines_in_file):
        test_file.writelines("{0} {1} {2} {3} {4}\n".format(gen_x_digits(7), #student id
     gen_x_letters(r(1,100)), #first name
     gen_x_letters(r(1,100)), #last name
     gen_x_letters(r(1,100)), #department
     (r(0,40)/float(10))+.01)) #GPA

    test_file.close()
    test_file = open(input_filename,"r")
    solution = open(solution_filename, "w")


    def student_id_comparison_function(key1, key2):
        id1 = key1.split(" ")[0]
        id1 = int(id1)
        id2 = key2.split(" ")[0]
        id2 = int(id2)
        return cmp(id1,id2)

    for eachEntry in sorted(test_file.readlines(), cmp= student_id_comparison_function):
        eachEntry = eachEntry.split(" ")
        solution.writelines(",".join("%s" % i for i in eachEntry))
        
    test_file.close()
    solution.close()

