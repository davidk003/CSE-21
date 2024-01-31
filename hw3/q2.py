import random


class Bud:
    branch1 = None
    branch2 = None
    isFlower = False
    treeList = None

    def __init__(self, inputList):
        self.treeList = inputList
        

    def growOneBranch(self):
        self.branch1 = Bud(self.treeList)
        self.treeList.append(self.branch1)


    def growTwoBranch(self):
        self.branch1 = Bud(self.treeList)
        self.treeList.append(self.branch1)
        self.branch2 = Bud(self.treeList)
        self.treeList.append(self.branch2)
        

    def growFlower(self):
        self.isFlower = True
        if self.branch1 or self.branch2:
            print("this shouldn't have branches")


def chooseGrowth(bud):
    if not bud.isFlower and not (bud.branch1 or bud.branch2):
        gen = random.random()
        if gen < 0.30:
            bud.growFlower()
            # print("flowa")
        elif gen < 0.55:
            bud.growTwoBranch()
            # print("two")
        else:
            bud.growOneBranch()
            # print("one")

TEST_ATTEMPTS = 1_000_000
oneBranch = 0
twoBranch = 0
flower = 0
inputList = []
test = []
for i in range(TEST_ATTEMPTS):
    test.append(Bud(inputList))
for b in test:
    chooseGrowth(b)
    if b.isFlower:
        flower+=1
    elif b.branch1 and b.branch2:
        twoBranch+=1
    else:
        oneBranch+=1
print(f"one branch: {oneBranch}\n two branches: {twoBranch}\n flower: {flower}")
print(f"one branch: {oneBranch/TEST_ATTEMPTS}\n two branches: {twoBranch/TEST_ATTEMPTS}\n flower: {flower/TEST_ATTEMPTS}")
assert(oneBranch+twoBranch+flower == TEST_ATTEMPTS)

# def countTree(bud, oneBranch, twoBranch, flowers, buds):
#     if bud.branch1:
#         countTree(bud.branch1,oneBranch, twoBranch, flowers, buds)

#     if bud.isFlower:
#         flowers+=1
#     elif bud.branch1 and bud.branch2:
#         twoBranch+=1
#     elif bud.branch1 != bud.branch2:
#         oneBranch+=1
#     else:
#         buds+=1
    
#     if bud.branch2:
#         countTree(bud.branch2,oneBranch, twoBranch, flowers, buds)
#     print(f"one branch: {oneBranch}\n two branches: {twoBranch}\n flowers: {flowers} \n buds: {buds}")

def growTree(bud):
    if bud.branch1:
        growTree(bud.branch1)
    chooseGrowth(bud)
    if bud.branch2:
        growTree(bud.branch2)

testList = []
testing = Bud(testList)
for i in range(5):
    growTree(testing)
print(testList)


# testTree = Bud()
# for i in range(5):
#     growTree(testTree)
#     countTree(testTree,0,0,0,0)



