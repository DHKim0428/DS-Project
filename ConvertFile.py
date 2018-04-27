import os
import zipfile
import shutil


def convertExtension(filename, nextExtension):
    nameList = os.path.splitext(filename)
    if nextExtension == '.zip':
        shutil.copy(filename, nameList[0] + "_원본" + nameList[1])
    os.rename(filename, nameList[0] + nextExtension)
    return nameList[0] + nextExtension


def extractZip(filename):
    nameList = os.path.splitext(filename)
    Dir = os.getcwd() + "\\" + nameList[0]
    pptzip = zipfile.ZipFile(filename)
    pptzip.extractall(Dir)
    pptzip.close()


def zipzip(dirname):
    ppt = zipfile.ZipFile(os.getcwd() + "\\" + dirname + ".zip", "w")

    for folder, subfolders, files in os.walk(os.getcwd() + "\\" + dirname):
        for file in files:
            ppt.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder, file), os.getcwd() + "\\" +
                                                                  dirname), compress_type=zipfile.ZIP_DEFLATED)
    ppt.close()


"""This method convert pptx file to zip file and extract it.
    filename string should contain Extention (Ex. test.pptx)"""
def ppt2zip(filename):
    try:
        filename = convertExtension(filename, ".zip")
        extractZip(filename)
    except FileNotFoundError as e:
        print(filename, "is not exist")
    except Exception as e:
        print(e)


"""This method convert xml directory to pptx file.
    dirname string must not contain Extention (Ex. test)"""
def dir2ppt(dirname):
    try:
        zipzip(dirname)
        convertExtension(dirname + ".zip", ".pptx")
    except FileExistsError as e:
        print(dirname + ".pptx", "is already exists")
    except Exception as e:
        print(e)


def main():
    mode = int(input("mode(1, 2): "))
    fname = input("file name: ")
    if mode == 1:
        ppt2zip(fname)
    else:
        dir2ppt(fname)


if __name__ == "__main__":
    main()
