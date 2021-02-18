
###### this clones a repo in another folder and automatically changes to it
```bash
gclone() {

cd $HOME/git-linux && git clone "$1" && cd "$(basename $1 .git)"

}
```

---

https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/shell_scripts/shell_scripts.html
http://mywiki.wooledge.org/BashSheet
linuxcommand.org/lc3_lts0070.php


https://community.linuxmint.com/tutorial/view/1998 <- self extracting file


(The Unix-Hater's Handbook, while dated, does an excellent job illustrating the design-flaws of Unix and C, though you sometimes have to "look a little below the surface" of the stories presented to see it.)



Turn touchscreen on/off: xinput set-prop "ELAN Touchscreen" "Device Enabled" 1
0 will turn it back off
xinput set-prop "ELAN Touchscreen" "Device Enabled" 0
 <- made it auto turn off with a bash file in /etc/init.d
<- sudo update-rc.d /etc/init.d/turnofftouchpad.sh defaults use to updatesetupstuff

-------
system info:  inxi -Fxz

------
disable bluetooth from booting:
 echo "blacklist btusb" | sudo tee /etc/modprobe.d/blacklist-bluetooth.conf
temporary enable it:
sudo modprobe -v btusb
permenantly enable it:
 sudo rm -v /etc/modprobe.d/blacklist-bluetooth.conf
---------
how to install on mint:
$ tar xjf Downloads/anki-2.1.22-linux-amd64.tar.bz2
$ cd anki-2.1.22-linux-amd64
$ sudo make install

-------- update python:
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.8

--------------
python ui
make something with designer

then alex@jungle2:~/.local/bin$ pyuic5 -x "/home/alex/Desktop/helloworld.ui" -o "/home/alex/Desktop/helloworld.py"

/home/alex/.local/bin/pyui5c
/home/alex/Desktop/helloworld.ui

/home/alex/Desktop/helloworld.ui

--------
 tab autocompletes filenames/commands etc! 
"cd -" #switches to last working directory (many shells have "cd" do it already)

ctrl a - moves to left of line, ctrl e to end of line
------

a fairly self-sufficient linux user:

0) comfort with bash syntax and basic commands; know what a pipe is and how to grep for something

1) ability to troubleshoot X11, in particular xorg.conf

2) basic proficiency with network tools iproute2/iwconfig and wpa_supplicant if you connect to secure networks

3) some understanding of your distro's package manager and the ways it can fail

4) ability to download and install a package from source: usually wget and tar commands followed by the magic './configure && make && make install' incantation

--------

Start scripts:
#!/bin/bash <- Oh, specifies the script interpreter.  LEARNED.
# chmod +x <- Oh, needs execute bit set.  LEARNED.
https://www.reddit.com/r/linux/comments/u5egw/so_what_is_the_best_way_to_learn_bash/c4soxtu/

---------

https://medium.com/better-programming/best-practices-for-bash-scripts-17229889774d


-----------

One of my favourite ways to reverse engineer whatever is running on the box is to use the ps and lsof commands:
ps -ef - list all running processes on the system
lsof -p <pid> - show all files, sockets and network ports open for a specific process
lsof -i :<port> - show which process has a specific port open


apt remove <xserver-xorg-input-synaptics> <- installs and uninstalls stuff from package manager
    apt install

cd test <- enters a directory/file (test!)
touch a b <- makes files a and b
ls <- lists files in directory
rm a # removes a
* #glob, means all

command types: # "type" gives command type description: type rm
    alias - shortening of command (only in interactive shell, not scripts) it's a word mapped to a string
        alias nmapp="nmap -Pn -A --osscan-limit" will run that command as nmapp
    functions - aliases but in scripts - can take arguments/create variables
    builtins - already provided functions: cd, echo etc.
    keywords - builtins with parsing rules (extended versions of buoltins?)
    executables - applications/external commands - seperated via colons e.g. ./usr/bin:/bin but if no file path specified, bash searches the directories in path to find something., if its outside of the known paths, you need to define it

start scripts with: #!/bin/bash <- interpreter directive specifies which interpreter to use
    #!/usr/bin/env bash <- equivilent variant'

execute scripts: bash myscript (doesn't need #!)
    OR :chmod +x myscript <- makes script executable
        ./myscript <- to execute it directly (#! is used)

Put your scripts in a personal directory:
$ mkdir -p "$HOME/bin" <- makes bin in home directory (tradition to hold commands in "something nmamed bin
$ echo 'PATH="$HOME/bin:$PATH" ' >> "$HOME/.bashrc" <- adds variable assignment to bash config file (so all interactive instances of bash will check this new directory)
$ source "$HOME/.bashrc" <- tells bash to reread the config
<- so $ myscript #instead of $ mv myscript "$HOME/bin"

Special characters: 
    $ - expansion
    ' ' single quotes give text "literal meaning" so it isn't parsed or changed
    " " double quotes allows substitutions to occur
    \ escape - keeps something from being read as a special character (As if in a quote)
    # comment, not parsed
    = assigns value to variable, no whitespace
    [[ ]] tests whether true or false to compare strings, see if file exists
    ! negate/reverse test or exit status
    >, >>, < redirect command output or input to file
    | pipe, makes a command's output another's input
    ; seperates commands on same line
    && like ; but only runs if last command was successful
    !$  reuse last item (e.g. file) from previous command
        alt . does this too, use . to shift between options
    !! reuse whole previous command (e.g. "sudo !!" to rerun it with root)
    { } inline group, multiple commands as one as if a function
    ( ) subshell group - like above, but in a subshell/new process (no effect on current program)
    (( )) arithmetic expression, (( a = 1 + 4 )) or if ((a < b ))
    $(( )) arithmetic expansion, expression is replaced with result echo "the average is $(( (a+b)/2))". 
    $( ) - command substitution   
     *, ? - wildcards matching parts of filenames
    ~ home directory (current users, or specify another user: ls ~/documents; cp ~john/.bashrc
    . current directory
    & background (run in background, don't wait for complete)
$ echo "I am $LOGNAME"
I am lhunath
$ echo 'I am $LOGNAME'
I am $LOGNAME
$ # boo
$ echo An open\ \ \ space
An open   space
$ echo "My computer is $(hostname)"
My computer is Lyndir
$ echo boo > file
$ echo $(( 5 + 5 ))
10
$ (( 5 > 0 )) && echo "Five is greater than zero."
Five is greater than zero.

paramters - named space in memory to retrieve/store info
    variables or special parameters. Special are read only, set by bashh to show internal status. You make the variables (named with letters, numbers or underscore, can't start with nunmber)
    Parameter expansion (happens with $ substitutes it with its value, bash may perform actions on the result! E.g. $ echo "Foo is $foo" will replace foo with its value (always put double quotes around them!). rm $file='no secret' would rm no and secret
nb: echo " '$USER', '${USER}s' " -> lhunath, lhunaths
$ for file in *.JPG *.jpeg
do mv -- "file" "${file%.*}.jpg" <- JPG/jpeg->jpg


    Special parameters: ???
0 - name/path of script (not always reliable)
1 2... contain arguments passed to script/function
* words of all positional parameters, in quotes - a single string
@ the words of all positional parameters, in quotes - a list of individual words
# the number of parameters set
? exit code of most recent foreground command
$ PID (process id number) of shell
! pid of most recent background command
_ last argument of last executed command
    variables given by shell: (among others)
TMPDIR - dir used to store temp files
 PS1 - format of shell prompt
PATH - list separated by colons, searched to find command
HOME - current home dir
LINES - height of terminal in characters
COLUMNS - widith of terminal in characters
UID - ID numb of user (not reliable?)
RANDOM - generates num between 0-32767
PWD - current working direct
PPID - PID of shell's parent process
HOSTNAME - of comptuter
Bash_VERSION - describes bashv ersion

    Variable types:
array - declare - a variable
associative array - A ...same?
integer - declare -i variable (Automatically triggers arithmetic evaluation
read only declare -r variable
export - declare -x variable - marked for export, inherited by a child process

    arrays - indexed list of strings

    parameter expansion tricks:
${parameter:-word} - use default, substitutes word if parameter's unset/ull
${parameter:=word} - assign default, if parameter's null/unset, defines parameter as word
${parameter:+word} - use alternate - if parameter's null/unset, no substitution, use word if parameter exists
${parameter:offset:length} substring expansion - types length's # of characters starting from the characterspecified by offset
${#parameter} substitutes length of parameter


apt rdepends python2.7 <- will list everything which has python2.7 as a dependency/needs it to run


