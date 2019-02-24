# MASTER YODA: Given a sentence, return a sentence with the words reversed 
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(text):
    a = text.split()
    b = a[::-1]
    c = " ".join(b)
    return c
	
# Check
master_yoda('I am home')

# Check
master_yoda('We are ready')
