def get0(m1,m2,line):
    x = ['00000',
         '0   0',
         '0   0',
         '0   0',
         '00000']
    use = x[line]
    for c in use:
        print(c*int(m2),end='')
def get1(m1,m2,line):
    x = ['    1',
         '    1',
         '    1',
         '    1',
         '    1']
    use = x[line]
    for c in use:
        print(c*int(m2),end='')
def get2(m1,m2,line):
    x = ['22222',
         '    2',
         '22222',
         '2    ',
         '22222']
    use = x[line]
    for c in use:
        print(c*int(m2),end='')
def get3(m1,m2,line):
    x = ['33333',
         '    3',
         '33333',
         '    3',
         '33333']
    use = x[line]
    for c in use:
        print(c*int(m2),end='')
def get4(m1,m2,line):
    x = ['4   4',
         '4   4',
         '44444',
         '    4',
         '    4']
    use = x[line]
    for c in use:
        print(c*int(m2),end='')
def get5(m1,m2,line):
    x = ['55555',
         '5    ',
         '55555',
         '    5',
         '55555']
    use = x[line]
    for c in use:
        print(c*int(m2),end='')
def get6(m1,m2,line):
    x = ['66666',
         '6    ',
         '66666',
         '6   6',
         '66666']
    use = x[line]
    for c in use:
        print(c*int(m2),end='')
def get7(m1,m2,line):
    x = ['77777',
         '    7',
         '    7',
         '    7',
         '    7']
    use = x[line]
    for c in use:
        print(c*int(m2),end='')
def get8(m1,m2,line):
    x = ['88888',
         '8   8',
         '88888',
         '8   8',
         '88888']
    use = x[line]
    for c in use:
        print(c*int(m2),end='')
def get9(m1,m2,line):
    x = ['99999',
         '9   9',
         '99999',
         '    9',
         '99999']
    use = x[line]
    for c in use:
        print(c*int(m2),end='')
def addspace(m2):
    print(' '*int(m2),end='')
def numer(number,m1,m2):
    for line in range(0,5):
        for tt in range(int(m1)):
            for i in range(len(number)):
                if(number[i] == '0'):
                    get0(m1,m2,line)
                    if(i != len(number)-1):
                        addspace(m2)
                elif(number[i] == '1'):
                    get1(m1,m2,line)
                    if(i != len(number)-1):
                        addspace(m2)
                elif(number[i] == '2'):
                    get2(m1,m2,line)
                    if(i != len(number)-1):
                        addspace(m2)
                elif(number[i] == '3'):
                    get3(m1,m2,line)
                    if(i != len(number)-1):
                        addspace(m2)
                elif(number[i] == '4'):
                    get4(m1,m2,line)
                    if(i != len(number)-1):
                        addspace(m2)
                elif(number[i] == '5'):
                    get5(m1,m2,line)
                    if(i != len(number)-1):
                        addspace(m2)
                elif(number[i] == '6'):
                    get6(m1,m2,line)
                    if(i != len(number)-1):
                        addspace(m2)
                elif(number[i] == '7'):
                    get7(m1,m2,line)
                    if(i != len(number)-1):
                        addspace(m2)
                elif(number[i] == '8'):
                    get8(m1,m2,line)
                    if(i != len(number)-1):
                        addspace(m2)
                elif(number[i] == '9'):
                    get9(m1,m2,line)
                    if(i != len(number)-1):
                        addspace(m2)
            print("") 
n,m1,m2 = input().split()
numer(n,m1,m2)
