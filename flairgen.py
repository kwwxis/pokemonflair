import time
import datetime
from flairnames import *

# PREPARE OUTPUT
# ------------------------------------------------------------------------------------------

output = ''
output_source = ''

# This is a string that will be pasted into the output JS file.
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

# Pokemon Flair
FLAIR_WIDTH   = 40 # pixel width of a flair cell
FLAIR_HEIGHT  = 32 # pixel height of a flair cell
SPRITE_WIDTH  = 33 # the number of cells allowed in one row
SPRITE_HEIGHT = 6 # the number of cells allowed in one column

# Trainer Flair
TRAINER_SHEET_REAL_WIDTH = 1300 # the real width of every trainerflair spritesheet
TRAINER_SHEET_SCALE_WIDTH = 1100 # the scale width (CHANGE ONLY THIS NUMBER FOR TRAINER FLAIRS)
TRAINER_SPRITE_WIDTH = 26 # the number of cells allowed in one row
TRAINER_SPRITE_HEIGHT = 3 # the number of cells allowed in one column
TRAINER_FLAIR_WIDTH  = round(float(TRAINER_SHEET_SCALE_WIDTH) / float(TRAINER_SPRITE_WIDTH), 3)
TRAINER_FLAIR_HEIGHT = TRAINER_FLAIR_WIDTH
TRAINER_FLAIR2_WIDTH = TRAINER_FLAIR_WIDTH / 2 * 3 # two cell

# List of Spritesheets
sheets = [
    'kantoflair', 'johtoflair', 'hoennflair', 'sinnohflair', 'unovaflair', 'kalosflair',
    'alolaflair', 'galarflair', 'formsflair', 'megasflair', 'badgesflair',
    'xytrainerflair', 'orastrainerflair', 'smtrainerflair',
    ]
                 
sheet_source  = [
    'https://b.thumbs.redditmedia.com/QemyaKTfPe2PGWKZ1ALoVELcwaU7it6KAexjGeXKYsQ.png', # kantoflair
    'https://b.thumbs.redditmedia.com/GCDd5BKwaRSOc1VdqYDhDgnyLZC5NLcbO0U9IXus8bs.png', # johto flair
    'https://b.thumbs.redditmedia.com/OWIeXzfOLwvupO2mXvp3Kv6iU3sjNsPUE5Q5L3IWwkk.png', # hoennflair
    'https://a.thumbs.redditmedia.com/uUdeRePNs4Kd-Qp6tRP4-GS4dalckILg5K0YRcHRfK8.png', # sinnohflair
    'https://b.thumbs.redditmedia.com/X-oLepVJ2SfUeyFhQ8MY-zEEAYDErjGz6ldsQHay5SQ.png', # unovaflair
    'https://b.thumbs.redditmedia.com/K0gWNad-nSUg4xnFnD3uDyEraSPMwmltI_9DFiWlRIo.png', # kalosflair
    'https://b.thumbs.redditmedia.com/t5Iw-YM410lzIpnW-fT8X6o7Ncg1ynBJMY7yYKbMtzI.png', # alolaflair
    'https://b.thumbs.redditmedia.com/EhfBIQtycSWUXwk8wpMC-LIf5BuzPOpBKG9qr-38H5Q.png', # galarflair

    'https://b.thumbs.redditmedia.com/7P2ccleOuhUg_OOxRQBQNZ9_zEtGAPs4xolwusf0H5k.png', # formsflair
    'https://b.thumbs.redditmedia.com/V_o8SHUzm2ZbDY76IKSvBdyuaq6lhIIusAfyK3VxY7w.png', # megasflair
    'https://b.thumbs.redditmedia.com/TrB7uTji8dtOKUKn78rAFfhBPKz4PRmGvj61vbh8LiU.png', # badgesflair

    'https://a.thumbs.redditmedia.com/rx-m1zj1pVvi454mmqi-47ep4FejUGbmvN_EQznBN68.png', # xytrainerflair
    'https://b.thumbs.redditmedia.com/uo2FwX_j2sqPkixsy1jmDSv29-1qiEe1NiccMW7Eowo.png', # orastrainerflair
    'https://b.thumbs.redditmedia.com/2CXPDBGX14k_AY06VjMShg-xDg9bds5p6En-coxjuGk.png', # smtrainerflair
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
        88,  # alolaflair
        81   # galarflair
    ]

# DETERMINE LEFT OFFSET POSITIONING
# ------------------------------------------------------------------------------------------

FLAIR_OFFSET_COMMENT     = 67
FLAIRTEXT_OFFSET_COMMENT = 114
FLAIRBALL_OFFSET_COMMENT = 312

FLAIR_OFFSET_LINK       = 145
FLAIRTEXT_OFFSET_LINK = FLAIRTEXT_OFFSET_COMMENT + (FLAIR_OFFSET_LINK - FLAIR_OFFSET_COMMENT)
FLAIRBALL_OFFSET_LINK = FLAIRBALL_OFFSET_COMMENT + (FLAIR_OFFSET_LINK - FLAIR_OFFSET_COMMENT)

output += '.comment .flair { left: '+str(FLAIR_OFFSET_COMMENT)+'px }'
output += '.link .flair { left: '+str(FLAIR_OFFSET_LINK)+'px }'

# changing COMMENT to LINK will give the same result for these 2 lines below
output += '.flair:before { left:'+str(FLAIRTEXT_OFFSET_COMMENT - FLAIR_OFFSET_COMMENT)+'px}'
output += '.flair:after { left:'+str(FLAIRBALL_OFFSET_COMMENT - FLAIR_OFFSET_COMMENT)+'px}'


# GENERATE CSS
# ------------------------------------------------------------------------------------------

# Pokemon Flair
# ~~~~~~~~~~~~~
for i in range(0, SPRITE_HEIGHT):
    for j in range(0, SPRITE_WIDTH):
        prop = 'background-position' if i == 0 and j == 0 else 'background'
        x = '0' if j == 0 else '-' + str(j*100) + '%'
        y = '0' if i == 0 else '-' + str(i*100) + '%'
        output += '.flair-' + str(i) + '-' + str(j) + '{'+prop+':'+x+' '+y+'}'
    output += "\n"
output += "\n"

# Trainer Flair
# ~~~~~~~~~~~~~
output += '.flair.flair-tf{'
output += 'background-size: '+str(TRAINER_SHEET_SCALE_WIDTH)+'px auto !important;'
output += 'width:'+str(TRAINER_FLAIR_WIDTH)+'px;'
output += 'height:'+str(TRAINER_FLAIR_HEIGHT)+'px;'
output += '}'
output += "\n"

# Trainer-2 Flair
# ~~~~~~~~~~~~~~~
TRAINER_FLAIR_OFFSET = abs(TRAINER_FLAIR_WIDTH - TRAINER_FLAIR2_WIDTH)
output += '.flair.flair-tf.flair-tf2{'
output += 'padding-right:'+str(TRAINER_FLAIR_OFFSET)+'px;'
output += 'margin-left:-'+str(TRAINER_FLAIR_OFFSET)+'px;'
output += 'background-origin: content-box;'
output += '}'
output += '.flair.flair-tf.flair-tf2:before, .flair.flair-tf.flair-tf2:after {'
output += 'margin-left:'+str(TRAINER_FLAIR_OFFSET)+'px;'
output += '}'

# Copy 'output' to 'output_source'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
output_source = output

# Sheets
# ~~~~~~
for idx, sheet in enumerate(sheets):
    output += '.flair-'+sheet+'{background-image:url(%%'+sheet+"%%) !important}\n"
    output_source += '.flair-'+sheet+'{background-image:url('+sheet_source[idx]+") !important}\n"

# Extra Sheets (no need to append to 'output_source')
output += '.flair-modtrainerflair { background-image:url(%%mtf%%) !important}'

# Write to output
# ~~~~~~~~~~~~~~~

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

# Default Types
# ~~~~~~~~~~~~~
js_output += 'flair.default_types = [' + "\n"
for default_type in flair_defaults_types:
    js_output += "    '" + default_type + "',\n"
js_output += '];' + "\n"

# Defaults
# ~~~~~~~~
js_output += 'flair.defaults = {' + "\n"
for user, flair in flair_defaults.items():
    js_output += '    "'+user+'": "'+flair+'",'+"\n"
js_output += '};' + "\n"

# Names
# ~~~~~
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
    
    