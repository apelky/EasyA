'''
Parse regular faculty so that it is last name, everything else
'''

dataFile = "Regular_Faculty.txt" # Regular faculty for all Natural Sciences

# Gets the value from the key/value pairs of the data file
def parseDataValue():
    
    # Open dataset file
    f = open(dataFile, "r")
    lines = f.readlines()
    names_list = []

    # Read data in from file
    for line in lines:         
         # - Traverse dataset -

        # Go down a layer in the dataset
        name_position = line.find(",")
        if name_position != -1:
            name = line[:name_position]
            names_list.append(name)
        
    without_dups = list(set(names_list))

    return without_dups

def sortDataValue():
    names_list = parseDataValue()
    new_names_list = []

    for name in names_list:
        print(name)
        last_index = name.rfind(" ")
        last = name[last_index+1:]
        first = name[:last_index]
        l_comma_f = last + ", " + first
        new_names_list.append(l_comma_f)
    
    return new_names_list



def main():
    test_print = sortDataValue()
    print(test_print)

# This calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
