# ilastik2tlp

Small script to convert a csv output from [ilastik](http://ilastik.org/ "ilastik") manual tracking into a [tulip](http://tulip.labri.fr/TulipDrupal/ "tulip") friendly file

## Content
- README.md: this file
- setup.py: install script
- ilastik2tlp.py: the converting script
- Data/divsions15.csv: a test file

## Dependecy
None

## Install
To install the script you can run the following command:
```shell
python setup.py install --user
```
Note that since it is just a small script that do not have dependecy, if you do not need to access it from "anywhere" on your computer, the installation part using ```setup.py``` is not necessary.

## Typical usage
Once install with the previous command, or from the folder containing the script, you can run the script as follow:
```shell
ilastik2tlp.py -i path/to/input.csv -o path/to/output.tlp [-at ADDED_TIME]
                                    [-pb PROLONGE_BRANCHES] [-mt MAX_TIME]
```
or if you want to print the "help", run 
```shell
ilastik2tlp.py -h
```
