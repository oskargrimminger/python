def lengthOfLongestSubstring(s):
        maxLen = 1
        if s == '':
            return 0                      
        for i in range(len(s)):
            substring = s[i]              
            for j in range(i+1, len(s)): 
                if s[j] not in substring: 
                    substring = substring + s[j]
                    maxLen = max(maxLen, len(substring))



                else:
                    break
        return maxLen

input_string = input("Enter your string: ")
result = lengthOfLongestSubstring(input_string)

print(result)