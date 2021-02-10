import struct, json
from functools import partial

binIndex = 'RT_SFXIndex.bin'
struct_fmt = "<IIIIII" # little-endian, 6 integers
                       # friendly reminder: "integer" tipically means a 16-bit integer
                       # and a 16-bit integer is the same as a DWORD
struct_len = struct.calcsize(struct_fmt)
struct_unpack = struct.Struct(struct_fmt).unpack_from

parsedIndex = []


def parse2list(_bin, unpack, length):
    ''' https://stackoverflow.com/a/14216741 '''
    return [unpack(chunk) for chunk in iter(partial(_bin.read, length), b'')]

def list2dict(_list):
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

with open(binIndex, 'rb') as f:
    parsedIndex = parse2list(f, struct_unpack, struct_len)

with open("index.json", 'w') as f:
    f.write(json.dumps(list2dict(parsedIndex), indent=4))