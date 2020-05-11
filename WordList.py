class WordList:
    @classmethod
    def create(self,data):
        wordList = []
        wordList.extend(self.insert_ASC(self,data))
        wordList.extend(self.insert_DESC(self,data))
        print(len(wordList))
        return wordList

    def insert_ASC(self,data):
        return  self.defaultInsert(self,data,1,len(data))

    def insert_DESC(self,data):
        data.reverse()
        return  self.defaultInsert(self,data,1,len(data))

    def defaultInsert(self,data,index,length):
        array = []
        if index >= length:
            for i in range(0,len(data)):
                array.append(data[i])

            return array
        else:
            array = self.defaultInsert(self,data,index + 1,length)
            for i in range(0,len(data)):
                for j in range(0,len(array)):
                    array.append(data[i]+array[j])

            return  array








