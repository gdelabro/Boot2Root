import os

passwd = "Public speaking is very easy.\n1 2 6 24 120 720\n1 b 214\n9 austinpowers\nopukmq\n"
t = [1, 2, 3, 4, 5, 6]

def are_all_diff(tab):
    for i in range(len(tab)):
        j = i+1
        while j < len(tab):
            if tab[i] == tab[j]:
                return 0
            j += 1
    return 1


def test_pattern(tab):
    fd = open("testFile", "w")
    string = list('1 2 3 4 5 6\n')
    for i in range(6):
        string[i * 2] = chr(tab[i] + ord('0'))
    new_pass = passwd
    string = ''.join(string)
    new_pass += string
    fd.write(new_pass)
    fd.close()
    ret = os.WEXITSTATUS(os.system("./bomb testFile | grep Congratulations!"))
    if not ret:
        print new_pass

for i1 in range(7):
    for i2 in range(7):
        for i3 in range(7):
            for i4 in range(7):
                for i5 in range(7):
                    if i1 and i2 and i3 and i4 and i5:
                        t[0],t[1],t[2],t[3],t[4],t[5] = 4,i1,i2,i3,i4,i5
                        if (are_all_diff(t)):
                            test_pattern(t)
