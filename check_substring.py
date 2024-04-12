def find_substring(main_string, substring):
    # Loop through the main string
    for i in range(len(main_string)):
        # Check if the substring matches starting from index i
        if main_string[i:i+len(substring)] == substring:
            return i
    # Substring not found
    return -1

# Example usage:
main_string = "hello world"
substring = "world"
index = find_substring(main_string, substring)
if index != -1:
    print("Substring found at index:", index)
else:
    print("Substring not found")








'''

s = 'helloyou'
    '01234567'


#gives the index
print(s.find('you'))


'''