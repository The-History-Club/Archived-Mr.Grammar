import language_tool_python
import os

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(filename):
    with open(filename, 'r') as f:
        text = f.read()

    matches = tool.check(text)
    return matches

def print_error_message(filename, matches):
    print(f"Grammar check failed for file: {filename}")
    for match in matches:
        print(f"Error at offset {match.offset}: {match.message}")
        print(f"Context: {match.context}\n")

# Check the grammar of all .md and .txt files in the repository
if __name__ == '__main__':
    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename.endswith('.txt'):
                filepath = os.path.join(root, filename)
                matches = check_grammar(filepath)
                if matches:
                    print_error_message(filepath, matches)
                    exit(1)
