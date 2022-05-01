from RawMovieReview import RawMovieReview

class MovieReview(RawMovieReview):
    def __init__(self, file_name, score_threshold):
        super().__init__(file_name)
        self.__score_thresdhold = score_threshold
    def indexing(self, n):
        if int(super().indexing(n)[2]) > self.__score_thresdhold:
            return super().indexing(n)[0], True
        else:
            return self.super().indexing(n)[0], False
if __name__ == '__main__':
    Naver_Movie = MovieReview('samples.csv', 4)
    print(Naver_Movie.indexing(50))