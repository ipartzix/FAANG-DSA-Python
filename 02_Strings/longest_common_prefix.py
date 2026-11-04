class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Iterate through each character of the first string\\
        for i in range(len(strs[0])):

            # Take the character at the current index
            char = strs[0][i]

            # Compare this character with the same index
            # in all the remaining strings
            for s in strs[1:]:

                # If the current string is shorter than index i
                # OR the character does not match
                if i == len(s) or s[i] != char:

                    # Return the common prefix found so far
                    return strs[0][:i]

        # If all characters match in every string,
        # return the entire first string
        return strs[0]
