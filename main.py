def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    low_text = text.lower()
    ch = {}
    for i in low_text:
        if i in ch:
            ch[i] += 1
        else:
            ch[i] = 1
    return ch

def sort_on(dict):
    return dict["count"]

def report(text):
    report_list = []
    char_counts = count_characters(text)
    
    # Convert to list of dictionaries
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    
    # Sort by count
    char_list.sort(reverse=True, key=sort_on)
    
    # Create formatted report lines
    for char_dict in char_list:
        report_line = f"The '{char_dict['char']}' character was found {char_dict['count']} times"
        report_list.append(report_line)
    
    return report_list

def main():
    with open("/Users/amrouafi/workspace/github.com/amiroxx12/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
  
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()  # blank line
    for line in report(file_contents):
        print(line)
    print("--- End report ---")

main()