from index_t import BKTree
from edit_distance import EditDistance
from avl_tree import AVLTree

from flask import Flask, request
import json

app = Flask(__name__)

textSearch = {}

def main():
    # d = EditDistance(x,y)
    # print('D is')
    # print(d)
    f = open("./word_search.tsv", "r")
    lines = f.readlines()
    # ind = {}
    # tokenS = 'abcdefghijklmnopqrstuvwxyz'

    # for t in list(tokenS):
    #     ind[t] = BKTree(EditDistance)

    bkTree = BKTree(EditDistance)
    i = 0
    for line in lines:
        print("Line number %s" % str(i +1))
        print(line.replace('\n', '').split('\t'))
        token = line.replace('\n', '').split('\t')
        # ind[token[0][0]].add({ 'token': token[0], 'frequency': token[1]})
        i += 1
        bkTree.add({ 'token': token[0], 'frequency': token[1]})
        # bkTree.add(token[0])
    # return ind
    return bkTree

treeSearch = main()

@app.route('/search', methods=['GET'])
def getResults():
    """
        Return search results
    """

    searchQuery = request.args.get('word')

    if not searchQuery:
        return json.dumps([])

    t = AVLTree()

    treeSearch.search(searchQuery, 3, t)

    return json.dumps(t.inorder_traverse())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True)
