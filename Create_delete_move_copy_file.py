                                # WORKING WITH FILES

1. 'touch <file_name>'              : Create a new file

    $ touch test_file.txt

2. 'open <file_name>'               : Open a file through a terminal

    $ open test_file.txt

3. 'cp <source_file> <new_file_name>': Copy a file

    $ cp test_file.txt copy_file.txt
    ##NOTE: The above copy_file.txt is created in same directory

    'Example':
    #Copy test_file.txt into different folder

    $ cp test_file.txt /c/Users/dell/desktop/copy_file.txt

4. 'mv <source_file> <new_file_name>'                       : To rename a file

    $ mv test_file.txt orig_file.txt

5. 'mv <source_file> <destination_directory>'               : To move a file

   $ mv orig_file.txt subdir1/

6. 'mv <source_file> <destination_directory/new_file_name>': Move and rename at the same time

    $ mv orig_file.txt subdir1/new_file.txt

7. 'rm <file_name>': Delete a file

    $ rm new_file.txt

                             # WORKING WITH DIRECTORIES

1. 'mkdir <new_folder_name>': Create a new folder

    $ mkdir testdir

2. 'cp -r <source_folder> <new_folder_name>': Copy a directory

    $ cp -r subdir1 subdir2
    ##NOTE: The above method make a folder subdir2 with same content as subdir1

3. 'mv <source_folder> <new_folder>': Rename a directory

    $ mv subdir1 subdir3

4. 'mv <source_folder> <destination_directory>': Move a directory

    $ mv subdir2 ../subdir3
    #NOTE: subdir2 folder is moved inside subdir3

5. 'rm -r <folder_name>': Delete a folder

    $ rm -r subdir1

#Note: If you have issues with a deletion to a folder, use -rf  i.e,Force Deletion

    'rm -rf <folder_name>': Delete a folder
    
    

    

    
    
    





