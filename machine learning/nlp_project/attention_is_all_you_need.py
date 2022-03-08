#BLEU Score evaluation done 
#torch text ver 0.6.0 installed 
#spaCy library: tokenization, tagging
#enlish and german library installed in conda nlp
import spacy
#english module from web
spacy_en = spacy.load('en_core_web_sm')
#german module from news
spacy_de = spacy.load('de_core_news_sm')
#distinguishing each word in the sentence
tokenized = spacy_en.tokenizer('I am a student')
#checking tokenization
for i, token in enumerate(tokenized):
    print(f'index {i}: {token.text}')
#defining tokenizing function for both enlgish and german 
def tokenize_de(text):
    return [token.text for token in spacy_de.tokenizer(text)]
def tokenize_en(text):
    return [token.text for token in spacy_en.tokenizer(text)]
#using this library. <sos> and <eos> are classified. Start of sequence and end of sequence.
from torchtext.data import Field, BucketIterator
#create class from spacy and defined function 
#put batch before the sequence, make all letters lower case
SRC = Field(tokenize=tokenize_de, init_token="<sos>", eos_token="<eos>", lower=True, batch_first=True)
TRG = Field(tokenize=tokenize_en, init_token="<sos>", eos_token="<eos>", lower=True, batch_first=True)
#english to german translation data set, Multi30k
from torchtext.datasets import Multi30k
#use classmethod of torchtext, splits, to seperate the data
train_dataset, valid_dataset, test_dataset = Multi30k.splits(exts=(".de", ".en"), fields=(SRC, TRG))
#check the data size by created examples from splits()
print(f"training dataset size: {len(train_dataset.examples)}")
print(f"validation dataset: {len(valid_dataset.examples)}")
print(f"testing dataset: {len(test_dataset.examples)}")
#use vars to print some examples of the dictionary type examples 
print(vars(train_dataset.examples[30])['src'])
print(vars(train_dataset.examples[30])['trg'])
#use build_vocab method to create vocabulary dictionary
SRC.build_vocab(train_dataset, min_freq=2)
TRG.build_vocab(train_dataset, min_freq=2)
#check the length
print(f"len(SRC): {len(SRC.vocab)}")
print(f"len(TRG): {len(TRG.vocab)}")
#construction of vocabulary dictionary. vocab.stoi returns index. vocab.itos returns string.  
print(TRG.vocab.stoi["abcabc"]) #non existing word: 0
print(TRG.vocab.stoi[TRG.pad_token]) # padding: 1
print(TRG.vocab.stoi["<sos>"]) # <sos>: 2
print(TRG.vocab.stoi["<eos>"]) # <eos>: 3
print(TRG.vocab.stoi["hello"]) #4112
print(TRG.vocab.stoi["world"]) #1752
#batch size control 
import torch
#define usable device. For my m1 notebook, cpu is the only option.
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
#set batch size
BATCH_SIZE = 128
#Use Bucketiterator from torchtext to put the squences with similar length in each batch
train_iterator, valid_iterator, test_iterator = BucketIterator.splits(
    (train_dataset, valid_dataset, test_dataset),
    batch_size=BATCH_SIZE,
    device=device)
#check the batch and its sequences
for i, batch in enumerate(train_iterator):
    src = batch.src
    trg = batch.trg

    print(f"{i}th batch size: {src.shape}")

    #extract information of sequences in the batch
    for i in range(src.shape[1]):
        print(f"index {i}: {src[0][i].item()}") #here [Seq_num, Seq_len]

    #do this for batch one only
    break
#Now, create multihead architecture
"""
Key, Query and Values have the same dimension 
parameter: hidden_dim -> dimension of the embedding vector of one word
n_heads: number of concepts for each attention output
dropout_ratio -> multiplying Bernoulli RV to each neuron preventing overfitting
"""
import torch.nn as nn

class MultiHeadAttentionLayer(nn.Module):
    def __init__(self, hidden_dim, n_heads, dropout_ratio, device):
        super().__init__() #imported from the class super

        assert hidden_dim % n_heads == 0 #concatenation will always result the hidden_dim of the embedding

        self.hidden_dim = hidden_dim
        self.n_heads = n_heads
        self.head_dim = hidden_dim // n_heads
        #creating y = wx + b network layer with hidden_dim -> hidden_dim
        self.fc_q = nn.Linear(hidden_dim, hidden_dim) #for query
        self.fc_k = nn.Linear(hidden_dim, hidden_dim) #for key 
        self.fc_v = nn.Linear(hidden_dim, hidden_dim) #for value

