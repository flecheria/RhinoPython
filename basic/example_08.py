######################################################################
#
# Write something here to recognize your own file
# 
# Copyright: MIT License
#
######################################################################

from string import maketrans 

if __name__ == "__main__":
    text = """
    Both versions give us the same dictionary, although in slightly different ways.1 As you
learn more Python, you will be better able to determine when defining more variables
makes sense and when it is not useful. For now, you can see it is easy to use many
different defined variables (like cat_names and dog_names) to create new variables
(like animal_names).
    """
    
    intab = "\n.,"
    outtab = "   "
    trantab = maketrans(intab, outtab)
    words = text.translate(trantab).translate(None, '()').split(' ')
    print(words)
    
    words_dict = {}
    
    for w in words:
        if(w is not ''):
            if(w in words_dict.keys()):
                words_dict[w] += 1
            else:
                words_dict[w] = 1
        else:
            continue
            
    print(words_dict)