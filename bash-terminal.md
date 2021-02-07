##### terminal hotkeys

- ctrl+alt+t opens terminal
- tab completion, bub

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
- curl (a tool)
  - curl -o outputgoeshere.txt https://blabla.com/poem.txt ( /-o is output)
  - /-O (capital o) creates a file with the same name as the target file
  - L follows any redirects


###### misc.

- which + (command) checks if the command is available, it will list where the command is located




- ls \*.txt #finds strings followed by .txt (remember * is "wildcard") ; has the options:
  - \-l long form (prints out date, permissions etc.
  - \rtl prints in order of newest modifcations first (reversed time of modification)(-r -t -l)
  - \-a all (shows hidden things which start with a . )
  - if you e.g. do ls b* it will... Well, if it lists a directory, it also opens it... So use \-d to limit it to the current directory
  
