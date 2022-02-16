# Printing the lyrics as a list
limelight_first_verse = ['Living on a lighted stage approaches the unreal', 
'For those who think and feel', 
'In touch with some reality beyond the gilded cage.']
print(limelight_first_verse)

# Join using a comma. Adds a comma and joins up a sentence. Spaces in the text are important, you could end up with poor punctuation.
limelight_lyrics_csv = ','.join(limelight_first_verse)
print(limelight_lyrics_csv)

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