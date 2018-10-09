import os 
def rename_files():
    # get file names from a folder
    
    file_list = os.listdir(r"C:\Users\sushma\Desktop\1\prank")
    #print(file_list )
    # to see the current working directory 
    saved_path = os.getcwd()
    print("Current working directory" + saved_path)
    # change directory to where files are present otherwise it will give error
    # path error 
    os.chdir(r"C:\Users\sushma\Desktop\1\prank")

    # for each file rename filename
    for file_name in file_list :
        print("old_name - "+ file_name)
        print("New_name - " + file_name, file_name.strip("0123456789"))
        os.rename(file_name, file_name.strip("0123456789") )

    # once done go back to original directory 

    os.chdir(saved_path) 

rename_files()
