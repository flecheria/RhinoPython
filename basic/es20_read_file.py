import rhinoscriptsyntax as rs

if __name__ == "__main__":
    
    """
    # select file from open window
    file_path = rs.OpenFileName("Open")
    print(file_path)
    """
    
    # or hard coding path
    file_path = "C:/Users/flecheria/Documents/workspace/RhinoPython/basic/champions/champions_ship_data.csv"
    
    file = open(file_path, "r")
    data = []
    
    # show results
    # print(file)
    # print(  type(file) )
    
    for f in file:
        """
        # temp = f
        temp = f.replace(' ', '')
        temp = temp.strip('\n')
        temp = temp.split(',')
        """
        temp = f.replace(' ', '').strip('\n').split(',')
        #temp[5] = float( '{:.6f}'.format( float(temp[5]) ) )
        data.append(temp)
        
        # data.append( f.replace(' ', '').strip('\n').split(',') )
    
    print(data)
    # print( file.read() )
    
    file.close()
    
    # write
    path = "C:\\Users\\flecheria\\AppData\\Roaming\\McNeel\\Rhinoceros\\5.0\\scripts\\course_introduction\\"
    out_path = rs.SaveFileName("Save file", folder = path, filename = "export_test", extension = ".csv")
    # print(out_path)
    
    out_file = open(out_path, "w")
    
    for d in data:
        
        for item in d:
            out_file.write(item + ",")
        
        out_file.write('\n')
    
    out_file.close()
    