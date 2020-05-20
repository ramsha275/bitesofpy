names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    i = 0
    
    for c , val in enumerate(names , 1):
        c = str(c)+'.'
	# < (or nothing) makes it left align i.e content will be on left and space is on right , > will do right alignment.
        print("{0:3}{1:<11}{2:}".format(c,val,countries[i]))   
        i += 1
        
enumerate_names_countries()