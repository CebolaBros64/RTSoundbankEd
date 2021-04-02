import argparse
import rtsoundbank

rtRomPath = 'rt_rom.gba'
output = 'RT_SFXIndex.bin'

sfxIndexOffset = 0xAA44FC
sfxIndexLength = 0x5A30

progName = 'main.py'
progDesc = 'Hey baby, howzit going? This. Is. A place. Holder.'

def validate_extension(_str, ext, forceExt=True):
    if forceExt:
        if not _str[-len(ext):] == ext:
            return _str + ext
        else:
            return _str
    else:
        if _str.find('.') != -1:
            return _str
        else:
            return _str + ext

parser = argparse.ArgumentParser(prog=progName, description=progDesc)
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 0.0')
parser.add_argument('-xs', '--export-samples',
                    metavar=('ROM', 'output'),
                    nargs=2,
                    help='Export all samples referenced in the SFX table.')
parser.add_argument('-xt', '--export-table',
                    metavar=('ROM', 'output'),
                    nargs=2,
                    help='Export binary SFX table.')
parser.add_argument('-dt', '--decode-table',
                    metavar=('bin', 'json'),
                    nargs=2,
                    help='Decode binary SFX table into a .json file.')
parser.add_argument('-et', '--encode-table',
                    metavar=('json', 'bin'),
                    nargs=2,
                    help='Encode .json SFX table into a binary file.')

args = parser.parse_args()

if args.decode_table:
    with (open(args.decode_table[1], 'w') as decodedOut,
          open(args.decode_table[0], 'rb') as binTableIn):
        decodedOut.write(rtsoundbank.decode_table_json(binTableIn))

    print('File successfully exported to', args.decode_table[1] + ".")

elif args.encode_table:
    binIndex = bytearray()

    with (open(args.encode_table[1], 'wb') as encodedOut,
          open(args.encode_table[0], 'r') as jsonIn):
        encodedOut.write(rtsoundbank.encode_table(jsonIn))

    print('File successfully exported to', args.encode_table[1] + ".")

elif args.export_samples:
    with (open(args.export_samples[0], 'rb') as ROMIn,
          open("tempTable.bin", 'wb') as binTableOut):
        tengokuROM = ROMIn.read()
        binTableOut.write(tengokuROM[sfxIndexOffset:sfxIndexOffset+sfxIndexLength])

    with (open(args.export_samples[0], 'rb') as ROMIn,
          open("tempTable.bin", 'rb') as binTable):
        outputFolder = args.export_samples[1]
        rtsoundbank.export_samples(ROMIn, 
                                   rtsoundbank.decode_table(binTable), 
                                   outputFolder)

elif args.export_table:
    args.export_table[1] = validate_extension(args.export_table[1], ".bin", forceExt=False)

    with (open(args.export_table[0], 'rb') as ROMIn,
          open(args.export_table[1], 'wb') as binTableOut):
        tengokuROM = ROMIn.read()
        binTableOut.write(tengokuROM[sfxIndexOffset:sfxIndexOffset+sfxIndexLength])

else:
    parser.parse_args('-h'.split())
