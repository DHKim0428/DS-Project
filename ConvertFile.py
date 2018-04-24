import os
import zipfile


def convertExtension(filename, nextExtension):
    nameList = os.path.splitext(filename)
    os.rename(filename, nameList[0] + nextExtension)
    return nameList[0] + nextExtension


def extractZip(filename):
    nameList = os.path.splitext(filename)
    Dir = os.getcwd() + "\\" + nameList[0]
    pptzip = zipfile.ZipFile(filename)
    pptzip.extractall(Dir)
    pptzip.close()


def ppt2zip(filename):
    try:
        filename = convertExtension(filename, ".zip")
        extractZip(filename)
    except FileNotFoundError as e:
        print(filename, "is not exist")
    except Exception as e:
        print(e)


def main():
    fname = input("file name: ")
    ppt2zip(fname)


if __name__ == "__main__":
    main()
