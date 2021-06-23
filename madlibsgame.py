# MADLIBS using string concatenation

from sample_madlibs import zombie, lum
import random

if __name__ == '__main__':
    m = random.choice([lum, zombie])
    m.madlib()