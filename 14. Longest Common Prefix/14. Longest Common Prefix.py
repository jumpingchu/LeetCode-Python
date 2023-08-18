def longestCommonPrefix(self, strs: List[str]) -> str:
    """
    1. 計算最短的單字（提升速度），收集每個單字中各個位置的字母，並串起來
        
        strs = ["flower","flow","flight"]
        min_len = 4
        str_freq = {"0":"fff", "1":"lll", "2":"ooi", "3":"wwg"}
    
    2. 把字母去重複，找出長度只有 1 的，代表這個字母三個都有重複出現
    3. 並且在找的過程一旦遇到長度不是 1 的就直接 break（以防後面滿足條件的字母也被加進去）

        for combined_str in str_freq.values():
            if len(set(combined_str)) == 1:
                max_str += combined_str[0]
            else:
                break
    
    Return:
        max_str = 'fl'
    """
    str_freq = {} 
    min_len = len(min(strs, key=len))
    for word in strs:
        for i, w in enumerate(word[:min_len]):
            if i not in str_freq:
                str_freq[i] = word[i]
            else:
                str_freq[i] += w
    
    max_str = ''
    for combined_str in str_freq.values():
        if len(set(combined_str)) == 1:
            max_str += combined_str[0]
        else:
            break
    return max_str

# Great Answer to me
# Runtime: 27ms
# Beats 99.80%
def longestCommonPrefix(self, strs: List[str]) -> str:
    # zip return a iterator which can only be iterated ONCE!
    # Can use `list(zip())` for iterating more than once.
    s = zip(*strs)
    ans = ''
    for x in s:
        res = set(x)
        if len(res) == 1:
            # Python's `set.pop()` randomly removes an element and returns the removed element.
            ans += res.pop()
        else:
            break
    return ans
