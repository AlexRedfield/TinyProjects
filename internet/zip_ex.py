import zipfile

def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password.encode('ascii'))
        return password
    except Exception as e:
        print(e)
        pass

def main():
    zFile=zipfile.ZipFile('test.zip')
    passFile=open('dic.txt')

    for line in passFile.readlines():
        password=line.strip('\n')
        guess=extractFile(zFile, password)
        print(guess)
        if guess:
            print('password: ',guess)
            return
        else:
            print("can't find password")

if __name__ == '__main__':
    main()