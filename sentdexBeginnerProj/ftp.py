from ftplib import FTP

#domain name or server ip:
ftp = FTP('123.server.ip')
ftp.login(user='username', passwd = 'password')
ftp.cwd('/whyfix/')

def grabFile():
    filename = 'fileName.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    filename = 'fileName.txt'
    ftp.storbinary('STOR ' + filename, open(filename, 'rb'))
    ftp.quit()