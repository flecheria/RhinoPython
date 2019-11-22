# NOTE: stand for expected output result

# -----------------------------------------------------------------------------
# BASIC FORMATTING
# -----------------------------------------------------------------------------
# TODO
# print("ciao mi chiamo %s e abito a %s" % (a, b) )
# print("kgjghj" + jhgjhgjhg + "bbjhkj" + hjkjhkhj)

# https://docs.python.org/2/library/string.html#formatstrings

# Old

# '%s %s' % ('one', 'two')
'paolo  il numero {} ma non il numero {}'.format(1, 2)
'paolo  il numero ' + str(1) + ' ma non il numero ' + str(2)
# New
prova = '{} {}'


prova.format('one', 'two')
'{} {}'.format('one', 'two')
# one two

# Old
'%d %d' % (1, 2)
# New
'{} {}'.format(1, 2)
# 1 2

# Only New
'{1} {0}'.format('one', 'two')
# two one

# -----------------------------------------------------------------------------
# PADDING AND ALIGNMENT
# -----------------------------------------------------------------------------

# Align right
# Old
'%10s' % ('test',)
# New
'{:->10}'.format('test')
#       test

# Align left
# Old
'%-10s' % ('test',)
# New
'{:10}'.format('test')
'{:-<10}'.format('test')

# Align center
# Only New
'{:-^10}'.format('test')
# ---test---

# -----------------------------------------------------------------------------
# TRUNCTION
# -----------------------------------------------------------------------------

# Old
'%.5s' % ('xylophone',)
# New
'{:.5}'.format('xylophone')
# xylop

# -----------------------------------------------------------------------------
# TRUNCATION AND PADDING
# -----------------------------------------------------------------------------

# Old
'%-10.5s' % ('xylophone',)
# New
'{:-<10.5}'.format('xylophone')
# xylop     

# -----------------------------------------------------------------------------
# NUMBERS
# -----------------------------------------------------------------------------

# Integers
#Old
'%d' % (42,)
# New
'{:d}'.format(42)
42

# Floats - Default decimal position specification: 6
# Old
'%f' % (3.141592653589793,)
# New
'{:f}'.format(3.141592653589793)
# 3.141593

# Floats - Custom decimal position specification
# Old
'%.3f' % (3.141592653589793,)
# New
'{:.3f}'.format(3.141592653589793,)
# 3.142
'{:f}'.format( round(3.141592653589793, 3) )
# 3.142000

# -----------------------------------------------------------------------------
# PADDING NUMBERS
# -----------------------------------------------------------------------------

#Old
'%4d' % (42,)
# New
'{:4d}'.format(42)
#  42

# Old
'%06.2f' % (3.141592653589793,)
# New
'{:06.2f}'.format(3.141592653589793)
# 003.14

# Old
'%04d' % (42,)
# New
'{:04d}'.format(42)
# 0042

# Old
'%04d' % (42,)
# New
'{:04d}'.format(42)
# 0042

# -----------------------------------------------------------------------------
# SIGNED NUMBERS
# -----------------------------------------------------------------------------

# Old
'%+d' % (42,)
# New
'{:+d}'.format(42)
# +42

# Use a space character to indicate that negative numbers should be prefixed with a minus symbol and a leading space should be used for positive ones.
# Old
'% d' % ((- 23),)
# New
'{: d}'.format((- 23))
# -23

# Old
'% d' % (42,)
# New
'{: d}'.format(42)
# 42

# New style formatting is also able to control the position of the sign symbol relative to the padding.
# This operation is not available with old-style formatting.
# New
'{:=5d}'.format((- 23))
-  23

# -----------------------------------------------------------------------------
# NAMED PLACEHOLDERS
# -----------------------------------------------------------------------------

data = {'first': 'Hodor', 'last': 'Hodor!'}

# Old
'%(first)s %(last)s' % data
# New
'{first} {last}'.format(**data)
# Hodor Hodor!

# .format() also accepts keyword arguments.
# This operation is not available with old-style formatting.
# New
'{first} {last}'.format(first='Hodor', last='Hodor!')
# Hodor Hodor!




# TODO
# -----------------------------------------------------------------------------
# DATETIME
# -----------------------------------------------------------------------------
# from datetime import datetime
# New
# '{:%Y-%m-%d %H:%M}'
# print( datetime(2001, 2, 3, 4, 5) )
# '{:.%Y-m-d H:M}'.format( datetime(2001, 2, 3, 4, 5) )
# 2001-02-03 04:05


"""
Parametrized formats

Additionally, new style formatting allows all of the components of the format to be specified dynamically using parametrization. Parametrized formats are nested expressions in braces that can appear anywhere in the parent format after the colon.

Old style formatting also supports some parametrization but is much more limited. Namely it only allows parametrization of the width and precision of the output.

Parametrized alignment and width:

This operation is not available with old-style formatting.
New

'{:{align}{width}}'.format('test', align='^', width='10')

Output

   test   

Parametrized precision:
Old

'%.*s = %.*f' % (3, 'Gibberish', 3, 2.7182)

New

'{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)

Output

Gib = 2.718

Width and precision:
Old

'%*.*f' % (5, 2, 2.7182)

New

'{:{width}.{prec}f}'.format(2.7182, width=5, prec=2)

Output

 2.72

The nested format can be used to replace any part of the format spec, so the precision example above could be rewritten as:

This operation is not available with old-style formatting.
New

'{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3')

Output

Gib = 2.72
"""

################################################################################

# The components of a date-time can be set separately:
# This operation is not available with old-style formatting.
# Setup

from datetime import datetime
dt = datetime(2001, 2, 3, 4, 5)

# New

# '{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M')

# Output
# 2001-02-03 04:05

################################################################################

"""
The nested formats can be positional arguments. Position depends on the order of the opening curly braces:

This operation is not available with old-style formatting.
New

'{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3)

Output

     +2.72

And of course keyword arguments can be added to the mix as before:

This operation is not available with old-style formatting.
New

'{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3, sign='+')

Output

     +2.72

"""




# -----------------------------------------------------------------------------
# SOME EXAMPLE
# -----------------------------------------------------------------------------

# Some example
'{0}, {1}, {2}'.format('a', 'b', 'c')
# 'a, b, c'

'{}, {}, {}'.format('a', 'b', 'c')  # 2.7+ only
# 'a, b, c'

'{2}, {1}, {0}'.format('a', 'b', 'c')
#'c, b, a'

'{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
# 'c, b, a'

'{0}{1}{0}'.format('abra', 'cad')  # arguments' indices can be repeated
# 'abracadabra'

'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
# Coordinates: 37.24N, -115.81W

print(test)