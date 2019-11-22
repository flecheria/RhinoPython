######################################################################
#
# Arc example from Rhinocommon
# 
# Copyright: MIT License
#
######################################################################

import rhinoscriptsyntax as rs

# imperative version with enumerator/generator
def range_float(start, stop, step):
    if(stop == None):
        stop = start + 0.0
    if(step == None):
        step = 1.0
    while start < stop:
        yield start
        start += step

# recursive version, see the tolerance on the result
def range_float_rec(start, stop, step):
    if(start <= stop):
        return [start] + range_float_rec(start + step, stop, step)
    else:
        return []

if __name__ == "__main__":
    
    """ this a version of a quad subdivision of nurb surface
    the programming style is pretty imperative, only to a
    common approach that more suitable for beginner, simpler
    maybe because more procedural
    """
    
    # starting with Rhinoscript
    objId = rs.GetObject("Select a surface", select = True)
    u_div = rs.GetInteger("Select u division", 5, minimum = 1)
    v_div = rs.GetInteger("Select u division", 4, minimum = 1)
    
    rs.EnableRedraw(False)
    
    u_list = range_float_rec(0.0, 1.0, 1 / u_div)
    v_list = range_float_rec(0.0, 1.0, 1 / v_div)
    
    matrix = []
    
    for x in range(len(u_list)):
        # create empty row
        row = []
            
        for y in range(len(v_list)):
            
            uv = (u_list[x], v_list[y])
            real_uv = rs.SurfaceParameter(objId, uv)
            real_p = rs.SurfaceEvaluate(objId, real_uv, 0)
#            p = rs.AddPoint(real_p[0])
            # append point to row
            row.append(real_p)
        
        matrix.append(row)
    
    for x in range(len(matrix) - 1):
        row1 = matrix[x]
        row2 = matrix[x + 1]
        for y in range(len(row) - 1):
            ps = [ row1[y][0], row1[y + 1][0], row2[y + 1][0], row2[y][0] ]
            rs.AddSrfPt(ps)
            
    rs.EnableRedraw(True)