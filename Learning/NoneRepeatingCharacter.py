class none_repeat:
    def __init__(self):
        self.char_map = dict()

    
    def impl(self, char: str) -> int:

        for wd in char:
            val =  wd.lower()
            if val in self.char_map:
                self.char_map[val] += 1
            else:
                self.char_map[val] = 1

        return -1
    
    def get_result(self) -> str:
        for key, value in self.char_map.items():  
            if (value==1):
                return key
            
        return None


test = none_repeat()
test.impl("Ddton")
print('result> ',test.get_result())

test = none_repeat()
test.impl("aabbcc")
print('result> ',test.get_result())