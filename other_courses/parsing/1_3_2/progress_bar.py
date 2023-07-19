from time import sleep
from tqdm import tqdm

if __name__ == '__main__':
    for i in tqdm(range(2000)):
        sleep(0.003)