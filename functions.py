import re
def sortKeyword(filename):
    
    keywords = []
    
    #lists used during sorting
    preKeywords = []
    andList = []
    andListNew = []
    
    #sorts into AND and not AND sections
    with open(filename, 'r') as f:
        for line in f:
            for word in re.split('\(\(|\)\)',line):
                if str(word).find('AND') > 0:
                    andList.append(str(word))
                elif word != ' OR ':
                    preKeywords.append(word)
                    
    #sorts the non AND section and appends the final product to keywords
    for x in preKeywords:
        for x in (x.split(' OR ')):
            if x != '':            
                keywords.append(str(x.replace("\"","")))
                
    #sorts the AND section into groups            
    for x in andList:
        for y in x.split(' AND '):
            andListNew.append(y.replace("(","").replace(")","").replace("\"","").split(" OR "))
         
    #sorts the AND section groups and appends the final product to keywords
    x = 0
    while x < len(andListNew):
        if x % 2 == 0:
            for z in andListNew[x]:
                for y in range(len(andListNew[x + 1])):
                    keywords.append((z + ' ' + andListNew[x + 1][y]))
        x += 1        
        
    return keywords