# seedcreator
generates 24 word seeds with 16-sided dices

#don't use the button random for real seed. it's only for testing!

## notes

it's version 0.1 but fully functional.

I'll make it more beautiful when I have a little time for it.

This is my first public project on github. I am always grateful for suggestions what I can do better.

you can use the binaries in binaries, but I recomment to run from source.

you need only to install pyside2 library to run it. It's testet with python 3.8.
pip install pyside2

run from source:
python main.py

### link to german forum about this tool:

https://coinforum.de/topic/20273-seed-durch-w%C3%BCrfeln-berechnen-f%C3%BCr-ledger-electrum-usw-von-hand-mit-tools/

## binary hashcode

### windows

hash SHA256: f192aea98b7619dfff92fd801b94d1fbeabc199bc1939d508ec6b70640c1a65a

check with: 

certutil -hashfile SeedCreatorr.exe SHA256

powershell:

Get-FileHash SeedCreatorr.exe -Algorithm SHA256