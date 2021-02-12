import argparse
import rtsoundbank

rtRomPath = 'rt_rom.gba'
output = 'RT_SFXIndex.bin'

sfxIndexOffset = 0xAA44FC
sfxIndexEnd = 0xAA9F2C

progName = 'main.py'
progDesc = 'Hey baby, howzit going? This. Is. A place. Holder.'

parser = argparse.ArgumentParser(prog=progName, description=progDesc)            
#parser.add_argument('ROM', 
#                    help='Rhythm Tengoku (GBA) ROM with a CRC32 value of 349D7025.')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.0')
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
    pass

elif args.encode_table:
    binIndex = bytearray()

    with open(args.encode_table[1], 'wb') as encodedOut, open(args.encode_table[0], 'r') as jsonIn:
        encodedOut.write(rtsoundbank.encode_table(jsonIn))
    
    print('File successfully exported to', args.encode_table[1] + ".")

elif args.export_samples:
    pass

elif args.export_table:
    pass

else:
    parser.parse_args('-h'.split())