import heapq
from HuffmanNode import HuffmanNode
from src import * 

def main(): 
    import os 
    import sys 

    current_file_path = os.path.dirname(os.path.abspath(__file__))  # Find the path to this file.
    os.chdir(current_file_path)  # cd to the directory containing this file.

    input_file = os.path.join(current_file_path, "input_output", "input.txt")
    output_file = os.path.join(current_file_path, "input_output", "output.txt") 

    frequency_table = {"A": 19, 
                    "B": 16,
                    "C": 17, 
                    "D": 11, 
                    "E": 47, 
                    "F": 12, 
                    "G": 14,
                    "H": 17, 
                    "I": 16, 
                    "J": 5,
                    "K": 10,
                    "L": 20, 
                    "M": 19, 
                    "N": 24,
                    "O": 18,
                    "P": 13,
                    "Q": 1, 
                    "R": 25, 
                    "S": 35, 
                    "T": 25, 
                    "U": 15, 
                    "V": 5, 
                    "W": 21,
                    "X": 2, 
                    "Y": 8,
                    "Z": 3,
                    }
 
    # Make heap from frequency table
    heap = []
    for char, freq in frequency_table.items(): 
        heapq.heappush(heap, HuffmanNode(char, freq))

    # Make Huffman Tree using the heap
    huffman_tree = build_huffman_tree(heap)

    # Print preorder traversal of tree
    preorder_traversal(huffman_tree[0])

    # Get the codes from the Huffman Tree 
    huffman_codes_dict = huffman_codes(huffman_tree[0])  # Start at the root node of the Huffman Tree (heap[0])
    print(huffman_codes_dict)

    # Generate codes for the input cases contained in input_output/input.txt file. 
    with open(input_file, 'r') as input_f:

        for input_string in input_f:

            input_string = input_string.replace(' ', '')  # Remove all spaces from the input strings. 
                                                          # NOT SURE IF THIS IS THE BEST WAY TO GO ABOUT THIS. will think about it more. Maybe better clean_up_input() function? 

            if len(input_string)==0:  # Skip empty lines in the input file. 
                continue 

            if is_binary(input_string):  # Decode the string if it is binary expression. 
                print(f"INPUT STRING: {input_string}")
                print("---BINARY STRING, MUST DECODE---\n")
                # decode_string()
            else:  # Encode the string if it is not a binary expression. 
                encoded_string = encode_string(input_string, sorted_huffman_codes_dict)
                print(f"INPUT STRING:\t{input_string}\nENCODED_STRING:\t{encoded_string}\n")


if __name__=="__main__":
    main()
