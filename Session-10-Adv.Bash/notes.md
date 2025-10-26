# command for background

- ping 8.8.8.8 > log.txt 
- above command will put only standard output to the log.txt file

- ping 8.8.8.8 > log.txt  2>&1 
- means standard error is also redirected to the same place where standard output will come which is log.txt.

- ping 8.8.8.8 > log.txt  2>&1  & 
- last & symbol indicates to execute the command in  background.

- 0 is stdin (standard input)
- 1 is stdout (standard output)
- 2 is stderr (standard error)

- simple word 2>&1
- 2> redirects stderr to a mentioned file
- &1 redirects to stdout

## $(command) execution

- create file xyz.txt (touch xyz.txt)
- create file which has data of above created file
- echo "xyz.txt" > data.txt

- rm $(cat data.txt)
- means it will read the file name mentioned inside data.txt which is xyz.txt and remove it from folder.

## Set a entire file data to one variable

- variable1=$(<test.txt)
- variable2=$(cat test.txt)

- check using below command
- echo $variable1
- echo $variable2
- above commands you cna run individually

or create below file

```bash
variable1=$(<test.txt)
variable2=$(cat test.txt)

# check using below command
echo $variable1
echo $variable2
```

## Process Substitution

```bash
#compare 2 sorted outputs of 2 files
diff <(sort file1.txt) <(sort file2.txt)

# Compare command putput directory
diff <(ls ~/dirA) <(ls ~/dirB)
# Create 2 directory and 1 file in each with diffrent name
# Check output
```