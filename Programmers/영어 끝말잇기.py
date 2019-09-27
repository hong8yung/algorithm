def solution(n, words):
    ex_words = []
    for idx, word in enumerate(words):
        if word in ex_words:
            return [(idx%n)+1, idx//n+1]
        if ex_words and word[0] != ex_words[-1][-1]:
            return [(idx%n)+1, (idx//n)+1]
        ex_words.append(word)
    else:
        return [0, 0]

n = [3, 5, 2]
words = [['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'], ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive'], ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']]

print(solution(n[0], words[0]))
print(solution(n[1], words[1]))
print(solution(n[2], words[2]))

#case0: [3, 3]
#case1: [0, 0]
#case2: [1, 3]
