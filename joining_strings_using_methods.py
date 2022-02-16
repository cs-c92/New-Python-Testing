# Printing the lyrics as a list
limelight_first_verse = ['Living on a lighted stage approaches the unreal', 
'For those who think and feel', 
'In touch with some reality beyond the gilded cage.']
#print(limelight_first_verse)

# Join using a comma. Adds a comma and joins up a sentence. Spaces in the text are important, you could end up with poor punctuation.
limelight_lyrics_csv = ','.join(limelight_first_verse)
#print(limelight_lyrics_csv)

# Join using \n as the delimiter. Prints as a paragraph, on separate lines.
limelight_lyrcs = '\n'.join(limelight_first_verse)
print(limelight_lyrcs)

# .strip cleans up the data!
# I'm using a for loop to iterate through the list
# then using .append() to add the stripped lines to a new list.
limelight_second_verse = ['Cast in this unlikely role, ill-equipped to act            ', 
'With insufficient tact           ', 
'            One must put up barriers to keep oneself intact.']

limelight_second_verse_stripped = []
for line in limelight_second_verse:
    limelight_second_verse_stripped.append(line.strip())

limelight_sv_full = '\n'.join(limelight_second_verse_stripped)
print(limelight_sv_full)

# .replace... Replace takes two arguments (I'll use a spelling error as an example)
# and replaces all instances of the first argument in a string with the second argument
# string_name.replace(substring_being_replaced, new_substring)
limelight_chorus = \
 '''Living in the lomeloght, the universal dream
For those who wish to see,
Those who wish to be,
Must put aside the alienation,
Get on with the fascination.
The real relation, the underlying theme!'''
limelight_chorus_fixed = limelight_chorus.replace("lomeloght", "limelight")
print(limelight_chorus_fixed)

# .find()
# takes a string as an argument and searching the string it was run on for that string.
# It then returns the first index value where that string is located. (Indexing starts at 0)
limelight_first_verse = '''Living on a lighted stage approaches the unreal, 
For those who think and feel, 
'In touch with some reality beyond the gilded cage.'''
limelight_placement = limelight_first_verse.find("limelight")
#print('limelight'.find('m'))

