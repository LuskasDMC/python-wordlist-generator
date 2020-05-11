from WordList import WordList
class File:
    def __init__(self,fileName):
        self.file = open(fileName,'w')

    def writeFile(self,data):
        data = list(filter(None,data.split(" ")))
        if isinstance(data,list):
            wordList = WordList.create(data)
            for el in wordList:
                self.file.write(el+'\n')
        else:
            'Invalid data format.'

    def readFile(self):
        print(self.file.readlines())

    def close(self):
        self.file.close()
