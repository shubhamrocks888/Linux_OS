                #find
-> find will default acts like ---> 'find .'


1.                  'find .'
-> '.' signifies the current directory
-> It list out all the files and folders below the current directory.

$ find .
.
./demoo.py
./testdir1
./testdir1/demoo1.py
./testdir2
./testdir2/demoo2.py
./testdir3
./testdir3/demoo3.py

2.              'find <folder or file_name>'
->  It list out all the files and folders below the current directory.

$ ls -l
drwxr-xr-x 1 dell 197121       0 Aug 28 13:01  sw_files/
drwxr-xr-x 1 dell 197121       0 Sep  1 19:51 'swati resume'/
drwxr-xr-x 1 dell 197121       0 Oct 28  2019  sweta/
drwxr-xr-x 1 dell 197121       0 Sep 10 11:14  testdir/

$ find testdir/testdir1
testdir/testdir1
testdir/testdir1/demoo1.py

$ find testdir
testdir
testdir/demoo.py
testdir/testdir1
testdir/testdir1/demoo1.py
testdir/testdir2
testdir/testdir2/demoo2.py
testdir/testdir3
testdir/testdir3/demoo3.py

$ cd testdir

$ find demoo.py
demoo.py

$ find testdir
find: ‘testdir’: No such file or directory

#NOTE: find method only search the current directory


3.                  'find <path or .> -type d'
-> It lists out only the directories

$ pwd
/c/Users/dell/desktop/testdir

$ ls
demoo.py  testdir1/  testdir2/  testdir3/

$ find . -type d
.
./testdir1
./testdir2
./testdir3

$ cd ..

$ pwd
/c/Users/dell/desktop

$ find testdir -type d
testdir
testdir/testdir1
testdir/testdir2
testdir/testdir3


4.                  'find <path or .> -type f'
-> It lists out all the files.


                                # SEARCH WITHIN A CURRENT DIRECTORY
-->         'find <path or .> -maxdepth 1'

$ find . -maxdepth 1
.
./demoo.py
./testdir1
./testdir2
./testdir3



                                    #SEARCH BY TIME


5.                  'find <path or .> -type f -name "<file_name>"'
-> It search the filename in current and in below directory.

$ pwd
/c/Users/dell/desktop

$ find testdir -type f -name "demoo1.py"
testdir/testdir1/demoo1.py

#NOTE: always search the file with extension.

$ find testdir -type f -name "demoo1"
#It return nothing bocoz file name not found


6.                  'find <path or .> -type f -name "<file_name*>"'
-> '*' is a wildcard operator
   for example: 'a*'--> it search the file starting with a
   for example: '*.py'--> it search the file starting ending with .py
   for example: '*mo*'--> it search the file starting with middle name no

#NOTE: '*' is a case-sensitive or In other words,searching file is a case_sensitive.

$ find testdir -type f -name "d*"
testdir/demoo.py
testdir/testdir1/demoo1.py
testdir/testdir2/demoo2.py
testdir/testdir3/demoo3.py

$ find testdir -type f -name "*.py"
testdir/demoo.py
testdir/testdir1/demoo1.py
testdir/testdir2/demoo2.py
testdir/testdir3/demoo3.py

$ find testdir -type f -name "*mo*"
testdir/demoo.py
testdir/testdir1/demoo1.py
testdir/testdir2/demoo2.py
testdir/testdir3/demoo3.py

$ find testdir -type f -name "D*"
#find nothing


7.                      'find <path or .> -type f -iname "<file_name*>"'
-> The above command is usef for case insensitive searching.

$ find testdir -type f -iname "D*"
testdir/demoo.py
testdir/testdir1/demoo1.py
testdir/testdir2/demoo2.py
testdir/testdir3/demoo3.py


8.                      'find <path or .> -type f -mmin -<time_limit_in_minutes>'
-> It shows the list of files that were modified or new file created less ten minutes ago

$ find testdir -type f -mmin -1000
testdir/demoo.py
testdir/testdir1/demoo1.py
testdir/testdir2/demoo2.py
testdir/testdir3/demoo3.py


9.                      'find <path or .> -type f -mmin +<time_limit_in_minutes>'
-> It shows the list of files that were modified or new file created more than ten minutes ago

$ find testdir -type f -mmin +1
testdir/demoo.py
testdir/testdir1/demoo1.py
testdir/testdir2/demoo2.py

10.                     'find <path or .> -type f -mmin +<x> -mmin -<y>'
->  It shows the list of files that were modified or newly created  more than x minutes but less
    than y minutes.

$ find testdir -type f -mmin +1 -mmin -10
testdir/testdir3/demoo3.py

11.                     'find <path or .> -type f -mtime -<time_limit_in_days>'
-> It shows the list of files that were modified less than days ago

#NOTE: You can use -mtime just like -mmin ,only difference is that time limit in days.

###Note:
1.  amin or atime --> file that has been accessed
2.  cmin or ctime--> for file status changed time.

#ctime :
-> This is the Change time :
-> ctime is updated when  file’s ownership, access permissions or file contents are modified.
   As stated in ls manual (man ls) : time of last modification of file status information.
   ctime is updated when the inode data changes.




                                     #SEARCH BY SIZE
11.                         'find <path or .> -size +<x>M'
-> It list out all the files that size is more than x MB.
-> Here, M is for mb.

$ find . -size +1M
./AA09B210
./mulyankan LIST 2019-2.xls


12.                         'find <path or .> -size +<x>M'
-> It list out all the files that size is more than x MB.
-> Here, M is for mb.

#NOTE:
1.  k -> for kilobytes
2.  G -> for gigabytes


                                # find files that are empty
-->             'find <path or .> -empty'

$ find . -empty
./demoo.py
./testdir1/demoo1.py
./testdir2/demoo2.py


                        #find the file that ends with .py  and remove it,within current directory

-->         'find . -maxdepth 1 -type f -name "*.py" -exec rm {} +'

$ find . -maxdepth 1 -type f -name "*.py"
./demo.py

$ find . -maxdepth 1 -type f -name "*.py" -exec rm {} +

$ ls
testdir1/  testdir2/  testdir3/

#NOTE: '-exec' is for running command on results
        '{}' is for results
        '+' or '\;' is for ending the command.

#NOTE: Better to use '\l;' for ending the command

'Example': find demo.py file and rename it to demoo.py, within current directory

$ ls
demo.py  testdir1/  testdir2/  testdir3/

$ find . -maxdepth 1 -type f -name "*.py" -exec mv {} demoo.py \;

$ ls
demoo.py  testdir1/  testdir2/  testdir3/


'Example': find demo.py file and move it to sub-directory testdir1

$ ls
demo.py  testdir1/  testdir2/  testdir3/


$ find . -maxdepth 1 -type f -name "*.py" -exec mv {} ./testdir1 \;

$ find
.
./testdir1
./testdir1/demoo.py
./testdir1/demoo1.py
./testdir2
./testdir2/demoo2.py
./testdir3
./testdir3/demoo3.py








        








   




                            



   
   





