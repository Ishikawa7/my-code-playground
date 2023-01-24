
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#Each letter in magazine can only be used once in ransomNote.
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    ransomNote_list = list(ransomNote)
    ransomNote_list.reverse()
    magazine_list = list(magazine)
    while len(ransomNote_list) > 0 and len(magazine_list) > 0:
        l = ransomNote_list.pop()
        if l in magazine_list:
            magazine_list.remove(l)
        else:
            return False
    if len(ransomNote_list) == 0:
        return True
    else:
        return False