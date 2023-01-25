import bisect
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        # 1. 정렬을 하면 검색을 단순화할 수 있다. (검색안되는 것 이후의 것은 모두 검색안됨)
        products = sorted(products)
        result = []
        # 2. 모든 검색글자에 대해 최대3개까지 조건에 맞는 단어를 보여줌
        currSearchWord = ""
        idx = 0
        for ch in searchWord:
            currList = []
            currSearchWord += ch
            # 정렬된 리스트에서 현재 검색글자가 들어갈만한 위치를 bisect로 구한다.
            idx = bisect.bisect_left(products, currSearchWord, idx) # idx까지가 검색가능한 단어의 첫 시작 idx라고 볼수 있다.
            for p in products[idx:idx + 3]:
                if p.startswith(currSearchWord):
                    currList.append(p)
            result.append(currList)
        return result
            
            
            