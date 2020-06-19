# Code to develop the logic to make the logic of the swordfish
import functions as f

p11 = f.Cell(0, 3)
p11.posVal = set([3, 4])
p12 = f.Cell(0, 6)
p12.posVal = set([4, 5])

p21 = f.Cell(1, 1)
p21.posVal = set([3, 5])
p22 = f.Cell(1, 7)
p22.posVal = set([4, 5])

p31 = f.Cell(6, 0)
p31.posVal = set([1, 5, 6])
p32 = f.Cell(6, 1)
p32.posVal = set([4, 5, 6, 9])

p41 = f.Cell(5, 7)
p41.posVal = set([2, 5])
p42 = f.Cell(5, 8)
p42.posVal = set([2, 5])

p51 = f.Cell(8, 1)
p51.posVal = set([4, 5, 9])
p52 = f.Cell(8, 8)
p52.posVal = set([3, 5, 9])

p61 = f.Cell(8, 5)
p61.posVal = set([3, 4, 5])
p62 = f.Cell(8, 8)
p62.posVal = set([3, 5, 9])

p71 = f.Cell(5, 7)
p71.posVal = set([2, 5])
p72 = f.Cell(5, 8)
p72.posVal = set([2, 5])

p81 = f.Cell(8, 0)
p81.posVal = set([1, 5])
p82 = f.Cell(8, 7)
p82.posVal = set([1, 4, 5])

p91 = f.Cell(0, 0)
p91.posVal = set([5, 6])
p92 = f.Cell(0, 1)
p92.posVal = set([3, 5, 6])

p101 = f.Cell(1, 1)
p101.posVal = set([3, 5])
p102 = f.Cell(1, 5)
p102.posVal = set([3, 4])

p111 = f.Cell(6, 0)
p111.posVal = set([1, 5, 6])
p112 = f.Cell(6, 7)
p112.posVal = set([1, 2, 4, 5])

p121 = f.Cell(6, 1)
p121.posVal = set([4, 5, 6, 9])
p122 = f.Cell(6, 8)
p122.posVal = set([2, 5, 9])

p131 = f.Cell(0, 1)
p131.posVal = set([3, 5, 6])
p132 = f.Cell(0, 3)
p132.posVal = set([3, 4])

p141 = f.Cell(1, 5)
p141.posVal = set([3, 4])
p142 = f.Cell(1, 7)
p142.posVal = set([4, 5])

p151 = f.Cell(6, 7)
p151.posVal = set([1, 2, 4, 5])
p152 = f.Cell(6, 8)
p152.posVal = set([2, 5, 9])

p161 = f.Cell(7, 1)
p161.posVal = set([4, 5])
p162 = f.Cell(7, 3)
p162.posVal = set([3, 4])

p171 = f.Cell(7, 1)
p171.posVal = set([4, 5])
p172 = f.Cell(7, 8)
p172.posVal = set([3, 5])

p181 = f.Cell(7, 3)
p181.posVal = set([3, 4])
p182 = f.Cell(7, 8)
p182.posVal = set([3, 5])


pairs = set([
    # 4, 5, 6, 2, 9,
    (p11, p12, 4),
    (p21, p22, 5),
    (p31, p32, 6),
    (p41, p42, 2),
    (p51, p52, 9),
    
    # 3, 5, 1, 6, 3,
    (p61, p62, 3),
    (p71, p72, 5),
    (p81, p82, 1),
    (p91, p92, 6),
    (p101, p102, 3),

    # 1, 9, 3, 4, 2,
    (p111, p112, 1),
    (p121, p122, 9),
    (p131, p132, 3),
    (p141, p142, 4),
    (p151, p152, 2),
    
    # 4, 5, 3
    (p161, p162, 4),
    (p171, p172, 5),
    (p181, p182, 3)
    ])


def swordfish(v, pairs, iniPos, currentPos, cellToPos, used=[]):
    # print("Iteration")
    if len(pairs) == 0:
        return None
    if iniPos == currentPos:
        if len(used) == 1: return None # If here, this is a double pair => nope
        return used + [iniPos]
    for p in pairs:
        if p[2] != v: continue # if different value, 
        if currentPos == cellToPos(p[0]): # If I can continue this path
            return swordfish(v, pairs - set([p]), iniPos, cellToPos(p[1]), cellToPos, used + [currentPos])
        
        elif currentPos == cellToPos(p[1]): # If I can continue this path
            return swordfish(v, pairs - set([p]), iniPos, cellToPos(p[0]), cellToPos, used + [currentPos])
    # If here, not possible
    return None


# What I Know:

# If this proccess is correct, it doesn't matter the way you circle the pairs


# print(len(pairs))
# print(len(pairs - set([(p11, p12, 4)])))
for p in pairs:
    result = swordfish(p[2], pairs - set(p), p[0].y, p[1].y, lambda x: x.y)
    if result != None:
        print(str(result) + " -> start = " + str(p[0].getPos()) + "; value: " + str(p[2]))