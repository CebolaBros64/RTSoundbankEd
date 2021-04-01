import struct, json

jsonIndex = 'index.json'
rtRomPath = 'rt_rom.gba'

def pointer_conv(p):
    return int.from_bytes(b''.join(struct.unpack(">ccc", (struct.pack('>i', p)[1:]))), byteorder="big")

sample_count = 000
with open(jsonIndex, 'r') as f, open(rtRomPath, 'rb') as romFile:
    tengokuROM = romFile.read()
    dictIndex = json.loads(f.read()) # json -> dict

    for item in dictIndex:
        startOffset = pointer_conv(item['start'])
        lengthOffset = startOffset + pointer_conv(item['length'])
        sample_with open("samples/"+str(count)+".raw", "wb") as outFile:
            outFile.write(tengokuROM[startOffset:lengthOffset])
            sample_count += 1

def export_all():
    '''export samples as one big file'''
    with open(rtRomPath, 'rb') as romFile, open(output, "wb") as outFile:
        outFile.write(tengokuROM[0x06AAAC:0x8A064F])

