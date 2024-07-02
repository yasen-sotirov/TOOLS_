"""
https://www.geeksforgeeks.org/time-complexities-of-different-data-structures/

Growth rates illustrated

	        n=1	    n=2	    n=4	    n=8	    n=16	n=32
O(1)	    1	    1	    1	    1	    1	    1
О(log n)	0	    1	    2	    3	    4	    5
О(n)	    1	    2	    4	    8	    16	    32
О(n*log n)	0	    2	    8	    24	    64	    160
О(n2)	    1	    4	    16	    64	    256	    1024
О(n3),	    1	    8	    64	    512	    4 096	32 768
О(2n)	    2	    4	    16	    235	    65 536	4 294 967 296




WORST CASE TIME COMPLEXITY

Data structure	        Access	    Search	    Insertion	Deletion
Array	                O(1)	    O(N)	    O(N)	    O(N)
Stack	                O(N)	    O(N)	    O(1)	    O(1)
Queue	                O(N)	    O(N)	    O(1)	    O(1)
Singly Linked list	    O(N)	    O(N)	    O(N)	    O(N)
Doubly Linked List	    O(N)	    O(N)	    O(1)	    O(1)
Hash Table	            O(N)	    O(N)	    O(N)	    O(N)
Binary Search Tree	    O(N)	    O(N)	    O(N)	    O(N)
AVL Tree	            O(log N)	O(log N)	O(log N)	O(log N)
Binary Tree	            O(N)	    O(N)	    O(N)	    O(N)
Red Black Tree	        O(log N)	O(log N)	O(log N)	O(log N)


THE AVERAGE TIME COMPLEXITY

Data structure	        Access	    Search	    Insertion	Deletion
Array	                O(1)	    O(N)	    O(N)	    O(N)
Stack	                O(N)	    O(N)	    O(1)	    O(1)
Queue	                O(N)	    O(N)	    O(1)	    O(1)
Singly Linked list	    O(N)	    O(N)	    O(1)	    O(1)
Doubly Linked List	    O(N)	    O(N)	    O(1)	    O(1)
Hash Table	            O(1)	    O(1)	    O(1)	    O(1)
Binary Search Tree	    O(log N)	O(log N)	O(log N)	O(log N)
AVL Tree	            O(log N)	O(log N)	O(log N)	O(log N)
B Tree	                O(log N)	O(log N)	O(log N)	O(log N)
Red Black Tree	        O(log N)	O(log N)	O(log N)	O(log N)



BEST CASE TIME COMPLEXITY

Data structure	        Access	    Search	    Insertion	Deletion
Array	                O(1)	    O(1)	    O(1)	    O(1)
Stack	                O(1)	    O(1)	    O(1)	    O(1)
Queue	                O(1)	    O(1)	    O(1)	    O(1)
Singly Linked list	    O(1)	    O(1)	    O(1)	    O(1)
Doubly Linked List	    O(1)	    O(1)	    O(1)	    O(1)
Hash Table	            O(1)	    O(1)	    O(1)	    O(1)
Binary Search Tree	    O(log n)	O(log n)	O(log n)	O(log n)
AVL Tree	            O(log n)	O(log n)	O(log n)	O(log n)
B Tree	                O(log n)	O(log n)	O(log n)	O(log n)
Red Black Tree	        O(log n)	O(log n)	O(log n)	O(log n)
"""