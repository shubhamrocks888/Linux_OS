                            #grep command
                            
->  It stands for global expression regular print           
->  It allows us to search for some texts within files on our system.


                        'Searching for some texts within file'
$ ls
Create_delete_move_copy_file.py  find_command.py  memo.txt  names.txt  Navigate_file_system.py

#lets search name jane wiliams  in names.txt file using grep command
dell@DESKTOP-GINK5BC MINGW64 ~/desktop/linux_os (master)
$  grep "Jane Williams" names.txt

dell@DESKTOP-GINK5BC MINGW64 ~/desktop/linux_os (master)
$

->So,when it didnot find any results,it returns nothing,i.e it jumps to the next line.

#lets search John Williams
$  grep "John Williams" names.txt
John Williams
John Williamson

#lets search only John Willimas as a word
$  grep -w "John Williams" names.txt
John Williams

# grep is a case sensitive,for case insensitive use -i
$  grep -wi "John Williams" names.txt
john williams
John Williams

#lets search the line number with our match using -n 
$  grep -n "John Williams" names.txt
431:John Williams
451:John Williamson

$  grep -wn "John Williams" names.txt
431:John Williams

$  grep -win "John Williams" names.txt
51:john williams
431:John Williams


                                'Search surrounding code of the match'

#Certain number of lines that comes before our match using -B <no.oflines>
$  grep -win -B 4 "John Williams" names.txt
47-119-555-3358
48-508 Pine St., Valyria MD 28445
49-mariajones@bogusemail.com
50-
51:john williams
--
427-218-555-5260
428-502 Maple St., Gotham OR 44147
429-lauraarnold@bogusemail.com
430-
431:John Williams


#Certain number of lines that comes after our match using -A <no.oflines>
$  grep -win -A 4 "John Williams" names.txt
51:john williams
52-304-555-4321
53-607 Martin Hollow, Chucktown WV 25311
54-johnw@johnscompany.com
55-
--
431:John Williams
432-515-555-4529
433-606 Pearl St., Eerie MI 10261
434-johnwilliams@bogusemail.com
435-


#Certain number of lines that comes before and after our match using -C <no.oflines>
$  grep -win -C 4 "John Williams" names.txt
47-119-555-3358
48-508 Pine St., Valyria MD 28445
49-mariajones@bogusemail.com
50-
51:john williams
52-304-555-4321
53-607 Martin Hollow, Chucktown WV 25311
54-johnw@johnscompany.com
55-
--
427-218-555-5260
428-502 Maple St., Gotham OR 44147
429-lauraarnold@bogusemail.com
430-
431:John Williams
432-515-555-4529
433-606 Pearl St., Eerie MI 10261
434-johnwilliams@bogusemail.com
435-


                                'Search text within current directory(Depth level-1)'

#Below command searches all files and directory withi current directory
$ grep "John Williams" ./*
./memo.txt:In our meeting today, John Williams had mentioned that the work could be completed by the end of the month.
./names.txt:John Williams
./names.txt:John Williamson
grep: ./subdir: Is a directory


#Below command searches only text files
$ grep "John Williams" ./*
./memo.txt:In our meeting today, John Williams had mentioned that the work could be completed by the end of the month.
./names.txt:John Williams
./names.txt:John Williamson
grep: ./subdir: Is a directory


                                "Search text below to the current directory (Recursive search)"

#Using -r
$ grep -win "John Williams" ./
grep: ./: Is a directory

$ grep -winr "John Williams" ./
./memo.txt:3:In our meeting today, John Williams had mentioned that the work could be completed by the end of the month.
./names.txt:51:john williams
./names.txt:431:John Williams

        'OR'

$ grep -winr "John Williams" .
./memo.txt:3:In our meeting today, John Williams had mentioned that the work could be completed by the end of the month.
./names.txt:51:john williams
./names.txt:431:John Williams


#Only display the files that contain the match using -l
$ grep -wirl "John Williams" .
./memo.txt
./names.txt

#Dispalys the number of matches in each file using -c
$ grep -wirc "John Williams" .
./Create_delete_move_copy_file.py:0
./find_command.py:0
./memo.txt:1
./names.txt:2
./Navigate_file_system.py:0


                                    "pipe the grep coomand"
$ history
   12  git push
   13  git log
   14  git pull
   15  git push
   16  git status
   17  ls
   18  git log
    .
    .
    .
    .
   508  grep -winr "John Williams" .
   509  grep -wirl "John Williams" .
   510  grep -wirc "John Williams" .
   511  history


#pipe the above command with grep
$ history | grep "git commit"
   48  git commit -m "third commit"
   83  git commit -m "subtract"
  101  git commit -m "bad commit,git revert....all explained"
  105  git commit -m "git revert updated"
  125  git commit -m "second file has changed"
  145  git commit -m "git checkout -- ."
  153  git commit -m
  154  git commit -m "calc python file"
  197  git commit -m "stash explained"
  213  git commit -m "updated add functionality"
  225  git commit -m "updated"
  231  git commit -m "Http Requests"
  235  git commit -m "response object methods"
  406  git commit -m "find command explained"
  452  git commit -m "find with -exec explained"
  512  history | grep "git commit"

$ history | grep "git commit" | grep "commit"
   48  git commit -m "third commit"
   83  git commit -m "subtract"
  101  git commit -m "bad commit,git revert....all explained"
  105  git commit -m "git revert updated"
  125  git commit -m "second file has changed"
  145  git commit -m "git checkout -- ."



                                            "Advanced Searche using grep"

#Search phone number like 123-456-7891
$ grep "...-...-..." names.txt
836-555-5439
442-555-9487
886-555-6636
489-555-4991
366-555-4305
.
.
.
851-555-6015
782-555-3582
689-555-2182
869-555-5446

'NOTE:' Here, '.' -> represents a character.

#Search phone number with advanced regex
$ grep -P "\d{3}-\d{3}-\d{4}" names.txt
836-555-5439
442-555-9487
886-555-6636
489-555-4991
366-555-4305
.
.
.
851-555-6015
782-555-3582
689-555-2182
869-555-5446                              

'NOTE': \d{3}-\d{3}-\d{4} -> This is Perl comaptible expression.

##The above command will work in linux not in mac.







