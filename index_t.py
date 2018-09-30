from collections import deque

RANK = 1000000000000

class BKTree:
    def __init__(self, distance_func):
        self._tree = None
        self._distance_func = distance_func

    def add(self, node):
        if self._tree is None:
            self._tree = (node, {})
            return
        
        current, children = self._tree
        while True:
            dist = self._distance_func(node['token'], current['token'])
            target = children.get(dist)
            if target is None:
                children[dist] = (node, {})
                break
            current, children = target

    def search(self, node, radius, a):
        if self._tree is None:
            return []
        
        candidates = deque([self._tree])
        result = []
        hits = 0
        while candidates:
            candidate, children = candidates.popleft()
            candidateRank = 0
            isSubStr = candidate['token'].find(node)
            # compute distance if there is no substring match
            if isSubStr == -1:
                dist = self._distance_func(node, candidate['token'])
                candidateRank += int(candidate['frequency'])
                if dist <= radius:
                    result.append((dist, candidate))
                    a.insert({'key': candidateRank, 'token': candidate['token']})
                low, high = dist - radius, dist + radius
                candidates.extend(c for d, c in children.items() if low <= d <= high)
            else:
                dist = 0
                low, high = dist - radius, dist + radius
                if isSubStr == 0:
                    candidateRank += RANK
                else:
                    candidateRank += RANK / isSubStr

                # Length
                lenDiff = len(candidate['token']) - len(node)
                if lenDiff == 0:
                    candidateRank += RANK
                else:
                    candidateRank += RANK / lenDiff
                a.insert({'key': candidateRank, 'token': candidate['token']})
                result.append((0, candidate))
                candidates.extend(c for d, c in children.items() if low <= d <= high)
        return result
