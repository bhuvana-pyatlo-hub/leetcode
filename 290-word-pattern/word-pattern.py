class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words =s.split()
        if len(pattern)!=len(words):
            return False
        
        char_to_word={}
        word_to_char={}
        for cs,cword in zip(pattern,words):
            if cs in char_to_word:
                if char_to_word[cs]!=cword:
                    return False
            else:
                char_to_word[cs]=cword
            
            if cword in word_to_char:
                if word_to_char[cword] != cs:
                    return False
            else:
                word_to_char[cword]= cs
        return True
            

        