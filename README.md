Dirsync
It syncs contents of two directories, replacing older files with their latest modified copies from other folder.

How to use:
It can be executed from a terminal and as an executable.
To run from the terminal,
    
python dirsync.py [additional_arguments]

Additional Arguments

-f [filename]
or
--filename [filename]
Used to read multiple directory paths from a file. The directory paths int the file should be one after the other and the script will sync directories in sets of 2 paths at a time.
Example,
/Directory1
/Directory2
/Directory3
/Directory4
1 and 2 shall be synced first followed by 3 and 4.

-p [path1] [path2]
or
--paths [path1] [path2]
Sync directories of path1 and path2

If not given any arguments when executed it will prompt you whether you want to read the directory paths a file or enter the directory paths yourself. This is the default behaviour when run as an executable.

Development status:
Fully usable
