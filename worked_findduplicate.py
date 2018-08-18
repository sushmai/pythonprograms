import os
import hashlib
from collections import defaultdict
import csv

src_folder = "D:\Python"

def generate_md5(fname, chunk_size = 1024):
    """
    Function which takes a file name and returns md5 checks
    """
    hash = hashlib.md5()
    with open(fname, 'rb') as f:
        #read th first block of the file
        chunk = f.read(chunk_size)
        #keep reading the file untill the end and update hash
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)

    # return the hex checksum
    return hash.hexdigest()

if __name__ == "__main__":
    """
    Starting block of script
    """

    # the dict will have a list as values
    md5_dict = defaultdict(list)

    file_types_inscope = ["ppt" , "pptx", "pdf", "txt", "py"]

    #walk through all files and folders with in directory

    for path, dirs, files in os.walk(src_folder):
        print("analyzing{}".format(path))
        for each_file in files:
            if each_file.split(".")[-1].lower() in file_types_inscope:
                #the path variables get updated for each subfolder
                file_path = os.path.join(os.path.abspath(path), each_file)
                # if more files with same checksum append to list
                md5_dict[generate_md5(file_path)].append(file_path)

    #identify keys(checksum) having more than one values(filenames)
    duplicate_files = (val for key, val in md5_dict.items() if len(val) > 1)

    # write the list of duplicate files to csv file
    with open ("duplicate.csv", 'w') as log:
        #lineterminator added for windows as it inserts blank rows otherwise
        csv_writer = csv.writer(log, quoting=csv.QUOTE_MINIMAL, delimiter=",", lineterminator="\n")
        header = ["File Names"]
        csv_writer.writerow(header)

        for file_name in duplicate_files:
            csv_writer.writerow(file_name)

    print("Done")
