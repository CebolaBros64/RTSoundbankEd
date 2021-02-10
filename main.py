rtRomPath = 'rt_rom.gba'
output = 'RT_SFXIndex.bin'

sfxIndexOffset = 0xAA44FC

with open(rtRomPath, "rb") as romFile, open(output, "wb") as outFile:  
    tengokuROM = romFile.read()
    
    end_offset = tengokuROM.find(b"MThd")
    #print("Found a MIDI file at:",str(end_offset)+". This means the index ends at that address.")
    
    outFile.write(tengokuROM[sfxIndexOffset:end_offset])