import sys
from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(" ")
        dictionary.sort(key = lambda i: len(i), reverse=False)
        for i,word in enumerate(words):
            for dict in dictionary:
                if dict == word[:len(dict)]:
                    words[i] = dict
                    break
        return " ".join(words)

    #字典树，就是构造树结构：
    def replaceWords1(self, dictionary: List[str], sentence: str) -> str:
        #构造树结构
        trie = {}
        for word in dictionary:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur['#'] = {}
        print(trie)
        words = sentence.split(' ')
        for i, word in enumerate(words):
            cur = trie
            for j, c in enumerate(word):
                if '#' in cur:
                    words[i] = word[:j]
                    break
                if c not in cur:
                    break
                cur = cur[c]
        return ' '.join(words)


if __name__ == '__main__':
    test = Solution()
    dictionary = ["catt","cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    print(test.replaceWords1(dictionary,sentence))

