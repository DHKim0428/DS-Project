from bs4 import BeautifulSoup


def main():
    filename = str(input('file name: '))
    f = open(filename, 'r')
    data = f.read()
    f.close()
    f = open(filename, 'w+')
    soup = BeautifulSoup(data, 'lxml-xml')
    data = soup.prettify()
    f.write(data)


main()
