import re

# Function to read data from an input file
def read_input_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Function to remove excess space and comments from the code
def process_code(code):
    # Remove comments
    code = re.sub(r'#.*', '', code)
    # Remove excess whitespace
    code = re.sub(r'\s+', ' ', code)
    return code

# Function to tokenize the remaining code
def tokenize_code(code):
    tokens = re.findall(r'\b\w+\b', code)
    return tokens

# Function to print the code after processing
def print_processed_code(code):
    print("Output1 - Code after removing excess space and comments:\n")
    print(code)

# Function to print tokenized code in tabular form
def print_tabular_form(tokens):
    print("\nOutput2 - Tokenized code in tabular form:\n")
    categories = {
        "Keywords": ["def", "return", "print"],
        "Identifiers": [],
        "Operators": ["=", "+"],
        "Delimiters": ["(", ")", ":", ","],
        "Literals": []
    }
    token_table = {}
    for token in tokens:
        categorized = False
        for category, keywords in categories.items():
            if token in keywords:
                if category in token_table:
                    token_table[category].append(token)
                else:
                    token_table[category] = [token]
                categorized = True
                break
        if not categorized:
            if "Identifiers" in token_table:
                token_table["Identifiers"].append(token)
            else:
                token_table["Identifiers"] = [token]
    max_category_length = max(len(category) for category in token_table.keys())
    for category, tokens in token_table.items():
        print(f"{category:<{max_category_length}}: {', '.join(tokens)}")

# Sample usage:
tokens = ['def', 'add', '(', 'a', ',', 'b', ')', ':', 'result', '=', 'a', '+', 'b', 'return', 'result', '=', 'a', '+', 'b', 'return', 'result', 'print', '(', '5', ',', '3', ')']
print_tabular_form(tokens)


# Main function
def main():
    # Read data from input file
    input_code = read_input_file("input.txt")

    # Process the code
    processed_code = process_code(input_code)

    # Tokenize the code
    tokens = tokenize_code(processed_code)

    # Print processed code
    print_processed_code(processed_code)

    # Print tokenized code in tabular form
    print_tabular_form(tokens)

if __name__ == "__main__":
    main()
