#Go through the string below and if the length of a word is even print "even!"


st = 'Print every word in this sentence that has an even number of letters'

for x in st.split():
    y = len(x)
    if y % 2 == 0:
        print(x)
