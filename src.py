from HuffmanNode import HuffmanNode
import heapq
import re 

def build_huffman_tree(heap): 
    while len(heap) > 1: 
        # Get the 2 top nodes in the heap 
        node_1 = heapq.heappop(heap)
        node_2 = heapq.heappop(heap) 

        # Merge the 2 nodes 
        char = node_1.char + node_1.char  # Combine symbols. 
        freq = node_1.freq + node_2.freq  # Add frequencies. 
        is_leaf = False  # Multiple letter groups are never leaf nodes. 
        merged = HuffmanNode(char, freq, is_leaf)

        # Set the 2 nodes as children of merged node
        merged.left = node_1
        merged.right = node_2

        # Put merged node into the heap 
        heapq.heappush(heap, merged)

    return heap 


def huffman_codes(node:HuffmanNode, code:str='', codes_dict:dict={}) -> dict: 
    """Generates a dictionary containing the codes for the characters in the Huffman tree. 

    Args:
        node (HuffmanNode): Current node in Huffman Tree. 
        code (str, optional): Code for the current node. Defaults to ''.
        codes_dict (dict, optional): Contains the codes for nodes in Huffman Tree. Defaults to {}.

    Returns:
        dict: Contains the codes for all nodes in Huffman Tree
    """
    if node is None: 
        return 
    
    if node.is_leaf: 
        codes_dict[node.char] = code

    huffman_codes(node.left, code+'0', codes_dict)  # Recursively traverse left subtrees (0). 
    huffman_codes(node.right, code+'1', codes_dict)  # Recursively traverse right subrees (1).

    return codes_dict


def prefix_traversal(huffman_tree):
    pass 


def encode_string(input_string, codes_dict):
    # encoded_string = ""
    input_string = input_string.upper()
    encoded_string = "".join(codes_dict[char] for char in input_string if char in codes_dict)
    return encoded_string


def decode_string(input_string, codes_dict):
    pass

def clean_up_input(input_string:str) -> str:
    """Removes all characters that are not alphabetic (spaces, punctuation, numbers). Also all characters are changed to upper case to match keys in Huffman Code. 

    Args:
        input_string (str): Input string. May contain alphanumeric characters, spaces, and punctuation. 

    Returns:
        str: Input string with numeric characters, spaces, and punctuation removed.
    """
    return re.sub(r'[^a-zA-Z]', '', input_string.upper())
