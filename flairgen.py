import time
import datetime
from flairnames import *

# PREPARE OUTPUT
# ------------------------------------------------------------------------------------------

output = ''
output_source = ''
load_by_id = """
    for (var key in flair.names) {
        if (flair.names.hasOwnProperty(key)) {
            var data = key.split(' ');
            
            var orig_id = data[2];
            
            if (orig_id.substring(0, 'a'.length) === 'a') {
                orig_id = orig_id.substring(1);
            }
            if (orig_id.substring(orig_id.length - 'm'.length) === 'm') {
                orig_id = orig_id.substring(0, orig_id.length - 1);
            }
            if (orig_id.substring(orig_id.length - 'o'.length) === 'o') {
                orig_id = orig_id.substring(0, orig_id.length - 1);
            }
            if (orig_id.substring(orig_id.length - 'x'.length) === 'x') {
                orig_id = orig_id.substring(0, orig_id.length - 1);
            }
            if (orig_id.substring(orig_id.length - 'y'.length) === 'y') {
                orig_id = orig_id.substring(0, orig_id.length - 1);
            }
            if (orig_id.substring(orig_id.length - 1).match(/[a-z]/i) &&
                orig_id.substring(0, orig_id.length - 1).match(/^\d+$/)) {
                orig_id = orig_id.substring(0, orig_id.length - 1);
            }
            
            var flair_class = '';
            for (var i = 0; i < data.length; i++) {
                flair_class += 'flair-' + data[i] + ' ';
            }
            
            flair_class = flair_class.slice(0, -1);
            
            flair.by_id[data[2]] = {
                key: key,
                spritepos: data[0],
                sheet: data[1],
                poke_id: data[2],
                orig_id: orig_id,
                poke_name: flair.names[key],
                flair_class: flair_class,
            }
        }
    }
"""
js_output = "/* FLAIR MASTER CONFIG | auto-generated at " + \
    datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S-0' + \
        str(7 if time.localtime().tm_isdst else 8) + '00 (ISO-8601)') + " */ \n" + \
        "flair.load__by_id = function() {"+load_by_id+"};\nflair.by_id = {};\n"
    
# SETTINGS
# ------------------------------------------------------------------------------------------

# the width and height of an individual sprite in pixels
FLAIR_WIDTH   = 40
FLAIR_HEIGHT  = 32

TRAINER_FLAIR_WIDTH = 50
TRAINER_FLAIR_HEIGHT = 50

# the number of sprites in a spritesheet row, and the max height of a spritesheet
SPRITE_WIDTH  = 33
SPRITE_HEIGHT = 6

TRAINER_SPRITE_WIDTH = 26
TRAINER_SPRITE_HEIGHT = 3

# list of spritesheets
sheets        = ['kantoflair', 'johtoflair', 'hoennflair', 'sinnohflair', 'unovaflair', 'kalosflair',
                 'alolaflair', 'formsflair', 'megasflair', 'badgesflair',
                 'smtrainerflair', 'xytrainerflair'
                ]
                 
sheet_source  = [
    'https://b.thumbs.redditmedia.com/QemyaKTfPe2PGWKZ1ALoVELcwaU7it6KAexjGeXKYsQ.png', # kantoflair
    'https://b.thumbs.redditmedia.com/GCDd5BKwaRSOc1VdqYDhDgnyLZC5NLcbO0U9IXus8bs.png', # johto flair
    'https://b.thumbs.redditmedia.com/OWIeXzfOLwvupO2mXvp3Kv6iU3sjNsPUE5Q5L3IWwkk.png', # hoennflair
    'https://a.thumbs.redditmedia.com/uUdeRePNs4Kd-Qp6tRP4-GS4dalckILg5K0YRcHRfK8.png', # sinnohflair
    'https://b.thumbs.redditmedia.com/X-oLepVJ2SfUeyFhQ8MY-zEEAYDErjGz6ldsQHay5SQ.png', # unovaflair
    'https://b.thumbs.redditmedia.com/K0gWNad-nSUg4xnFnD3uDyEraSPMwmltI_9DFiWlRIo.png', # kalosflair
    
    'https://b.thumbs.redditmedia.com/WepmgA-MliysLGLOjnx3jhOXnz0sGwU77kqbTihqHQU.png', # alolaflair
    'https://b.thumbs.redditmedia.com/PnQID7Ul-NR2HiieSz5tnpbYkoJyqkC8ZPyJLPOr5Wc.png', # formsflair
    'https://b.thumbs.redditmedia.com/V_o8SHUzm2ZbDY76IKSvBdyuaq6lhIIusAfyK3VxY7w.png', # megasflair
    'https://b.thumbs.redditmedia.com/J_xv88BigKNiZUW0GZmryY7DU-EVwMd0YmlqXD0aHCQ.png', # badgesflair
    
    'https://b.thumbs.redditmedia.com/-dp0Flmv3DsUR_I1gi64ji-1tcPa33WWSmSSQSkHT7c.png', # smtrainerflair
    'https://a.thumbs.redditmedia.com/gu-J-KeHvqzCQwGLMgYOgFIu15WLKIaumShUDakrcF0.png', # xytrainerflair
]

# the number of pokemon in each region/sheet
# excluding special sheets (no national id) - formsflair, megasflair, badgesflair
counts = [
        151, # kantoflair
        100, # johtoflair
        135, # hoennflair
        107, # sinnohflair
        156, # unovaflair
        72,  # kalosflair
        81   # alolaflair
    ]

# GENERATE CSS
# ------------------------------------------------------------------------------------------

# Pokemon
for i in range(0, SPRITE_HEIGHT):
    for j in range(0, SPRITE_WIDTH):
        if (i == 0 and j == 0):
            output += '.flair-0-0{background-position:0 0}'
            continue
        
        x = '-' + str(j * FLAIR_WIDTH) + 'px'
        y = '-' + str(i * FLAIR_HEIGHT) + 'px'
        
        if (j == 0):
            x = '0'
        if (i == 0):
            y = '0'
        
        output += '.flair-' + str(i) + '-' + str(j) + '{background:' + x + ' ' + y + '}'
    output += "\n"
    
output += "\n"

# Trainer
for i in range(0, TRAINER_SPRITE_HEIGHT):
    for j in range(0, TRAINER_SPRITE_WIDTH):
        if (i == 0 and j == 0):
            output += '.flair-0-0.flair-tf{background-position:0 0}'
            continue
        
        x = '-' + str(j * TRAINER_FLAIR_WIDTH) + 'px'
        y = '-' + str(i * TRAINER_FLAIR_HEIGHT) + 'px'
        
        if (j == 0):
            x = '0'
        if (i == 0):
            y = '0'
        
        output += '.flair-' + str(i) + '-' + str(j) + '.flair-tf{background:' + x + ' ' + y + '}'
    output += "\n"
    
output += "\n"
output_source = output

i = 0
for sheet in sheets:
    output += '.flair-'+sheet+'{background-image:url(%%'+sheet+'%%) !important}'
    output += "\n"
    
    output_source += '.flair-'+sheet+'{background-image:url('+sheet_source[i]+') !important}'
    output_source += "\n"
    
    i += 1
    
with open('./flair.css', 'w+') as outfile:
    outfile.seek(0)
    outfile.write(output)
    outfile.truncate()
    
with open('../pokemoncss/src/flair.css', 'w+') as outfile:
    outfile.seek(0)
    outfile.write(output)
    outfile.truncate()
    
with open('../rpokemon.github.io/flair.css', 'w+') as outfile:
    outfile.seek(0)
    outfile.write(output_source)
    outfile.truncate()
    
# GENERATE FLAIR.JS
# ------------------------------------------------------------------------------------------

js_output += 'flair.default_types = [' + "\n"
for default_type in flair_defaults_types:
    js_output += "    '" + default_type + "',\n"

js_output += '];' + "\n"

js_output += 'flair.defaults = {' + "\n"
for user, flair in flair_defaults.items():
    js_output += '    "'+user+'": "'+flair+'",'
    js_output += "\n"

js_output += '};' + "\n"

js_output += 'flair.names = {' + "\n"
js_output += "/* [STANDARD] */\n"

count_index = 0
national_id = 1
offset      = 0

for count in counts:
    # loop height
    for j in range(0, SPRITE_HEIGHT):
        do_break = False
        # loop width
        for k in range(0, SPRITE_WIDTH):
            # break out loop when count exceeded and must go to next sheet
            if national_id > offset + count:
                do_break = True
                offset += count
                break
            
            # Only allow it to go through if in flair_names and is enabled
            if str(national_id) in flair_names and flair_names[str(national_id)][1]:
                pokename = flair_names[str(national_id)][0]
                
                js_output += '    "'+str(j)+'-'+str(k)+' ' + sheets[count_index] + ' ' + str(national_id) + '": "'+pokename+'",'
                js_output += "\n"
            
            national_id += 1
            
        if do_break:
            break
            
    count_index += 1
    
js_output += "/* [ETC/FORMS] */\n"

for sheet_element in flair_etc:
    sheet_name = sheet_element[0]
    sheet_data = sheet_element[1]
    for line_number, sprite_map in sheet_data.items():
        k = 0
        for item in sprite_map:
            poke_id  = item[0]
            enabled  = item[1]
            pokename = item[2]
            
            if poke_id == 'x' or poke_id == 'X':
                k += 1
                continue
            
            if pokename != 'AUTO':
                pokename = item[2]
            elif poke_id[0].isdigit():
                if poke_id.endswith('m'): # megas
                    pokename = ''
                    orig_id = poke_id[:-1]
                    
                    if orig_id.endswith('x'):
                        orig_id = orig_id[:-1]
                        pokename = ' X'
                    elif orig_id.endswith('y'):
                        orig_id = orig_id[:-1]
                        pokename = ' Y'
                    
                    pokename = 'Mega ' + flair_names[orig_id][0] + pokename
                    
                elif poke_id.endswith('f') and (poke_id[:-1]+'e') not in flair_etc_list: # female forms
                    orig_id = poke_id[:-1]
                    pokename = 'Female ' + flair_names[orig_id][0]
                    
            elif poke_id.startswith('a'): # alolan forms
                orig_id = poke_id[1:]
                pokename = 'Alolan ' + flair_names[orig_id][0]
                
            # if pokename is still 'AUTO' (i.e. no name found), set to 'MISSING_NAME'
            if pokename == 'AUTO':
                pokename = 'MISSING_NAME'
            
            # make sure enabled and append
            if enabled:
                js_output += '    "'+str(line_number-1)+'-'+str(k)+' '+sheet_name+' ' + poke_id + '": "'+pokename+'",'
                js_output += "\n"
            
            # increment k
            k += 1
            
js_output += "/* [ETC/TRAINERS] */\n"

for sheet_element in flair_trainers:
    sheet_name = sheet_element[0]
    sheet_data = sheet_element[1]
    for line_number, sprite_map in sheet_data.items():
        k = 0
        for item in sprite_map:
            poke_id   = item[0]
            cellwidth = item[1]
            pokename  = item[2]
            
            
            # make sure enabled and append
            if cellwidth != 0:
                js_output += '    "'+str(line_number-1)+'-'+str(k)+' '+sheet_name+' '+poke_id +' tf tf'+str(cellwidth)+'": "'+pokename+'",'
                js_output += "\n"
                
            # increment k
            if cellwidth == 0:
                k += 1
            else:
                k += cellwidth
    
js_output += '};'

with open('./flair.js', 'w+') as outfile:
    outfile.seek(0)
    outfile.write(js_output)
    outfile.truncate()
    
with open('../rpokemon.github.io/flair.js', 'w+') as outfile:
    outfile.seek(0)
    outfile.write(js_output)
    outfile.truncate()
    
    