import re

def process_file(file_path):
    f = open(file_path, "r")

    # read the file content
    text = f.read()

    # close the input file
    f.close()

    # replace all ' -- ' with ';'
    text = re.sub(r' -- ', ';', text)

    # replace all ' ' with ';'
    text = re.sub(r' ', ';', text)

    # replace all ',' with '.'
    text = re.sub(r',', '.', text)

    # add names to csv
    text = 'timestamp;x;y;z\n' + text

    # write the CSV to a file in Data
    f = open(file_path[:-3] + 'csv', "w")
    f.write(text)

# run the function
process_file('/home/virgil/workspace/PycharmProjects/step_detector/Data/LinearAccelerationDataFile_2016_03_28__15_57_28.txt')
process_file('/home/virgil/workspace/PycharmProjects/step_detector/Data/LinearAccelerationDataFile_2016_03_28__16_22_43.txt')
