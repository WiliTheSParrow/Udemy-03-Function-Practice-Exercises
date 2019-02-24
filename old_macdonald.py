# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    a=name[0].upper()
    b=name[1:3]
    c =name[3].upper()
    d=name[4:]
    name =a+b+c+d
    return name
	
# Check
old_macdonald('macdonald')
