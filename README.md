# why
if you tired of looking on results of 
`find / -perm -u=s -type f 02>/dev/null`
and matching these binaries to binaries from gtfobins, then this python code is for you
# how
`gtfobins suid.txt` contains names of binaries with SUID tag in gtfobins
`found suids.txt` are ones you found on machine
# As a result
it matches them and saves you a lot of nerves