__author__ = 'rene_esteves'

class exam_01:

    ##Nao funcionou ainda....

    def somadig(self, input):
        if input < 0: #base case
            return int(self.somadig(self, -input))
        if input == 0: #base case
            return 0
        return input%10 + int(self.somadig(self, input/10))


exam_01.somadig(exam_01, 10000);
