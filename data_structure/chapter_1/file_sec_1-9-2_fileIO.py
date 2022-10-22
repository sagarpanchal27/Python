
# Reading Single Line Records from a File
def method1(filename):

    print ("method 1")
    file = open(filename, 'r')
    for line in file:
        
        contents = line.split(',')
        command = contents[0]
        # match method is newly introduced in python 3.10
        match command:
            case "beginfill":
                print (command)
                fill_color = contents[1]
            case "circle":
                print (command)
                radius = contents[1]
                line = contents[2]
                color = contents[3]
            case "endfill":
                print (command)
        # similarly we can parse all the commands and do the needful opeations like calling proper methods from graphics lib

    file.close()

# Pattern for Reading Multi-line Records from a File
def method2(filename):

    file = open(filename, 'r')

    command = file.readline().strip()
    while command != "":
        print (command)
        if command == "goto":
            x = file.readline()
            y = file.readline()
            width = file.readline()
            color = file.readline().strip()
        elif command == "circle":
            radius = file.readline()
            width = file.readline()
            color = file.readline().strip()
        elif command == "beginfill":
            color = file.readline().strip()
        elif command == "endfill":
            print ("command -endfill")
        elif command == "penup":
            print ("command -penup")
        elif command == "pendown":
            print ("command -pendown")
        else:
            print ("command -unknown")
        command = file.readline().strip()
    file.close()

if __name__ == "__main__":
    # method1("text_sec_1-9-2.txt")
    method2("file2.txt")
