import json

jsonIndex = 'index.json'
rtRomPath = 'rt_rom.gba'

output = 'samples.bin'

'''Lowest start value'''
lowStart = 4294967295   # this variable will store lowest start value.
                        # by default it is the highest number 
                        # that a 16-bit integer can store

'''Highest end of a sample'''
hiEnd = 0               # this one'll store the sample's end that's
                        # closest to the file's end.
                        # I really should reword these comments

with open(jsonIndex, 'r') as f:
    for item in json.loads(f.read()):
        if item['start'] < lowStart:
            lowStart = item['start']

        if item['start'] + item['length'] > hiEnd:
            hiEnd = item['start'] + item['length']

print('the first sample referenced by the index is located at', str(lowStart))
print('the end of the samples referenced by the index:', str(hiEnd))

with open(rtRomPath, 'rb') as romFile, open(output, "wb") as outFile:
    '''export samples as one big file'''
    outFile.write(romFile.read()[0x06AAAC:0x8A064F])

rtRomPath = 'rt_rom.gba'
output = 'RT_SFXIndex.bin'

sfxIndexOffset = 0xAA44FC
sfxIndexEnd = 0xAA9F2C

with open(rtRomPath, "rb") as romFile, open(output, "wb") as outFile:  
    tengokuROM = romFile.read()
    
    end_offset = tengokuROM.find(b"MThd")
    print("Found a MIDI file at:",str(hex(end_offset))+". This means the index ends at that address.")
    
    outFile.write(tengokuROM[sfxIndexOffset:end_offset])