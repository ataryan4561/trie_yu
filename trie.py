class TrieNode:
    def __init__(self,char=''):
        self.children = [None]*26
        self.is_end_word = False
        self.char = char

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self,t):
        return ord(t)-ord('a')

    def insert(self,key):
        if key is None:
            return False
        key = key.lower()
        current = self.root
        for letters in key:
            index = self.get_index(letters)
            if current.children[index] is None:
                current.children[index] = TrieNode(letters)
            
            current = current.children[index]

        current.is_end_word = True

    def search(self,key):
        if key is None:
            return False
        key = key.lower()
        current = self.root
        for letters in key:
            index = self.get_index(letters)
            if current.children[index] is None:
                return False
            current = current.children[index]

        if current is not None and current.is_end_word:
            return True
        return False

    def delete_helper(self, key, current, length, level):
        deleted_self = False

        if current is None:
            print("Key does not exist")
            return deleted_self

        # Base Case:
        # We have reached at the node which points
        # to the alphabet at the end of the key
        if level is length:
            # If there are no nodes ahead of this node in
            # this path, then we can delete this node
            print("Level is length, we are at the end")
            if current.children.count(None) == len(current.children):
                print("- Node", current.char, ": has no children, delete it")
                current = None
                deleted_self = True

            # If there are nodes ahead of current in this path
            # Then we cannot delete current. We simply unmark this as leaf
            else:
                print("- Node", current.char, ": has children, don't delete \
                it")
                current.is_end_word = False
                deleted_self = False

        else:
            index = self.get_index(key[level])
            print("Traverse to", key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(
                key, child_node, length, level + 1)
            # print( "Returned from", key[level] , "as",  child_deleted)
            if child_deleted:
                # Setting children pointer to None as child is deleted
                print("- Delete link from", current.char, "to", key[level])
                current.children[index] = None
                # If current is a leaf node then
                # current is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current.is_end_word:
                    print("- - Don't delete node", current.char, ": word end")
                    deleted_self = False

                # If child_node is deleted and current has more children
                # then current must be part of another key
                # So, we cannot delete current Node
                elif current.children.count(None) != len(current.children):
                    print("- - Don't delete node", current.char, ": has \
                    children")
                    deleted_self = False

                # Else we can delete current
                else:
                    print("- - Delete node", current.char, ": has no children")
                    current = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            print("None key or empty trie error")
            return
        print("\nDeleting:", key)
        self.delete_helper(key, self.root, len(key), 0)

        
def total_words(root):
	result = 0
	if root.is_end_word:
		result += 1

	for letter in root.children:
		if letter is not None:
			result += total_words(letter)
	return result

def helper(root,ans,l):
    if root.is_end_word:
        l=l+root.char
        ans.append(l)
    for letter in root.children:
        if letter is not None:
            if root.is_end_word:
                helper(letter,ans,l)
            else:
                helper(letter,ans,l+root.char)

def find_words(root):
    ans = list()
    helper(root,ans,'')
    return ans

def get_words(root, result, level, word):
    # Leaf denotes end of a word
    if (root.is_end_word):
        # Current word is stored till the 'level' in the character array
        temp = ""
        for x in range(level):
            temp += word[x]
        result.append(temp)

    for i in range(26):
        if (root.children[i] is not None):
            # Non-null child, so add that index to the character array
            word[level] = chr(i + ord('a'))
            get_words(root.children[i], result, level + 1, word)


def sort_list(trie):
    result = []
    word = [''] * 20
    get_words(trie.root, result, 0, word)
    return result

def is_formation_possible(dictionary, word):

    # Create Trie and insert dictionary elements in it
    trie = Trie()
    for elem in dictionary:
        trie.insert(elem)

    # Get root
    current = trie.root

    # Iterate all the letters of the word
    for i in range(len(word)):
        # get index of the character from Trie
        char = trie.get_index(word[i])

        # Return FALSE if the prefix of word does not exist
        if current.children[char] is None:
            return False

        # If the substring of the word exists as a word in trie,
        # check whether rest of the word also exists,
        # if it does return true
        elif current.children[char].is_end_word:
            if trie.search(word[i+1:]):
                return True

        current = current.children[char]

    return False


