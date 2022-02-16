# using .format to return the artist and song
def song_and_artist(title, artist):
    song_desc = "The song \"{}\" is written by {}.".format(title, artist)
    return song_desc
#print(song_and_artist("Limelight", "Rush"))

# using .format with keywords
def song_description(title, date_released, album_name, artist, label):
    song_des = '''The song {title} was released as a part of the album {album_name}. By the band {artist} in the year {date_released}. It was produced by the record label {label}:'''.format(title = title, date_released = date_released, album_name = album_name, artist = artist, label = label)
    return song_des
artist = "Rush"
title = "Limelight"
album_name = "Moving Pictures"
date_released = "1981"
label = "Mercury"

limelight_description = song_description(title, date_released, album_name, artist, label)
print(limelight_description)

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

# .lower, lets make a lower case verse.
limelight_verse_three = '''Living in a fish eye lens, caught in the camera eye,
I have no heart to lie,
I can't pretend a stranger is a long-awaited friend'''
verse_three_fixed = limelight_verse_three.lower()
print(verse_three_fixed)

# .upper, lets make an upper case verse.
limelight_bridge = '''All the world's indeed a stage and we are merely players!!
Performers and portrayers!
Each anothers audience outside the gilded cage!'''
limelight_bridge_fixed = limelight_bridge.upper()
print(limelight_bridge_fixed)

# .split, lets chop the penultimate chorus up!
penultimate_chorus = '''Living in the limelight, the universal dream
For those who wish to see
Those who wish to be
Must put aside the alienation
Get on with the fascination
The real relation, the underlying theme'''
penultimate_chorus_words = penultimate_chorus.split()
print(penultimate_chorus_words)

# .title, lets capitalise every word in this last chorus
final_chorus = '''Living in the limelight, the universal dream
For those who wish to see
Those who wish to be
Must put aside the alienation
Get on with the fascination
The real relation, the underlying theme
The real relation, the underlying theme!!!'''
final_chorus_titled = final_chorus.title()
print(final_chorus_titled)