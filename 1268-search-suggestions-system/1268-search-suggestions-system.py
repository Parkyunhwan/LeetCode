class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products = sorted(products)
        result = []
        sw = ""
        for i in range(len(searchWord)):
            sw += searchWord[i]
            li = []
            for pi in range(len(products)):
                currName = products[pi]
                diff = False
                k = 0
                if len(currName) <= i:
                    diff = True
                while k <= i and len(currName) > i:
                    if currName[k] != sw[k]:
                        diff = True
                        break
                    k += 1
                if not diff and len(li) < 3:
                    li.append(currName)
            result.append(li)
        return result
