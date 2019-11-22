######################################################################
#
# Arc example from Rhinocommon
# 
# Copyright: MIT License
#
######################################################################

import rhinoscriptsyntax as rs
import scriptcontext as sc
from System import Guid

def range_float(start, stop, step):
    if(stop == None):
        stop = start + 0.0
    if(step == None):
        step = 1.0
    while start < stop:
        yield start
        start += stop

def range_float(start, stop, step):
    if(start < stop):
        return [start] + range_float(start + step, stop, step)
    else:
        return [stop]

def get_normalized_series(division):
    return range_float(0.0, 1.0, 1.0 / division)

def get_row(x_division, y_value):
    return (get_normalized_series(x_division), y_value)

def make_matrix(x_division, y_value):
    if(len(y_value) > 1):
        return [get_row(x_division, y_value[0])] + make_matrix(x_division, y_value[1:])
    else:
        return [get_row(x_division, y_value[0])]

def test(matrix):
    if(len(matrix) > 2):
        return [(matrix[0], matrix[1])] + test(matrix[1:])
    else:
        return [(matrix[0], matrix[1])]

def iterate(matrix):
    if(len(matrix) > 2):
        return operate(matrix[0], matrix[1]) + iterate(matrix[1:])
    else:
        return operate(matrix[0], matrix[1])

def operate(row1, row2):
    xs1 = row1[0]
    xs2 = row2[0]
    y1 = row1[1]
    y2 = row2[1]
    
    if(len(xs1) > 2):
        return [(xs1[0], y1, xs1[1], y1, xs1[1], y2, xs1[0], y2)] + operate((xs1[1:], y1), (xs2[1:], y2))
    else:
        return [(xs1[0], y1, xs1[1], y1, xs1[1], y2, xs1[0], y2)]

def operate1(row1, row2):
    print("== " + str(row1) + " " + str(row2))

# SCRIPT

# select object
#objId = rs.GetObject("Select the surface", preselect = True, select = True)
#objId = "48a4e368-b082-4929-b4f9-da80ee50404a"
a = sc.doc.Objects.FindId(Guid.Parse(objId))
print(a)
#rs.EnableRedraw(False)

# make matrix
m = make_matrix(10, get_normalized_series(17))
# iterate matrix
d = iterate(m)

for comb in d:
    params1 = rs.SurfaceParameter(objId, [ comb[0], comb[1] ])
    params2 = rs.SurfaceParameter(objId, [ comb[2], comb[3] ])
    params3 = rs.SurfaceParameter(objId, [ comb[4], comb[5] ])
    params4 = rs.SurfaceParameter(objId, [ comb[6], comb[7] ])
    
    p1 = rs.SurfaceEvaluate(objId, params1, 0)
    p2 = rs.SurfaceEvaluate(objId, params2, 0)
    p3 = rs.SurfaceEvaluate(objId, params3, 0)
    p4 = rs.SurfaceEvaluate(objId, params4, 0)
    
    rs.AddSrfPt([p1[0], p2[0], p3[0], p4[0]])

#rs.EnableRedraw(True)
