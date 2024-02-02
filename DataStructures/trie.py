class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    # the add method takes a string as input and adds it to the trie
    def add (self, word):
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current[self.end_symbol] = True

    # the exists method takes a string as input and returns true if the 
    # string exists in the trie, and false if it does not
    def exists(self, word):
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return self.end_symbol in current
    
    # words with prefix and search level are used together to take in a 
    # prefix as input and returns a list of words that share that prefix
    def words_with_prefix(self, prefix):
        result = []
        current = self.root
        for char in prefix:
            if char not in current:
                return []
            current = current[char]
        self.search_level(current, prefix, result)
        return result
    
    def search_level(self, cur, cur_prefix, words):
        if self.end_symbol in cur:
            words.append(cur_prefix)
        for char in sorted(cur.keys()):
            if char != self.end_symbol:
                self.search_level(cur[char], cur_prefix + char, words)
            return words
        
    # find_matches takes an entire document as input and returns a set() 
    # of all the words in the trie that exist in the document as continuous substrings.
    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i, len(document)):
                ch = document[j]
                if ch not in level:
                    break
                level = level[ch]
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
        return matches
    
    # longest_common_prefix takes no input other than "self", it operates on the trie itself,
    # and returns the longest common prefix between all words in the trie
    def longest_common_prefix(self):
        current = self.root
        prefix = ""
        while True:
            children = []
            for key in current.keys():
                if key != self.end_symbol:
                    children.append(key)
            if len(children) == 1:
                prefix += children[0]
                current = current[children[0]]
            else:
                break
        return prefix
    
    # advanced_find_matches is an advanced word filter that can catch variations of bad words efficiently.
    # for example, if the bad word id "darn", we want to filter variations like 'd@rn', 'd4rn', or 'd@rn1t'
    def advanced_find_mathces(self, document, variations):
        matches = set()
        for i in range(len(document)):
            level = self.root
            for j in range(i,  len(document)):
                ch = document[j]
                if ch in variations:
                    ch = variations[ch]
                if ch in level:
                    level = level[ch]
                else:
                    level = self.root
                    break
                if self.end_symbol in level:
                    matches.add(document[i : j + 1])
