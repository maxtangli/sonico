# reference

- https://www.gnu.org/software/bash/manual/bash.html
- Linux Shell Scripting Cookbook(2nd).Shantanu Tushar etc.2014

# grammar

~~~~
# expansion
expansion * # any character in a filename without hidden, e.g. ls [[:upper:]]*
expansion ~ # home dir
expansion $VAR # e.g. $USER
expansion $(expression) # result e.g. $(1+2) $(ls) `1+2`
a=1;b=2;let c=a+b;c=$[a+b];
echo "scale=2;3/8" | bc
(cd /bin; pwd); # subshell 

# bash4.0(2009) array, associative_array
a=(0,1);a=([0]=0 [1]=1);a[0]=0;for i in ${a[*]};do echo $i; done; echo ${#a[*]};

unset m;declare -A m;
m=([apple]='100 yen' [orange]='200 yen');
echo ${m[apple]};
echo ${!m[*]};

# quoting
word delimiters by default: space, tab, newline
double quotes "" # do not suppress $ / ` e.g. "two words $(1+2) $(cal)"
single quotes '' # suppress all
escape \ # e.g. \" \newline
ansi-c quoting # e.g. \n

# stream
0 1 2 stdin stdout stderr
> redirect output overwrite
>> redirect output append
>/dev/null 2>&1 silent
< redirect input
| pipe, means result as input
[time [-p]] [!] command1 [ | or |& command2 ] …
|& shorthand for 2>&1 |
| tee [-a] file1 file2... # copy stdout to files

# loop
expansion {} # e.g. {1,2,3} {1..3} {01..15} {3..1} {a..z}

until xx; do xx; done;
while xx; do xx; done;
for name in words; do xx; done;
for (xx;xx;xx); do xx; done; # similar: select

# conditional
[$? -eq 0] -ne -lt -le -gt -ge, -a -o, -f -e -d -r -w -x
[[ str1 == str2 ]] -z -n

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

# script
$# argc
$@ argv
$0 argv[0]
$INDEX argv[INDEX]
$$ pid
$? exit status, default 0 means success

chmod +x script.sh & ./script.sh

how shell handle terminal input
1.terminal input
2.built-in command?
3.absolute path executable?
4.user $PATH executable? // typically, global and local bin/
e.g. ./mybinfile
// dot slash ./ required since current path not included in $PATH, for security reason
// solution: put binary file into mybindir/, add the dir into $PATH

script execution impl: fork(), setup redirect, exec(), wait()

:(){ :|:& };: # http://en.wikipedia.org/wiki/Fork_bomb
~~~~

# scenes

~~~~
# input
read -n 2 chars
read -p "enter password:" -s password

# output
echo -e "1\n2\n3"
printf "%-5s %-10s %-4.2f\n" 1 Sarath 80.3456
echo 'Text through stdin' | cat - file.txt
cat -n lines.txt
cat -s multi_blanks.txt
cat -T tabs.txt

# export $1=$2:$1
prepend() { [ -d "$2" ] && eval $1=\"$2':'\$$1\" && export $1; }

# text edit
sed -i '1i#!/bin/bash' script.sh
sed -i '1c#!/bin/bash' script.sh

echo "splitXsplitXsplitXsplit" | xargs -d X -n 2

echo "HELLO WHO IS THIS" | tr 'A-Z' 'a-z'
echo "Hello 123 world 456" | tr -d '0-9'
echo hello 1 char 2 next 4 | tr -d -c '0-9 \n'
echo "GNU  is  not  UNIX.  Recursive  right  ?" | tr -s ' '
cat multi_blanks.txt | tr -s '\n'
cat sum.txt | echo $[ $(tr '\n' '+' ) 0 ]

sort -nrk 3 sort1.txt | uniq -c

# ls display
find . \( -name "*.txt" -o -name "*.pdf" \) -path "*/slynux/*"
find . -iregex '.*\(\.py\|\.sh\)$'
find . -type f -name "*.swp" -delete
find . -type f -name "*.php" ! -perm 644
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

# symbol link
ln -s target linkname

# rename files

rename *.JPG *.jpg
rename 's/ /_/g' *

# temp files
mktemp # /tmp/tmp.wWlzfGWhCW
mktemp -u test.XXX

# merge files
cat * > merged.txt

# split files
split -b 10k data.file -d -a 4 split_file
csplit server.log /SERVER/ -n 2 -s {*} -f server -b "%02d.log"

# compress: -c compress -x extract -v verbose -z .gz -f .tar
tar -cvzf /mybackupfolder/backup.tar.gz /backup-target-dir
tar -xvzf target.tar.gz

# date
date --date 'Thu Nov 18 08:07:21 IST 2010' +%Y%m%d
date -d '-1 days'
time PIPELINE

# send mail
echo "contents" | mail -s "subject" someone@somecompany.com
~~~~
