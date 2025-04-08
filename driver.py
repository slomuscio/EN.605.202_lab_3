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
    heap = build_huffman_tree(heap)

    # Get the codes from the Huffman Tree 
    # Start at the root node of the Huffman Tree (heap[0])
    huffman_codes_dict = huffman_codes(heap[0])
    # Sort huffman_codes_dict so keys are alphabetical 
    sorted_code_keys = sorted(huffman_codes_dict.keys())
    sorted_huffman_codes_dict = {key: huffman_codes_dict[key] for key in sorted_code_keys}

    print(sorted_huffman_codes_dict)

    # Generate codes for the input cases contained in input_output/input.txt file. 
    with open(input_file, 'r') as input_f:

        for input_string in input_f:

            if len(input_string)==0:  # Skip empty lines in the input file. 
                continue 

            encoded_string = encode_string(input_string, sorted_huffman_codes_dict)
            print(f"INPUT STRING:\t{input_string}\nENCODED_STRING:\t{encoded_string}")


if __name__=="__main__":
    main()
