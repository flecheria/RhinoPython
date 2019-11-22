######################################################################
#
# DO NOT CANCEL THIS PART
# Author: Paolo Cappelletto
# e-mail: info@flecheria.it
# skype: flecheria
# Date: 191014
# Version: 1.0
# 
# Copyright: MIT License
#
######################################################################

import rhinoscriptsyntax as rs

if __name__ == "__main__":

    objs = rs.GetObjects("Select objects for exporting", select = True, preselect = True)
    folder_path = rs.BrowseForFolder(message = "Select folder for the export:", title = "Multiple SAT exporting")
    file_name = rs.GetString("Write the file name:", "file")
    
    print(folder_path)
    
    for i, obj in enumerate(objs):
        print( "{} {}".format(i, obj) )
        path = "-_Export {}\{}_{}.sat Type Default".format(folder_path, file_name, i)
        rs.Command(path)