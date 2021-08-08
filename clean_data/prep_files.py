from tqdm import tqdm
import pickle
import subprocess
import preprocessor as p
p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.MENTION,
              p.OPT.HASHTAG, p.OPT.NUMBER)

# choosing the validation set for finding validation score
folder_path = '../Data/multilexnorm/data/'
file_path = 'en/dev.norm'
data_path = folder_path + file_path

raw = []
norm = []

with open(data_path, 'r') as f:
    tweet_raw = []
    tweet_norm = []
    for line in f:
        if line == '\n':
            raw.append(tweet_raw)
            norm.append(tweet_norm)
            tweet_raw = []
            tweet_norm = []
        else:
            tokens = line.split('\t')

            tweet_raw.append(tokens[0])
            tweet_norm.append(tokens[1].strip())

with open('raw.pkl', 'wb') as f:
    pickle.dump(raw, f)

with open('gold.pkl', 'wb') as f:
    pickle.dump(norm, f)
