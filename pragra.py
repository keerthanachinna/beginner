 def main(re):
    line = ("hello world.good bye")
    print (line)
    print ()
    count = len(re.findall(r'\w+', line))
    print ("The number of words in this paragraph:", count)
