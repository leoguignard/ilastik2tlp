# ilastik2tlp

Small script to convert a csv output from ilastik manual tracking into a tulip friendly file

## Content
- README.md: this file
- ilastik2tlp.py: the converting script
- Data/divsions15.csv: a test file

## Dependecy
None

## Install
To install the script run the following command:
```shell
python setup.py install --user
```

## Typical usage
```shell
ilastik2tlp.py -i path/to/input.csv -o path/to/output.tlp [-at ADDED_TIME]
                                    [-pb PROLONGE_BRANCHES] [-mt MAX_TIME]
```
or 
```shell
ilastik2tlp.py -h
```
to print the help
