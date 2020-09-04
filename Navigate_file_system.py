1. 'pwd':  tells us about the current working directory

    $ pwd
    /c/Users/dell/desktop/linux_os

2. 'ls' : list the fles of current working directory

     $ ls
     ARRAY_PROGRAMS/   BINARY_SEARCH/         LIST_PROGRAMS/   MORE_PYTHON_PROGRAMS/
     BASIC_PROGRAMS/   DICTIONARY_PROGRAMS/   MATH_PROGRAMS/  

##NOTE:
if we use here like : ls ARRAY_PROGRAMS/  -->we will get the list of  files or folders in ARRAY_PROGRAMS folder.


3. 'ls -a' : To see the list of files including hideen files

    ./   .git/            BASIC_PROGRAMS/  DICTIONARY_PROGRAMS/  MATH_PROGRAMS/
    ../  ARRAY_PROGRAMS/  BINARY_SEARCH/   LIST_PROGRAMS/        MORE_PYTHON_PROGRAMS/

4. 'ls -l' : long form of list which displays the permissions of users and group owners,somesizes and data information.

    $ ls -l
    total 48
    drwxr-xr-x 1 dell 197121 0 Aug 28 18:26 ARRAY_PROGRAMS/
    drwxr-xr-x 1 dell 197121 0 Aug 28 10:12 BASIC_PROGRAMS/
    drwxr-xr-x 1 dell 197121 0 Aug 30 10:45 BINARY_SEARCH/
    drwxr-xr-x 1 dell 197121 0 Aug 29 23:32 DICTIONARY_PROGRAMS/
    drwxr-xr-x 1 dell 197121 0 Aug 28 20:14 LIST_PROGRAMS/
    drwxr-xr-x 1 dell 197121 0 Sep  3 20:16 MATH_PROGRAMS/
    drwxr-xr-x 1 dell 197121 0 Aug 31 16:33 MORE_PYTHON_PROGRAMS/

5. 'ls -la': hidden files plus the long form inforamtion (ls -a + ls -l == ls -la)

    $ ls -la
    total 80
    drwxr-xr-x 1 dell 197121 0 Sep  4 11:29 ./
    drwxr-xr-x 1 dell 197121 0 Sep  4 11:21 ../
    drwxr-xr-x 1 dell 197121 0 Sep  3 20:18 .git/
    drwxr-xr-x 1 dell 197121 0 Aug 28 18:26 ARRAY_PROGRAMS/
    drwxr-xr-x 1 dell 197121 0 Aug 28 10:12 BASIC_PROGRAMS/
    drwxr-xr-x 1 dell 197121 0 Aug 30 10:45 BINARY_SEARCH/
    drwxr-xr-x 1 dell 197121 0 Aug 29 23:32 DICTIONARY_PROGRAMS/

6. 'cd': goes back to home directory

    $ pwd
    /c/Users/dell/desktop/questions

    $ cd
    $ pwd
    /c/Users/dell

7. 'man <command>' : list all the functions of that command

    $ man ls
    $ man pwd
    
##NOTE:
    '.'     -> current directory
    '..'    -> parent directory
    '../'   -> parent directory

##Example:
    $ pwd
    /c/Users/dell/desktop/questions

    $ cd ..
    $ pwd
    /c/Users/dell/desktop

##Example:
    $ pwd
    /c/Users/dell/desktop/questions

    $ cd ../..
    $ pwd
    /c/Users/dell

##Example:
    $ pwd
    /c/Users/dell/desktop/questions

    $ cd ../../Documents
    $ pwd
    /c/Users/dell/Documents










