# Cracking

Readme for cracking different things

# John bruteforce with Crunch

If have a hash and need to find the original text you can use John-The-Ripper alongside Crunch to generate all possible combinations of a string of a certain length and then hash it to compare to the original hash.

This specific one is from PST's advent calender 2019, and was used to find a 4 character ascii string that hashed to the SHA1 hash found in target.txt.

    crunch 4 4 -f charset.lst ascii-32-95 | john target.txt --session=crack --stdin --progress-every=3
## Crunch
The first 4 specifies min-length of string, and the second 4 specifies the max-length of the string.

-f tells it to use the charset ascii-32-95 from the file charset.lst.

charset.lst:

> loweralpha-numeric = [abcdefghijklmnopqrstuvwxyz0123456789]
mixalpha-numeric   = [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]
ascii-32-95        = [ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~]

## John
Using | you can pipe the output of Crunch into John.
target.txt is the file it find the hash(es) in that it will compare the hashes it generates to.

--session=crack is an optional parameter that tells it to name the session 'crack' in case you want to check the status of this specific session. When piping into John it has a tendency to not work properly, so it is basically useless in this context.

---stdin tells it to use the input from Crunch as the strings it will hash. You can also specify a file with pre-hashed strings. This will increase time, but the file will likely consume several GBs of storage, so I prefer to pipe the strings in. 

---progress-every=3 tells it to output the current hash it is testing every 3 seconds. This is only necessary if you are piping in info from Crunch, as otherwise you can just press Enter if you want to check progress.

John will automagically find out what hash to use from the target.txt file, so no need to specify.

target.txt:

> 42f82ae6e57626768c5f525f03085decfdc5c6fe


