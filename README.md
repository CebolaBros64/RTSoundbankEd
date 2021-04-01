This script provides a CLI interface for exporting samples off of a Rhythm Tengoku (GBA) ROM file. It's still a work in progress.
Requires Python >3.5

```
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -xs ROM output, --export-samples ROM output
                        Export all samples referenced in the SFX table.
  -xt ROM output, --export-table ROM output
                        Export binary SFX table.
  -dt bin json, --decode-table bin json
                        Decode binary SFX table into a .json file.
  -et json bin, --encode-table json bin
                        Encode .json SFX table into a binary file.
```
