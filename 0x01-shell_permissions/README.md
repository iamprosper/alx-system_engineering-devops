# Resume of the commands

## Task 0
	The command that switches the current user to the user betty is `su betty`

## Task 1
	The command that shows the username  of the current user is `whoami`


## Task 2
	The command that shows all the groups the current user is part of is ``groups``

## Task 3
	The command that changes the owner of the file hello to the user betty is ``sudo chown betty hello``

## Task 4
	The command that creates an empty file is ```touch```

## Task 5
	The command that adds execute permission to the owner of the file hello is ``chmod u+x hello

##Task 6
	The command that adds execute permission to the owner and the group owner and read permission to other users to the file hello is ``chmod 754 hello``


## Task 7
	The command that add execute permisions to everyone is ``chmod +x``

## Task 8
	The command that adds permission for just all others users is ``chmod 007``

## Task 9
	The command that adds all permissions to the owner, read and execute to the group, and write and execute to the others to the file hello is ``chmod 753 hello``


## Task 10
	The command that sets the same permissions as another file is ``chmod --reference=ref_file file``


## Task 11 
	The command that adds execute permission to only all subdirectories of the current directory is ``find /path/to/base/dir -type d -exec chmod 755 {} +``

## Task 12
	The command that creates a directory with permissions set initially is ``mkdir -m MODE dirname```

## Task 13
	The command that changes the group owner to school for the file hello is ``chgrp school hello``

## Task 14
	The command that changes the owner to vincent and the group owner to staff for all files and directories in the working directory is `` chown -R vicent:staff . ``

## Task 15
	The command that changes the owner nd the group owner of the symbolic link _hello to vincent and staff is ` chown -h vincent:staff _hello `

## Task 16
	The command that changes the owner of the file hello to betty if only it's owned by the user guillaume is ``` chown --from=guillaume betty hello ```

## Task 17
	The command that play the StarWars IV episode in the terminal is ` telnet towel.blinkenlights.nl `

