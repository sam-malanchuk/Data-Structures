lruTest = LRUCache(3)
lruTest.set("item1", "a")
lruTest.set("item2", "b")
lruTest.set("item3", "c")
lruTest.get("item1")
lruTest.set("item4", "d")

print(lruTest.get("a"))
