Dirsync
It syncs contents of two directories both ways, older files are replaced with the latest modified ones.

How to use:
It can be run from the terminal as well as a normnal python script.
To run from the terminal,
    
python dirsync.py additional_arguments

You can pass two directories as arguments or use -f as an argument if you want it to read directory paths from a file.
It reads paths from path.txt file present in the same folder as the script.

If not given any arguments while being called it will prompt you whether you want to read the directory paths from the paths.txt file or enter the directory paths yourself.

Development status:
Still in development.