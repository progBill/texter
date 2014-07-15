

class Word:

    def __init__(self, word):
        self.word=word
        self.qual={}


    def set_quality(self, key, val):
        self.qual[key]=val

class Text:

    def __init__(self, unbroken_text, num_chunk=None, len_chunk=None):
        self.words = [new Word(x) for x in unbroken_text.split()]
        self.chunks=[]
        self.unigram={}

        # ordered list of words
        if num_chunk:
            #TODO: I think below will leave some words off 
            n=self.len(self.words)/num_chunk
            for i in range(n):
                self.chunks=[x for x in self.words[i:i+n]]
       elif len_chunk:
            n=self.len_chunk/len(self.words)
            for i in range(n):
                self.chunks=[x for x in self.words[i:i+n]]

        # dict of token:num_appearing
        for x in self.chunks:
            if x in self.unigram.keys():
                self.unigram[x]+=1
            else:
                self.unigram[x]=1




