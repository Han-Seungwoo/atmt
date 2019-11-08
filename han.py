import truecase
from bpe import Encoder
from tokenizer import tokenize, TOK

def make_truecase(text):
  for s in text:
    truecase = truecase.get_true_case(s)
  return truecase


def make_bpe(text):
  encoder = Encoder(200, pct_bpe=0.88)
  bpe = encoder.fit(text.split('\n'))
  return bpe

def make_token(text):
  for s in text:
    token = tekenize(s)
  return token



