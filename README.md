# Cleanup Stuff

This is a simple command line utility written to move files from one place to another. Seriously, that's what it does.

## Install
Download this file and put it into ```/usr/local/bin``` or ```/usr/bin/``` and that's about it.

## Use
The tool takes three positional arguments: 
- **source**: Where to search for files 
- **dest**: Where to put your files when cleaning up
- **ext**: Which type of files to look for


### Example 
**Cleanup a bunch of downloaded PDFs**

```$ cleanup ~/Downloads ~/PDFs pdf```

## Usage
```
usage: cleanup [-h] [--dry-run] source dest ext

positional arguments:
  source      Cleanup Source
  dest        Cleanup Destination
  ext         Files with extension to clean up, Ex. pdf

optional arguments:
  -h, --help  show this help message and exit
  --dry-run   Cleanup Dry Run. Doesn't actually move the files
```
