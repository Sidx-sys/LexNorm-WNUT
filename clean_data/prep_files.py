from tqdm import tqdm
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
            raw.append(p.clean(" ".join(tweet_raw)))
            norm.append(p.clean(" ".join(tweet_norm)))
            tweet_raw = []
            tweet_norm = []
        else:
            tokens = line.split()

            tweet_raw.append(tokens[0])
            tweet_norm.extend(tokens[1:])

with open('raw', 'w', encoding='utf-8') as f:
    for s in raw:
        f.write(s+'\n')

with open('gold', 'w', encoding='utf-8') as f:
    for s in norm:
        f.write(s+'\n')
