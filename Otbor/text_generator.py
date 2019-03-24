
#     text=text.replace(' '+s+' ',' '+s+'_')
import re


class TextGenerator():

    dictionary = {}
    
    # Создадим словарь токенов
    
    def tokenezatciya(self,text):
        text=text.replace('.', ' ')
        text = re.sub(r'\s+', ' ', text)
        t=text.split(' ')
        print(len(t))
        tokens = {}
        for ton in t:
            if(ton in tokens):
                tokens[ton]+=1
            else:

                tokens[ton]=1
        keys=[]  

        for w in sorted(tokens, key=tokens.get, reverse=True):
            keys.append(w)
        tokens = keys
        return tokens

    # Объявляем генераторы

    def gen_sentence (self,text):
        sentence  = text.split('.')
        for s in sentence :
            yield s
            
    def gen_tokens(self,sentence):
        words = sentence.split(' ')
        for w in words:
            if(w!=''):
                try:
                    yield self.tokens.index(w)
                except:
                    print('not in tokens:',w)
                 
    def gen_diigrams(self,tokens_line):
        t0 = '$'
        for t1 in tokens_line:
            yield [t0, t1]
            t0 = t1

    def fit(self,text):

        text = re.sub(r'[^а-яА-Я .]', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        text = text.lower()

        self.tokens = self.tokenezatciya(text)
        # make a list if words value
        sentence = self.gen_sentence(text)
        text = text.replace('.', ' ')

        # make a digrams dictionary
        for sen in sentence:
            toks = self.gen_tokens(sen)
            bigrams = self.gen_diigrams(toks)
            for d in bigrams:
                if (not d[0] in self.dictionary):
                    self.dictionary[ d[0] ] =[]
                if not d[1] in self.dictionary[d[0]]:
                    self.dictionary[d[0]].append(d[1])




    def predict(self,word):
        import random
        wt=0

        word = word.lower()
        try:
            t = self.tokens.index(word)
        except:
            return ' '

        wt = random.choice(self.dictionary[t])

        return self.tokens[wt]

    def gentext(self,word, n_words):
        s = ''
        for i in range(n_words):
            word = self.predict(word)
            s += word + ' '
        return s
    def save(self,name):
        import pickle
        f = open(name+'_dictionary.pkl', 'wb')
        pickle.dump(self.dictionary, f)

        f = open(name+'tokens.pkl', 'wb')
        pickle.dump(self.tokens, f)

    def load(self,name):
        import pickle
        f = open(name+'_dictionary.pkl', 'wb')
        selfdictionary = pickle.load(f)

        f = open(name+'tokens.pkl', 'wb')
        self.tokens = pickle.load(f)






# text=''
# txt =['vm.txt','vm2.txt','vm3.txt','vm4.txt']
# for name in txt:
#     text+=open(name, encoding='utf-8').read()
#
#
# model = TextGenerator()
# model.fit(text)
#
# # print(model.predict('лев'))
# print(model.gentext('лев', 10))


# In[ ]:




