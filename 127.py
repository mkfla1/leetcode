###
bfs
###

import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet: return 0


        queue = collections.deque([beginWord])
        visited = set([beginWord])
        graph = {}
        length = 0

        while queue:
            length += 1 
            for _ in range(len(queue)):
                curt = queue.popleft()
                self.lazy_load(curt, wordSet, graph)
                for neighbor in graph[curt]:
                    if neighbor == endWord:
                        return length + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return 0
    
    def lazy_load(self, curt, wordSet, graph):
        if curt in graph: return
        graph[curt] = []
        letters = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(curt)):
            for letter in letters:
                if curt[i] == letter: continue
                new_word = curt[:i] + letter + curt[i + 1:]
                if new_word in wordSet:
                    graph[curt].append(new_word)
        return
        
        
###
双向bfs
###
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        words.add(beginWord)
        if endWord not in words: return 0
        graph = {}

        forward_queue = collections.deque([beginWord])
        forward_visited = set([beginWord])
        backward_queue =  collections.deque([endWord])
        backward_visited = set([endWord])

        length = 1
        while forward_queue and backward_queue:
            length += 1
            if self.bfs(forward_queue, forward_visited, backward_visited, graph, words):
                return length
            length += 1
            if self.bfs(backward_queue, backward_visited, forward_visited, graph, words):
                return length
        return 0
    
    def bfs(self, queue, visited, reverse_visited, graph, words):
        for _ in range(len(queue)):
            curt = queue.popleft()
            self.lazy_load(curt, graph, words)
            for neighbor in graph[curt]:
                if neighbor in reverse_visited:
                    return True
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        return False
    
    def lazy_load(self, curt, graph, words):
        if curt in graph: return
        graph[curt] = []
        letters = "abcdefghijklmnopqrstuvwxyz"

        for i in range(len(curt)):
            for letter in letters:
                if curt[i] == letter: continue
                new_word = curt[:i] + letter + curt[i + 1:]
                if new_word in words:
                    graph[curt].append(new_word)
        return
