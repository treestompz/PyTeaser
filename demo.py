from pyteaser import Summarize

def summarize_file(filename):
    with open(filename, 'r') as f:
        title = f.readline().decode('cp1252')

        content = ""
        for line in f:
            if line:
                content += line.decode('cp1252')

        print filename + " / " + title
        summary = Summarize(title, content)

        for bullet_point in summary:
            print "[+] " + bullet_point


summarize_file("500words.txt")
print ""
print ""
summarize_file("1000words.txt")
print ""
print ""
summarize_file("2000words.txt")