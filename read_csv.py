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
import Rhino.Geometry as rg
from random import random
from System.Drawing import Color

###############################################################################
# METHODS
###############################################################################

def read_csv():
    filepathname = rs.OpenFileName("File csv for reading", "Text Files (*.csv)|*.csv")
    
    if(not filepathname):
        print("not file path")
        return
    
    """
    # get data from user
    start = rs.GetInteger("Start at line number",1,1)
    if start is None:
        print("no start value")
        return
    
    end=rs.GetInteger("End at line number",start,start)
    if(end is None):
        print("no end value")
        return
    """
    start = 0
    end = 31
    
    file = open(filepathname)
    data = []
    # line_list = []
    
    for i, line in enumerate(file):
        if(i < start):
            continue
        
        if(i > end):
            break
        
        #line_list.append(line)
        string = ''.join( line[:len(line) - 1] )
        data.append( string.split(',') )
    
    file.close()
    # DEBUG
    # print(data)
    
    return data
    
def sweep_2D_data(data):
    
    row_len = len(data)
    col_len = len(data[0])
    
    new_data = []
    for i in range(col_len):
        new_data.append( range(row_len) )
    
    for i in range(row_len):
        for j in range(col_len):
            new_data[j][i] = data[i][j]
    
    return new_data
    
def random_color():
    red   = int(255 * random() )
    green = 0.0
    blue  = int(255 * random() )
    
    return Color.FromArgb(red, green, blue)


###############################################################################
# MAIN SCRIPT
###############################################################################

if __name__ == "__main__":
    
    # global parameters
    factor = 5
    
    string_data = read_csv()
    
    v_count = len(string_data)        # team
    u_count = len(string_data[0]) + 2 # team data
    # print(u_count, v_count)
    
    id_surface = rs.GetObject("Surface to frame", 8, True, True)
    u_domain = rs.SurfaceDomain(id_surface, 0)
    v_domain = rs.SurfaceDomain(id_surface, 1)
    
    u_step = (u_domain[1] - u_domain[0]) / u_count
    v_step = (v_domain[1] - v_domain[0]) / v_count
    
    rs.EnableRedraw = False
    
    point_list = []
    norm_list = []
    for u in range(u_count):
        point_temp = []
        norm_temp = []
        
        if(u < 1):
            continue
        if(u > u_count - 2):
            continue
            
        u_v = u * u_step
        for v in range(v_count):
            v_v = v * v_step
            pt = rs.EvaluateSurface(id_surface, u_v, v_v)
            point_temp.append(pt)
            
            norm = rs.SurfaceNormal(id_surface, [u_v, v_v])
            norm[1] = 0.0
            norm_temp.append(norm)
            # rs.AddPoint(pt)
            
        point_list.append(point_temp)
        norm_list.append(norm_temp)
    
    # DEBUG
    # check correct data structure
    # print(len(point_list), len(point_list[0]))
    # print(len(norm_list), len(norm_list[0]))
    
    point_list = sweep_2D_data(point_list)
    norm_list = sweep_2D_data(norm_list)
    """
    print( len(string_data), len(string_data[0]) )
    print( len(point_list), len(point_list[0]) )
    print( len(norm_list), len(norm_list[0]) )
    """
    for i, team in enumerate(string_data):
        
        new_color = random_color()
        new_layer = rs.AddLayer(name = team[0], color = new_color)
        mat = rs.AddMaterialToLayer(new_layer)
        # test = rs.LayerMaterialIndex("base_surf")
        # rs.MatchMaterial(rs.ObjectMaterialIndex(new_layer), rs.ObjectMaterialIndex(mat) )
        rs.MaterialColor(mat, new_color)
        rs.MaterialShine(mat, 255 * 0.03)
        
        for j, value in enumerate(team):
            
            if(j == 0):
                # print("ok")
                name_dot = rs.AddTextDot(value, point_list[i][j])
                rs.ObjectLayer(name_dot, new_layer)
            else:
                # convert to string to float
                value = float(value)
                if(value > 0):
                    value = value * factor
                # select vector
                vec_coord = norm_list[i][j]
                print(vec_coord)
                # scale vector with data from team
                vec = rs.VectorScale(vec_coord, value + 0.1 )
                
                if(rs.VectorLength(vec) < 0.1):
                    # unitize vector
                    vec_unit = rs.VectorUnitize(vec)
                    vec = rs.VectorScale(vec_unit, 0.2)
                
                print(point_list[i][j])
                # copy point
                start_point = rs.AddPoint(point_list[i][j])
                end_point = rs.CopyObject(start_point, vec)
                # create a line
                line = rs.AddLine(point_list[i][j], end_point)
                pipe = rs.AddPipe(line, [0.0, 1.0], [4, 4], cap = 1)
                rs.DeleteObjects([start_point, end_point, line])
                rs.ObjectLayer(pipe, new_layer)
                
        
    
    rs.EnableRedraw = True