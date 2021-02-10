import struct, json
from functools import partial

jsonIndex = 'index.json'
struct_fmt = "<IIIIII" # little-endian, 6 integers
                       # friendly reminder: "integer" tipically means a 16-bit integer
                       # and a 16-bit integer is the same as a DWORD
binIndexPath = 'index.bin'
binIndex = bytearray()

with open(jsonIndex, 'r') as f:
    #parsedIndex = []
    dictIndex = json.loads(f.read()) # json -> dict

    for item in dictIndex:
        #itemTuple = item["length"], item["samplerate"], item["pitch"], item["looppoints"], item["looppointl"], item["start"]
        #parsedIndex.append(itemTuple)
        binItem = struct.pack(struct_fmt, item["length"], item["samplerate"], item["pitch"], item["looppoints"], item["looppointl"], item["start"])
        binIndex += binItem

with open(binIndexPath, 'wb') as f:
    f.write(binIndex)