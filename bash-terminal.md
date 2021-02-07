##### terminal hotkeys

- ctrl+alt+t opens terminal
- tab completion, bub
- !! (exclamation mark is pronounced bang) - runs the previous command (sudo !!)
- ! e.g. !curl runs the last curl command (you could even do !c for the last command in c)
- ctrl R searches through commands (and lets you edit them)
- -h gives a command's flags e.g. curl -h
- | pipes, (if you e.g. want to do wc of head of example.txt, you could do head example.txt > dummyfile.txt, then wc dummyfile.txt. Or head sonnets.txt | wc piping the output as the standard input of the next command!
- ~ home directory shorthand (i.e. /Users/yourname/
- sudo is substitute user + do
- .. (read dot dot) changes directory one level up
- cd by default goes to ~
- . current directory (cp ~/text_files/sonnets.txt . # copies it to current directory!
- - previous directory! (cd -)
- ; seperates commands
- && <- runs the next command if the last succeeded

###### ctrl plus
- u = clear line
- e = to end of line
- a = to beginning of line
- c = start new line, leaving the other just typed
- l = clears the screen (or type clear)
- d = exit terminal (or type exit)

^ is often used to mean ctrl key

###### files
- \> redirect operator:    echo "blabla" > file.txt #will make a file with those contents!
- \>> append operator will add it to the end of a file (the redirect operator would rewrite it
- cat file.txt prints the file's contents ("concatenate")
- touch foo.txt # creates such a file
- mv both moves a file, but can simply rename it # mv test.txt /folder/test.txt or test1.txt
- cp copies a file #cp test.txt cloneoftest.txt
- rm - deletes one
- head - shows first 10 lines of file (use -11 to read 11 lines...) 
- tail - shows last 10 lines
  - use for monitoring webservers ("tailing the log file") using -f
  - f autorefreshes it(?)
- wc (wordcount) gives # of lines, words, bytes of a file
- less (and more) lets you navigate through a file using the arrow keys, use /the to jump to a the, use n to get to the next the, N to the last... G goes to the end of the file, 1G (one) goes to thee beginning. ctrl-F moves forward one page, ctrl-B back one... Man uses less
  -1g goes to the first line, 17g goes to the 17th line...

###### internet
- ping + url (it will... ping it constantly. You can then print it to a log, then use tail -f to read the log)
- curl (a tool)
  - curl -o outputgoeshere.txt https://blabla.com/poem.txt ( -o is output)
  - -O (capital o) creates a file with the same name as the target file
  - L follows any redirects
  - I prints HTTP header (a bunch of info about the site...)

###### misc.

- pwd
- history prints command history
- which + (command) checks if the command is available, it will list where the command is located

- grep
  - grep rose sonnets.txt #prints every line with "rose"
  - grep rose sonnets.txt | wc # tells us how many lines have rose (and how many words...)
  - -i ignore case
  - -r (recursive) looks in a directory's files and subdirectories' files
  - grep -r cat text_Files (will output files which contain "cat" in directory text_files
  - -v matches everything except what follows!
- ps aux - shows all processes on your computer (ps = process status, its options dont use -)
  - use kill -15 then the first number found with ps (this is the process id) to kill it
  - pkill -15 -f spring would kill all processes named spring (pkill uses the name, not id?)

- ls \*.txt #finds strings followed by .txt (remember * is "wildcard") ; has the options:
  - \-l long form (prints out date, permissions etc.
  - \rtl prints in order of newest modifcations first (reversed time of modification)(-r -t -l)
  - \-a all (shows hidden things which start with a . )
  - if you e.g. do ls b* it will... Well, if it lists a directory, it also opens it... So use \-d to limit it to the current directory
  - ls text_files/ would list the contents of that directory!


- find
  - find . -name '*.txt' # find in current directory (and subdirectories) stuff with .txt in the name
  
- xdg-open will open something, e.g. .

