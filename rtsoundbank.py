import struct, json
from pathlib import Path
from functools import partial

struct_fmt = "<IIIIII" # little-endian, 6 integers
                       # friendly reminder: "integer" tipically means a 16-bit integer
                       # and a 16-bit integer is the same as a DWORD

def parse2list(_bin, unpack, length):
    ''' https://stackoverflow.com/a/14216741 '''
    return [unpack(chunk) for chunk in iter(partial(_bin.read, length), b'')]

def banklist2dict(_list):
    dictIndex = []
    for item in _list:
        itemDict = {}
        itemDict['length'] = item[0]
        itemDict['samplerate'] = item[1]
        itemDict['pitch'] = item[2]
        itemDict['looppoints'] = item[3]
        itemDict['looppointl'] = item[4]
        itemDict['start'] = item[5]

        dictIndex.append(itemDict)

    return dictIndex

def pointer_conv(p):
    return int.from_bytes(b''.join(struct.unpack(">ccc", (struct.pack('>i', p)[1:]))), byteorder="big")

def decode_table(_bin): 
    struct_len = struct.calcsize(struct_fmt)
    struct_unpack = struct.Struct(struct_fmt).unpack_from

    parsedIndex = []
    with open(_bin, 'rb') as f:
        parsedIndex = parse2list(f, struct_unpack, struct_len)

    return(banklist2dict(parsedIndex))

def decode_table_json(_bin):
    return json.dumps(decode_table(_bin), indent=4)

def encode_table(f):
    binIndex = bytearray()
    dictIndex = json.loads(f.read()) # json -> dict

    for item in dictIndex:
        binItem = struct.pack(struct_fmt, item["length"], item["samplerate"], item["pitch"], item["looppoints"], item["looppointl"], item["start"])
        binIndex += binItem

    return binIndex

def export_samples(ROMIn, sampleTable, outputFolder): # samples is a list containing the id for the samples that will be exported
    sample_count = 000

    tengokuROM = ROMIn.read()
    dictIndex = sampleTable

    Path(outputFolder).mkdir(parents=True, exist_ok=True) # https://stackoverflow.com/a/273227

    for item in dictIndex:
        startOffset = pointer_conv(item['start'])
        lengthOffset = startOffset + pointer_conv(item['length'])

        with open(outputFolder+"/"+str(sample_count)+".raw", "wb") as outFile:
            outFile.write(tengokuROM[startOffset:lengthOffset])
            sample_count += 1
