class HuffmanNode:
    def __init__(self, char, freq, is_leaf=True):
        """Initialization of node in Huffman Tree. 

        Args:
            char (_type_): Character found in input text. 
            freq (_type_): Frequency of character. 
            is_leaf (bool, optional): If current node is a leaf node. Defaults to True.
        """
        self.char = char 
        self.freq = freq
        self.is_leaf = is_leaf
        self.left = None
        self.right = None

    def __lt__(self, other):
        """_summary_

        Args:
            other (HuffmanNode): Other Huffman Node to compare to current node to determine precedence. 
        """
        if self.freq != other.freq:  # Frequency precedence.
            return self.freq < other.freq
        if self.is_leaf != other.is_leaf:  # Single letter precedence over multiple letter groups. 
            return self.is_leaf  
        return self.char < other.char # Alphabetical precedence. 


