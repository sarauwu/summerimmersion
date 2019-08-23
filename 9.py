import hashlib, sys, getopt

#Coded by CameToLearn from https://cybrary.it

#TODO: Add input of multiple hashes

def usage():
print “-v              |    Print attempts”
print “-h              |    This menu”
print “-H, –hash      |    Hash to crack”
print “-t –type       |    Supports: md5, sha1, sha224, sha256, sha384, sha512”
print “-d –dict       |    Dictionary file to crack with”

#    print “-i, –inputfile |    Input file of hashes”
sys.exit()

def main():
counter = 0
input_hash = “”
input_hash_type = “”
#input_hash_file = “”
wordlist = “”
verbose = 0

try:
options, arguments = getopt.getopt(sys.argv[1:], “vhi:H:t:d:”, [“hash=”, “type=”, “help”, “inputfile=”, “dict=”])
except getopt.GetoptError as err:
print str(err)
usage()

for option, argument in options:
if option in (“-h”, “–help”):
usage()
elif option == “-v”:
verbose = 1
elif option in (“-H”, “–hash”):
input_hash = argument
elif option in (“-t”, “–type”):
input_hash_type = argument.lower()
elif option in (“-d”, “–dict”):
wordlist = argument

“””elif option in (“-i”, “–inputfile”):
input_hash_file = argument”””

if input_hash == “” or input_hash_type == “” or wordlist == “”:
usage()

if input_hash_type == “md5”:
htype = hashlib.md5
elif input_hash_type == “sha1”:
htype = hashlib.sha1
elif input_hash_type == “sha224”:
htype = hashlib.sha224
elif input_hash_type == “sha256”:
htype = hashlib.sha256
elif input_hash_type == “sha384”:
htype = hashlib.sha384
elif input_hash_type == “sha512”:
htype = hashlib.sha512

try:
dictfile = open(wordlist,’r’)
except Exception as e:
print “Unable to open file, make sure you typed the correct filename.”, e
sys.exit()

try:
if verbose:
for word in dictfile:
counter += 1
word = word.strip()
hashed = htype(word).hexdigest()
if hashed == input_hash:
print “Hash cracked, at attempt {0}. hashed word is: ‘{1}’ “.format(counter, word)
dictfile.close()
sys.exit()
else:
print “Attempting password ‘{0}’, Attemp No. {1}”.format(word, counter)
else:
for word in dictfile:
counter += 1
word = word.strip()
hashed = htype(word.strip()).hexdigest()
if hashed == input_hash:
print “Hash cracked, at attempt {0}. hashed word is: ‘{1}’ “.format(counter, word)
dictfile.close()
sys.exit()
except KeyboardInterrupt:
print “User Exit”
sys.exit()

main()
