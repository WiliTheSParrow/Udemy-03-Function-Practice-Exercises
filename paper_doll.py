# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    new_text=''
    for l in text:
        new_text=new_text + l * 3
    return new_text
	
# Check
paper_doll('Hello')

# Check
paper_doll('Mississippi')
