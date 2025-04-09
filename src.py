from HuffmanNode import HuffmanNode
import heapq
import re 

def build_huffman_tree(heap:list) -> list: 
    """Builds Huffman Tree from pritority queue list. 

    Args:
        heap (list): Input heap from which to construct the Huffman Tree. 

    Returns:
        list: Huffman Tree. 
    """
    while len(heap) > 1: 
        # Get the 2 top nodes in the heap 
        node_1 = heapq.heappop(heap)
        node_2 = heapq.heappop(heap) 

        # Merge the 2 nodes 
        char = node_1.char + node_2.char  # Combine symbols. 
        freq = node_1.freq + node_2.freq  # Add frequencies. 
        is_leaf = False  # Multiple letter groups are never leaf nodes. 
        merged = HuffmanNode(char, freq, is_leaf)

        # Set the 2 nodes as children of merged node
        merged.left = node_1
        merged.right = node_2

        # Put merged node into the heap 
        heapq.heappush(heap, merged)

    return heap 


def huffman_codes(huffman_node:HuffmanNode, code:str='', codes_dict:dict={}) -> dict:
    """Generates a dictionary containing the codes for the characters in the Huffman tree with keys sorted alphabetically. 

    Args:
        node (HuffmanNode): Current node in Huffman Tree. 
        code (str, optional): Code for the current node. Defaults to ''.
        codes_dict (dict, optional): Contains the codes for nodes in Huffman Tree. Defaults to {}.  

    Returns:
        dict: Contains the codes for all nodes in Huffman Tree, with keys sorted alphabetically. 
    """
    def huffman_codes_unsorted(node:HuffmanNode, code:str='', codes_dict:dict={}) -> dict: 
        """Generates a dictionary containing the codes for the characters in the Huffman tree. 

        Args:
            node (HuffmanNode): Current node in Huffman Tree. 
            code (str, optional): Code for the current node. Defaults to ''.
            codes_dict (dict, optional): Contains the codes for nodes in Huffman Tree. Defaults to {}.

        Returns:
            dict: Contains the codes for all nodes in Huffman Tree
        """
        if node is None:  # Base case. When to terminate recursion. 
            return 
        
        if node.is_leaf:  
            codes_dict[node.char] = code

        huffman_codes_unsorted(node.left, code + '0', codes_dict)  # Recursively traverse left subtrees (0). 
        huffman_codes_unsorted(node.right, code + '1', codes_dict)  # Recursively traverse right subrees (1).

        return codes_dict

    huffman_codes_dict = huffman_codes_unsorted(huffman_node)  # Start at the root node of the Huffman Tree (heap[0])
    sorted_code_keys = sorted(huffman_codes_dict.keys())  # Sort huffman_codes_dict so keys are alphabetical 
    return {key: huffman_codes_dict[key] for key in sorted_code_keys}


def preorder_traversal(huffman_node:HuffmanNode) -> None:
    """Prints a preorder traversal of the Huffman Tree. 

    Args:
        huffman_node (HuffmanNode): Node of Huffman Tree. 
    """
    if huffman_node is None:  # Base case, when to terminate recursion 
        return 

    print(f"{huffman_node.char} ({huffman_node.freq})")  # Current node 

    preorder_traversal(huffman_node.left)  # Traverse left subtree 
    preorder_traversal(huffman_node.right)  # Traverse right subtree 


def encode_string(input_string:str, codes_dict:dict) -> str:
    """Encodes alphabetical string into binary using the Huffman Tree code dictionary (ourput of huffman_codes() function).

    Args:
        input_string (str): Input alphabetical string to encode. 
        codes_dict (dict): Huffman code. 

    Returns:
        str: Binary encoded form of input_string. 
    """
    input_string = input_string.upper()  # Make all characters uppercase to match keys in codes_dict. 
    encoded_string = "".join(codes_dict[char] for char in input_string if char in codes_dict)  # Replace alphabetical chars with corresponding Huffman code. 
    return encoded_string


def decode_string(input_string, codes_dict):
    pass


def is_binary(input_string:str) -> bool: 
    """Determine if input string is a binary expression (contains only 0s and 1s). 

    Args:
        input_string (str): Input string. 

    Returns:
        bool: True if input string is binary expression. 
    """
    return set(input_string).issubset({'0', '1'})

# def clean_up_input(input_string:str) -> str:
#     """Removes all characters that are not alphabetic (spaces, punctuation, numbers). Also all characters are changed to upper case to match keys in Huffman Code. 

#     Args:
#         input_string (str): Input string. May contain alphanumeric characters, spaces, and punctuation. 

#     Returns:
#         str: Input string with numeric characters, spaces, and punctuation removed.
#     """
#     return re.sub(r'[^a-zA-Z]', '', input_string.upper())
