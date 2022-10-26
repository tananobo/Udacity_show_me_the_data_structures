I referred https://www.callicoder.com/design-lru-cache-data-structure/ based on MENTORS HELP comment

This problem_1.py code works as LRU_Cache. To use this, firstly define LRU_Cache class with size like our_cache = LRU_Cache(size=5).
When you set a item to the cache, call set function with key and value, like our_cache.set(key=1,value=1).
When you get a item from the cache, call get function with key, like our_cache.get(key=1). If the key is not in cache, you get -1.

Both function take O(1) time. 
Regarding set function, a key and a value can be stored in cache. And thanks to doublyLinkedList, cache re_queue also take O(1).
Regarding get function, a key can access a value directly (meaning O(1)). And thanks to doublyLinkedList, cache re_queue also take O(1).