        q = Queue()
        q.enqueue(node)
        
        while q.size > 0:
            node = q.dequeue()
            print(node.value)
            # node = None
            if node.left != None:
                q.enqueue(node.left)
            if node.right != None:
                q.enqueue(node.right)
