import clr
import scriptcontext as sc
import rhinoscriptsyntax as rs

clr.AddReference("Microsoft.Office.Interop.Excel")

from Microsoft.Office.Interop import Excel

if __name__ == "__name__":

    if( scriptcontext.sticky.has_key("ExcelApp") ):
        xl = scriptcontext.sticky["ExcelApp"]
        return xl
        
    xl = Excel.ApplicationClass()
    
    sc.sticky["ExcelApp"] = xl
    
    wb = xl.Workbooks.Open(r'path\to\myfile.xlsx', False, True)
    sh = wb.Worksheets(1)
    value = sh.Range["B4"].Text
    # close and quit excel
    close = wb.Close(True)
    close = xl.Quit