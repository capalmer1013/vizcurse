# vizcurse
Curses based livecoding vj environment

# Getting started
Supports python 2 for now...
- `git clone https://github.com/capalmer1013/vizcurse.git`
- `cd vizcurse`
- `python vizcurse`
- modify and save example.py
- repeat

## Input File

By default, vizcurse will use the provided `example.py` as the input file. To use another file, specify the argument: `-i <file_location>`.
```
$ python vizcurse -i mycode.py
```

## Code Overlay

By default vizcurse will overlay the code from input file. To disable this behavior, specify the `--hide-overlay` flag.
```bash
$ python vizcurse --hide-overlay
```

