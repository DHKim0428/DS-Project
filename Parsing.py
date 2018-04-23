from bs4 import BeautifulSoup


def main():
    filename = str(input('file name: '))
    f = open(filename, 'r', encoding="UTF8")
    data = f.read()
    f.close()
    f = open(filename, 'w+', encoding="UTF8")
    soup = BeautifulSoup(data, 'lxml-xml')
    data = soup.prettify()
    f.write(data)
    print(data)


main()
