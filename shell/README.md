# reference

- https://www.gnu.org/software/bash/manual/bash.html
- Linux Shell Scripting Cookbook(2nd).Shantanu Tushar etc.2014

# grammar

~~~~
# expansion&quoting
expansion * # any character in a filename without hidden, e.g. ls [[:upper:]]*
expansion ~ # home dir
expansion {} # e.g. {1,2,3} {1..3} {01..15} {3..1}
expansion $(expression) # result e.g. $(1+2) $(ls) `1+2`
expansion $VAR # e.g. $USER

word delimiters by default: space, tab, newline
double quotes "" # do not suppress $ / ` e.g. "two words $(1+2) $(cal)"
single quotes '' # suppress all
escape \ # e.g. \" \newline
ansi-c quoting # e.g. \n

# stream
0 stdin
1 stdout
2 stderr
> redirect output overwrite
>> redirect output append
>/dev/null 2>&1 silent
< redirect input
| pipe, means result as input
[time [-p]] [!] command1 [ | or |& command2 ] …
|& shorthand for 2>&1 |

# loop
until xx; do xx; done;
while xx; do xx; done;
for name in words; do xx; done;
for (xx;xx;xx); do xx; done; # similar: select

# conditional
if xx; then xx; elif xx; then xx; else xx; fi;

echo -n "Enter the name of an animal: "
read ANIMAL
echo -n "The $ANIMAL has "
case $ANIMAL in
  horse | dog | cat) echo -n "four";;
  man | kangaroo ) echo -n "two";;
  *) echo -n "an unknown number of";;
esac
echo " legs."

command1 && command2
command1 || command2
~~~~

# scenes

~~~~
# display
echo -e "1\n2\n3"
printf "%-5s %-10s %-4.2f\n" 1 Sarath 80.3456

# ls display
ls -1
ls -lh

# ls filter
ls -R
ls -d */
ls -I

# ls sort
ls # by name asc
ls -v # by natural order
ls -S # by size desc
ls -lt # by modification time desc

# merge files
cat * > merged.txt

# compress: -c compress -x extract -v verbose -z .gz -f .tar
tar -cvzf /mybackupfolder/backup.tar.gz /backup-target-dir
tar -xvzf target.tar.gz

# send mail
echo "contents" | mail -s "subject" someone@somecompany.com

# export $1=$2:$1
prepend() { [ -d "$2" ] && eval $1=\"$2':'\$$1\" && export $1; }
~~~~
