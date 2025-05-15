#its like switch in java
#match the op and execute
#python > 3.10

#match variable:
         #case pattern1:
                #code block
          #case pattern 2:
                 #code block
#write a program to ask the  user which brwoser he want to run autoamtion

browser = (str(input("Enter the browser name\n")))
match browser:
    case "firefox":
        print("starting firefox")
    case "chrome":
        print("starting chrome")
    case "edge":
        print("Execute the edge code")
    case "safari":
        print("Execute the safari code")
    case _: #default when nothing match
         print("Browser not found")


