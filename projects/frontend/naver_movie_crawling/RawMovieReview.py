import csv

class RawMovieReview:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__data = list()
        self.__file = open(str(self.__file_name),'r',encoding='utf8')
        self.__read = csv.reader(self.__file)
        for row in self.__read:
            self.__data.append((row[0], row[1], row[2]))
    def indexing(self, n):
        return self.__data[n]
    def len(self):
        return len(self.__data[:])

if __name__ == '__main__':
    Naver_Movie = RawMovieReview('samples.csv')
    print(Naver_Movie.len())
    print(Naver_Movie.indexing(2))