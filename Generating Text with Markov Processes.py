# Source: https://www.reddit.com/r/dailyprogrammer/comments/4n6hc2/20160608_challenge_270_intermediate_generating/
# NOTE: NOT MY WORK. BORROWED TO TEST IT.
# Original work from: https://www.reddit.com/r/dailyprogrammer/comments/4n6hc2/20160608_challenge_270_intermediate_generating/d41cve9/

from collections import defaultdict
import random
import sys


def ngrams(it, n):
    it = iter(it)
    ngram = list(next(it) for i in range(n))
    while len(ngram) == n:
        yield ngram
        ngram = ngram[1:] + [next(it)]


def markov_graph(input_file):
    graph = defaultdict(list)
    words = (word for line in input_file for word in line.split())
    for a, b, c in ngrams(words, 3):
        graph[a, b].append(c)
    return graph


def stream_markov(graph):
    all_words = [word for v in graph.values() for word in v]
    a, b = random.sample(all_words, 2)
    while True:
        a, b = b, random.choice(graph[a, b] or all_words)
        final = b.endswith('.') and random.random() < 0.1
        print(b, end='\n\n' if final else ' ')


if __name__ == '__main__':
    stream_markov(markov_graph(sys.stdin))
