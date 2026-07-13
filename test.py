
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    if len(strs)== 0 or len(strs) == 1: return [strs]
    def makeFreqMap(word: str) -> dict:
        freq_map = {}
        for w in word:
            count = word.count(w)
            freq_map[w] = count

        return freq_map
    
    map_list = []
    anagram_list = []
    ans_list = []
    for word in strs:
        w_map = makeFreqMap(word)
        map_list.append(w_map)
    

    for mp_idx_1 in range(len(map_list)): # eat, "tea", "ate", bat, cat, tab
        if map_list[mp_idx_1] == "": continue
        anagram_list.append(strs[mp_idx_1])

        for mp_idx_2 in range(1, len(map_list)):
            if (mp_idx_1 == mp_idx_2 or map_list[mp_idx_2] == "" 
                or map_list[mp_idx_1] != map_list[mp_idx_2]): continue
            
            anagram_list.append(strs[mp_idx_2])
            map_list[mp_idx_2] = ""
        ans_list.append(anagram_list)
        anagram_list = []
        
    return ans_list


string_list = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(string_list))