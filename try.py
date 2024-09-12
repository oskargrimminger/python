def find_shortest_length(strings):
    return len(min(strings, key=len))
  
def all_contain_prefix(strings, prefix, start, end):
    for i in range(0, len(strings)):
        word = strings[i]
        for j in range(start, end + 1):
            if word[j] != prefix[j]:
                return False
    return True
  
def find_longest_common_prefix(strings):
    shortest_length = find_shortest_length(strings)
    common_prefix = ""   
  
    low, high = 0, shortest_length - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if all_contain_prefix(strings, strings[0], low, mid):
            common_prefix = common_prefix + strings[0][low:mid + 1]
            low = mid + 1
        else: 
            high = mid - 1
  
    return common_prefix

if __name__ == "__main__":
    strings_list = input("Enter string list: ")
    result = find_longest_common_prefix(strings_list)
