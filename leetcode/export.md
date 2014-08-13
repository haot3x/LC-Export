## Word Break

**20.9%**

*2013-10-04*

[url](https://oj.leetcode.com/problems/word-break/submissions/)

`java`

```

public class Solution {
    public boolean wordBreak(String s, Set<String> dict) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int len = s.length();
        if(len == 0)
            return false;
        boolean [] dp = new boolean[len + 1];
        dp[0] = true;
        for(int i = 1; i <= len; i++)
        {
            for(int j = 0; j < i; j++)
            {
                if(dict.contains(s.substring(j, i)) && dp[j])
                    dp[i] = true;
            }
        }
        return dp[len];
    }
}

```

====

## Gas Station

**25.1%**

*2013-09-28*

[url](https://oj.leetcode.com/problems/gas-station/submissions/)

`java`

```

public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
          int tank = -1;
        int ret = -1;

        for (int i = 0; i < gas.length; ++i) {
            int tmp = gas[i] - cost[i];
            if (tank >= 0) {
                tank += tmp;
                ret = tank < 0 ? -1 : ret;
            } else if (tmp >= 0) {
                tank = tmp;
                ret = i;
            }
        }

        for (int i = 0; tank >= 0 && i < ret; ++i)
            tank += gas[i] - cost[i];

        return tank >= 0 ? ret : -1;
        
    }
}

```

====

## Single Number

**45.8%**

*2013-10-01*

[url](https://oj.leetcode.com/problems/single-number/submissions/)

`java`

```

public class Solution {
    public int singleNumber(int[] A) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int len = A.length, xor = 0;
        for(int i = 0; i < len; i++)
        {
            xor = xor ^ A[i];
        }
        return xor;
    }
}

```

====

## Clone Graph

**22.5%**

*2013-09-24*

[url](https://oj.leetcode.com/problems/clone-graph/submissions/)

`java`

```

/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(node == null)
            return null;
        UndirectedGraphNode ret = new UndirectedGraphNode(node.label);
        
        HashMap<Integer, UndirectedGraphNode> map = new HashMap<Integer, UndirectedGraphNode>();
        map.put(node.label, ret);
        
        Deque<UndirectedGraphNode> queue = new ArrayDeque<UndirectedGraphNode>();
        queue.addLast(node);
        
        UndirectedGraphNode temp, newTemp, newNode;
        ArrayList<UndirectedGraphNode> tempList;
        while(queue.size() > 0)
        {
            temp = queue.removeFirst();
            tempList = temp.neighbors;
            newTemp = map.get(temp.label);
            for(UndirectedGraphNode cur: tempList)
            {
                if(!map.containsKey(cur.label))
                {
                    queue.addLast(cur);
                    newNode = new UndirectedGraphNode(cur.label);
                    newTemp.neighbors.add(newNode);
                    map.put(cur.label, newNode);
                }
                else{
                    newNode = map.get(cur.label);
                    newTemp.neighbors.add(newNode);
                }
            }
        }
        
        
        return ret;
    }
}

```

`java`

```

/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(node == null)
            return null;
        UndirectedGraphNode ret = new UndirectedGraphNode(node.label);
        
        HashMap<Integer, UndirectedGraphNode> map = new HashMap<Integer, UndirectedGraphNode>();
        map.put(node.label, ret);
        
        Deque<UndirectedGraphNode> queue = new ArrayDeque<UndirectedGraphNode>();
        queue.addLast(node);
        
        UndirectedGraphNode temp, newTemp, newNode;
        ArrayList<UndirectedGraphNode> tempList;
        while(queue.size() > 0)
        {
            temp = queue.removeFirst();
            tempList = temp.neighbors;
            newTemp = map.get(temp.label);
            for(UndirectedGraphNode cur: tempList)
            {
                if(!map.containsKey(cur.label))
                {
                    queue.addLast(cur);
                    newNode = new UndirectedGraphNode(cur.label);
                    newTemp.neighbors.add(newNode);
                    map.put(cur.label, newNode);
                }
                else{
                    newNode = map.get(cur.label);
                    newTemp.neighbors.add(newNode);
                }
            }
        }
        
        //create new node with no neighbors
        //add neighbors next time;
        return ret;
    }
}

```

====

## Binary Tree Preorder Traversal

**35.5%**

*2013-11-05*

[url](https://oj.leetcode.com/problems/binary-tree-preorder-traversal/submissions/)

`java`

```

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ArrayList<Integer> preorderTraversal(TreeNode root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ArrayList<Integer> res = new ArrayList<Integer>();
        helper(root, res);
        return res;
    }
    public void helper(TreeNode root, ArrayList<Integer> res)
    {
        if(root == null) return;
        res.add(root.val);
        helper(root.left, res);
        helper(root.right, res);
    }
}

```

`java`

```

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ArrayList<Integer> preorderTraversal(TreeNode root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
       
        Stack<TreeNode> s = new Stack<TreeNode>();
        ArrayList<Integer> res = new ArrayList<Integer>();
         if(root == null)
            return res;
        s.push(root);
        while(!s.isEmpty()){
            root = s.pop();
            res.add(root.val);
            if(root.right != null){
                s.push(root.right);
            }
            if(root.left != null)
                s.push(root.left);
        }
        return res;
    }
        
        
        
        
        /*ArrayList<Integer> res = new ArrayList<Integer>();
        helper(root, res);
        return res;
    }
    public void helper(TreeNode root, ArrayList<Integer> res)
    {
        if(root == null) return;
        res.add(root.val);
        helper(root.left, res);
        helper(root.right, res);
    }*/
}

```

====

## Sum Root to Leaf Numbers

**29.6%**

*2013-02-18*

[url](https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/submissions/)

`java`

```

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
   
	    public int sumNumbers(TreeNode root) {
	        // Start typing your Java solution below
	        // DO NOT write main() function
	        if(root == null)
	            return 0;
	       return helper(root, 0); 
	    }
	    
	    private int helper(TreeNode node, int cur)
	    {
	        if(node == null)
	        {    
	        	return 0;
	        }
	        
	        if(node.left == null && node.right == null)
	        {
	            cur = cur*10 + node.val;
	            return cur;
	        }
	        if(node.left != null || node.right != null)
	        {
	            cur = cur*10 + node.val;
	            return helper(node.left, cur) + helper(node.right, cur);
	        }
	        return 0;
	    }
	
    
    
}

```

====

## Binary Tree Postorder Traversal

**30.9%**

*2013-11-07*

[url](https://oj.leetcode.com/problems/binary-tree-postorder-traversal/submissions/)

`java`

```

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ArrayList<Integer> postorderTraversal(TreeNode root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        Stack<TreeNode> s1 = new Stack<TreeNode>();
        Stack<TreeNode> s2 = new Stack<TreeNode>();
        ArrayList<Integer> ret = new ArrayList<Integer>();
        if(root == null)
            return ret;
        s1.push(root);
        while(!s1.isEmpty())
        {
            root = s1.pop();
            if(root.left != null)
                s1.push(root.left);
            if(root.right != null)
                s1.push(root.right);
            s2.push(root);
        }
        while(!s2.isEmpty())
            ret.add(s2.pop().val);
        return ret;
    }
}

```

====

## Linked List Cycle

**35.8%**

*2013-10-28*

[url](https://oj.leetcode.com/problems/linked-list-cycle/submissions/)

`java`

```

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        /*if(head == null || head.next == null)
            return false;
        if(head.next.next == null)
            return head.next == head;
        
        ListNode p1 = head;
        ListNode p2 = head.next;
        
        while(p1 != null && p2.next != null)
        {
            if(p1 == p2)
                return true;
            p1 = p1.next;
            p2 = p2.next.next;
        }
        return false;*/
        if(head == null || head.next == null)  
            return false;  
        ListNode p = head, q = head.next;  
        while( q!= null && q.next != null)  
        {  
            if(p == q)  
                return true;  
            p = p.next;  
            q = q.next.next;  
        }  
        return false; 
    }
}

```

`java`

```

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(head == null || head.next == null)
            return false;
        
        ListNode p1 = head;
        ListNode p2 = head.next;
        
        while(p2 != null && p2.next != null)
        {
            if(p1 == p2)
                return true;
            p1 = p1.next;
            p2 = p2.next.next;
        }
        return false;
    }
}

```

`java`

```

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(head == null || head.next == null)
            return false;
        
        ListNode p1 = head;
        ListNode p2 = head.next;
        
        while(p2 != null && p2.next != null) // important! p2!=null
        {
            if(p1 == p2)
                return true;
            p1 = p1.next;
            p2 = p2.next.next;
        }
        return false;
    }
}

```

====

## Binary Tree Maximum Path Sum

**19.9%**

*2012-11-07*

[url](https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/submissions/)

`java`

```

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    int max;
    public int maxPathSum(TreeNode root) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        max = (root==null)? 0: root.val;
        findMax(root);
        return max;
    }
    public int findMax(TreeNode node){
        if(node == null) return 0;
        int left = Math.max(findMax(node.left),0);
        int right = Math.max(findMax(node.right),0);
        max = Math.max(node.val + left + right, max);
        return node.val + Math.max(left,right);
    }
}

```

====

## Linked List Cycle II

**30.9%**

*2013-10-30*

[url](https://oj.leetcode.com/problems/linked-list-cycle-ii/submissions/)

`java`

```

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(head == null || head.next == null)
            return null;
        
        ListNode p1 = head;
        ListNode p2 = head;
        boolean isCycle = false;
        while(p2 != null && p2.next != null) // important! p2!=null
        {
            p1 = p1.next;
            p2 = p2.next.next;
            if(p1 == p2)
            {
                isCycle = true;
                break;
            }
        }
        if(isCycle == false)
            return null;
            
        p1 = head;
        while (p1 != p2) {
            p1 = p1.next;
            p2 = p2.next; 
            }
        // Now n2 points to the start of the loop.
        return p2;
    }
}

```

====

