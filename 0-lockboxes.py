#!/usr/bin/python3

def canUnlockAll(boxes):
    if len(boxes) == 1:
        return True
    if len(boxes[0]) == 0:
        return False
    keys = boxes[0]
    for i in range(len(keys) - 1):
        if keys[i] > len(boxes) -1:
            keys.pop(i)
    keys2 = []
    while not len(keys) > len(boxes) - 1 and keys2 != keys:
        keys2 = keys.copy()
        for i in range(len(keys2)):
            keys += boxes[keys2[i]]
            keys = list(set(keys))
    for i in range (len(keys) - 1):
        if keys[i] == 0:
            keys.pop(i)
    if len(keys) == len(boxes) - 1:
        return True
    return False 