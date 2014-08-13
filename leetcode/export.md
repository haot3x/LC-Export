## Count and Say

**27.1%**

*2012-03-05*

[url](https://oj.leetcode.com/problems/count-and-say/submissions/)

`java`

```

public class Solution {
    public String countAndSay(int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        String a, b;
        a = "1";
        for(int i = 2; i <= n; i++)
        {
            b = "";
            int len = a.length(), count = 1;
            char prev = a.charAt(0), cur;
            for(int j = 1; j < len; j++)
            {
                cur = a.charAt(j);
                if(prev == cur)
                    count++;
                else{
                    b += count;
                    b = b + prev;
                    count = 1;
                    prev = cur;
                }
            }
            b += count;
            b = b + prev;
            String tmp = a;
            a = b;
            b = tmp;
        }
        return a;
    }
}

```

====

## Integer to Roman

**33.3%**

*2012-01-15*

[url](https://oj.leetcode.com/problems/integer-to-roman/submissions/)

`java`

```

public class Solution {
    public String intToRoman(int num) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int [] vals = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String [] chars = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        
        int len = vals.length;
        StringBuilder ret = new StringBuilder();
        
        for(int i = 0; i < len; i++)
        {
            int times = num/vals[i];
            for(int j = 0; j < times; j++)
                ret.append(chars[i]);
            num -= vals[i]*times;
        }
        
        return ret.toString();
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

## Two Sum

**18.4%**

*2011-03-13*

[url](https://oj.leetcode.com/problems/two-sum/submissions/)

`java`

```


	public class Solution {
	    public int[] twoSum(int[] numbers, int target) {
	        // Start typing your Java solution below
	        // DO NOT write main() function
	        int [] ret = new int[2];
	        int j = 0;
	        Map<Integer, Integer> hash = new HashMap<Integer, Integer>();
	        
	        for(int i = 0; i < numbers.length; i++)
	            hash.put(target - numbers[i], i);
	        for(int i = 0; i < numbers.length; i++)
	            if(hash.containsKey(numbers[i]))
	            {
	                j = hash.get(numbers[i]);
	                if(j != i)
	                {    
	                    ret[0] = i+1;
	                    ret[1] = j+1;
	                    return ret;
	                }
	            }
	        return ret;
	    }
	}



```

====

## Swap Nodes in Pairs

**32.4%**

*2012-02-14*

[url](https://oj.leetcode.com/problems/swap-nodes-in-pairs/submissions/)

`java`

```

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if(head == null || head.next == null)
            return head;
        
        int tmp = 0;
        ListNode cur = head;
        while(cur.next != null)
        {
            tmp = cur.val;
            cur.val = cur.next.val;
            cur.next.val = tmp;
            if(cur.next.next != null)
                cur = cur.next.next;
            else break;
        }
        return head;
    }
}

```

====

## Convert Sorted List to Binary Search Tree

**27.1%**

*2012-10-02*

[url](https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/submissions/)

`java`

```

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
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
    public TreeNode sortedListToBST(ListNode head) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(head == null)
            return null;
        int n = 0;
        ArrayList<Integer> a = new ArrayList<Integer>();
        while(head!=null)
        {
            n++;
            a.add(head.val);
            head = head.next;
        }
        int [] array = new int[n];
        for(int i = 0; i < a.size(); i++)
            array[i] = a.get(i);
        
        return helper(array, 0, n-1);
        
    }
    
     public TreeNode helper(int [] num, int start, int end)
    {
        if(start > end)
            return null;
        if(start == end)
            return new TreeNode(num[start]);
        TreeNode root = null;
        if(start < end)
        {
            root = new TreeNode(num[(start + end)/2]);
            root.left = helper(num, start, (start + end)/2 - 1);
            root.right = helper(num, (start+end)/2 + 1, end);
        }
        return root;
    }
}

```

====

## Maximum Subarray

**33.6%**

*2012-03-21*

[url](https://oj.leetcode.com/problems/maximum-subarray/submissions/)

`java`

```

public class Solution {
    public int maxSubArray(int[] A) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int len = A.length;
        if(len == 0)
            return 0;
        if(len == 1)
            return A[0]; 
        
        int low, maxDiff = 0, curDiff;
        int[] sumSoFar = new int[len];
        
        sumSoFar[0] = A[0];
        for(int i = 1; i < len; i++)
            sumSoFar[i] = A[i] + sumSoFar[i-1];
            
        low = sumSoFar[0];
        maxDiff = sumSoFar[0];
        for(int i = 1; i < len; i++)
        {
            curDiff = sumSoFar[i] - low;
            maxDiff = Math.max(Math.max(curDiff, maxDiff), sumSoFar[i]);
            low = sumSoFar[i] < low ? sumSoFar[i] : low;
        }
        return maxDiff;
    }
}

```

`java`

```

public class Solution {
    public int maxSubArray(int[] A) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int len = A.length;
        if(len == 0)
            return 0;
        int curSum = 0;
        int low = 0;
        int max = A[0];
        
        for(int i = 0; i < len ; i++)
        {
            curSum += A[i];
            max = Math.max(curSum-low, max);
            low = Math.min(low, curSum);
        }
        return max;
    }
}

```

====

## Divide Two Integers

**16.3%**

*2012-02-18*

[url](https://oj.leetcode.com/problems/divide-two-integers/submissions/)

`java`

```

public class Solution {
    public int divide(int dividend, int divisor) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
          assert(divisor != 0);
        if(dividend == 0)   return 0;
        boolean isNeg = (dividend > 0) != (divisor > 0);
        
        long dvd = dividend > 0 ? dividend : (long)dividend*-1;
        long dvs = divisor > 0 ? divisor : (long)divisor*-1;
        
        if(dvd < dvs) return 0;
        long ans = 0;
        long cur = 1;
        while(dvs <= dvd)
        {
            dvs <<= 1;
            cur <<= 1;
        }
        
        dvs >>= 1;
        cur >>= 1;
        
        while(cur != 0)
        {
            if(dvd >= dvs)
            {
                dvd -= dvs;
                ans += cur;
            }
            cur >>= 1;
            dvs >>= 1;
        }
        if(isNeg)   return (int)(-1*ans);
        return (int)ans;
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

## Anagrams

**23.4%**

*2012-03-19*

[url](https://oj.leetcode.com/problems/anagrams/submissions/)

`java`

```

public class Solution {
    public ArrayList<String> anagrams(String[] strs) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        Map<String, ArrayList<String>> table = new HashMap<String, ArrayList<String>>();
        ArrayList<String> ret = new ArrayList<String>();
        for(String s : strs)
        {
            String temp = toAscendingString(s);
            if(!table.containsKey(temp))
            {
                    ArrayList<String> indexList = new ArrayList<String>();
                    indexList.add(s);
                    table.put(temp, indexList);
            }
            else
            {
                table.get(temp).add(s);    
            }
        }
        
        for(String s: table.keySet())
        {
            if(table.get(s).size() > 1)
                ret.addAll(table.get(s));
        }
        
        return ret;
    }
    
    private String toAscendingString(String s)
    {
        char[] c = s.toCharArray();
        Arrays.sort(c);
        return String.copyValueOf(c);
    }
}

```

====

## Construct Binary Tree from Preorder and Inorder Traversal

**26.4%**

*2012-09-30*

[url](https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/)

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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        if(preorder.length == 0 || inorder.length == 0)
            return null;
        return builder(preorder, 0, preorder.length-1, inorder, 0, inorder.length-1);
    }
    
    public TreeNode builder(int[] preorder, int prestart, int preend, int[] inorder, int instart, int inend)
    {
        if(prestart > preend)
    		return null;
        if(prestart == preend)
            return new TreeNode(preorder[prestart]);
        int rootLoc = 0, leftCount = 0, rightCount = 0;
        TreeNode root = new TreeNode(preorder[prestart]);
        for(int i = 0; i <= inend; i++)
        {
            if(inorder[i] == preorder[prestart])
            {   
                rootLoc = i;
                break;
            }
        }
        
        leftCount = rootLoc - instart;
        rightCount = inend - rootLoc;
        
        
        root.left = builder(preorder, prestart+1, prestart+leftCount, inorder, instart, instart+leftCount);
        root.right = builder(preorder, prestart+leftCount+1, preend, inorder, instart+leftCount+1, inend);
        return root;
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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        
        if(preorder.length == 0 || inorder.length == 0)
            return null;
        return builder(preorder, 0, preorder.length-1, inorder, 0, inorder.length-1);
    }
    
    public TreeNode builder(int[] preorder, int prestart, int preend, int[] inorder, int instart, int inend)
    {
        if(prestart > preend)
    		return null;
        if(prestart == preend)
            return new TreeNode(preorder[prestart]);
        int rootLoc = 0, leftCount = 0, rightCount = 0;
        TreeNode root = new TreeNode(preorder[prestart]);
        for(int i = 0; i <= inend; i++) //here
        {
            if(inorder[i] == preorder[prestart])
            {   
                rootLoc = i;
                break;
            }
        }
        
        leftCount = rootLoc - instart;
        rightCount = inend - rootLoc;
        
        
        root.left = builder(preorder, prestart+1, prestart+leftCount, inorder, instart, instart+leftCount);
        root.right = builder(preorder, prestart+leftCount+1, preend, inorder, instart+leftCount+1, inend);
        return root;
    }
}

```

====

## Generate Parentheses

**31.4%**

*2012-02-12*

[url](https://oj.leetcode.com/problems/generate-parentheses/submissions/)

`java`

```

public class Solution {
    public ArrayList<String> generateParenthesis(int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        assert(n>=0);


		if(n == 0)
			return  new ArrayList<String> ();

		return generator(new StringBuffer(), 0, 0, n);

	}

	public ArrayList<String> generator(StringBuffer buf, int l, int r, int n)
	{
		ArrayList<String> ret = new ArrayList<String> ();
		if(l > n || r > n)
		{
			return ret;
		}
		if(r == n)
		{
			ret.add(buf.toString());
			return ret;
		}

		if (r < l) {
			StringBuffer newBuf = new StringBuffer(buf);
			newBuf.append(")");
			ret.addAll(generator(newBuf, l, r + 1, n));
		}
		
		if(l < n)
		{
			StringBuffer newBuf = new StringBuffer(buf);
			newBuf.append("(");
			ret.addAll(generator(newBuf, l + 1, r, n));
		}

		return ret;
	}
}

```

====

## Minimum Depth of Binary Tree

**29.5%**

*2012-10-09*

[url](https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/submissions/)

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
    public int minDepth(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if(root == null)
            return 0;
        return helper(root);
    }
    
     
    public int helper(TreeNode node)
    {
        int ret = 0, leftDepth = 0, rightDepth = 0;
        if(node == null)
        	return 0;
        if(node.left == null && node.right == null)
        	return 1;
        if(node.left == null && node.right != null)
        	return helper(node.right) + 1;
        if(node.left != null && node.right == null)
        	return helper(node.left) + 1;
        return Math.min(helper(node.left), helper(node.right)) + 1;
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

## Multiply Strings

**20.5%**

*2012-03-12*

[url](https://oj.leetcode.com/problems/multiply-strings/submissions/)

`java`

```

public class Solution {
    public String multiply(String num1, String num2) {
        // Start typing your Java solution below
        // DO NOT write main() function
        
        int[] num = new int[num1.length()+num2.length()];
        for(int i=0;i<num1.length();i++){
            int carry = 0;
            int a = num1.charAt(num1.length()-1-i)-'0';
            for(int j=0;j<num2.length();j++){
                int  b = num2.charAt(num2.length()-1-j)-'0';
                num[i+j]+=carry+a*b;
                carry=num[i+j]/10;
                num[i+j]%=10;
            }
            num[i+num2.length()]+=carry;
        }
        int i=num.length-1;
        while(i>0 && num[i]==0) i--;
        
        StringBuilder temp = new StringBuilder("");
        while(i>=0)
            temp.append((char)('0'+num[i--]));
        
        return temp.toString();
    }
}

```

====

## Binary Tree Inorder Traversal

**35.5%**

*2012-08-27*

[url](https://oj.leetcode.com/problems/binary-tree-inorder-traversal/submissions/)

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
    public ArrayList<Integer> inorderTraversal(TreeNode root) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(root == null)
            return new ArrayList<Integer>();
        
        return helper(new ArrayList<Integer>(), root);
    }
    
    ArrayList<Integer> helper(ArrayList<Integer> list, TreeNode node)
    {
        if(node == null)
            return null;
        helper(list, node.left);
        list.add(node.val);
        helper(list, node.right);
        return list;
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
    public ArrayList<Integer> inorderTraversal(TreeNode root) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        ArrayList<Integer> ret = new ArrayList<Integer>();
        if(root == null)
            return ret;
        
        Stack<TreeNode> s = new Stack<TreeNode>();
        boolean isFinished = false;
        
       // s.push(root);
        while(!isFinished){
            if(root != null){
                s.push(root);
                root = root.left;
            }
            else
            {
                if(!s.isEmpty()){
               root = s.pop();
               ret.add(root.val);
                root = root.right;
               }  
               else
                    isFinished = true;
            }
        }
        return ret;
    }
        
        
        
        
        /*if(root == null)
            return new ArrayList<Integer>();
        
        return helper(new ArrayList<Integer>(), root);
    }
    
    ArrayList<Integer> helper(ArrayList<Integer> list, TreeNode node)
    {
        if(node == null)
            return null;
        helper(list, node.left);
        list.add(node.val);
        helper(list, node.right);
        return list;
    }*/
}

```

====

## Add Binary

**25.8%**

*2012-04-02*

[url](https://oj.leetcode.com/problems/add-binary/submissions/)

`java`

```

public class Solution {
    public String addBinary(String a, String b) {
        // Start typing your Java solution below
        // DO NOT write main() function
       
        String ret = "";
        
        int carry = 0;
        
        int i = a.length() - 1, j = b.length() - 1; 
        while(i >= 0 && j >= 0)
        {
            int cur = Integer.valueOf(a.charAt(i)) + Integer.valueOf(b.charAt(j)) - 96 + carry;
            if(cur == 0)    
            {
                ret = "0" + ret;
                carry = 0;
            }
            else if (cur == 1)
            {
                ret = "1" + ret;
                carry = 0;
            }
            else if (cur == 2)
            {
                ret = "0" + ret;
                carry = 1;
            }
            else if (cur == 3)
            {
                ret = "1" + ret;
                carry = 1;
            }
            i--;
            j--;
        }
        
        while(i >= 0)
        {
            int cur = Integer.valueOf(a.charAt(i)) - 48 + carry;
            if(cur == 0)    
            {
                ret = "0" + ret;
                carry = 0;
            }
            else if (cur == 1)
            {
                ret = "1" + ret;
                carry = 0;
            }
            else if (cur == 2)
            {
                ret = "0" + ret;
                carry = 1;
            }
            else if (cur == 3)
            {
                ret = "1" + ret;
                carry = 1;
            }
            i--;
        } 
        while(j >= 0)
        {
            int cur = Integer.valueOf(b.charAt(j)) - 48 + carry;
            if(cur == 0)    
            {
                ret = "0" + ret;
                carry = 0;
            }
            else if (cur == 1)
            {
                ret = "1" + ret;
                carry = 0;
            }
            else if (cur == 2)
            {
                ret = "0" + ret;
                carry = 1;
            }
            else if (cur == 3)
            {
                ret = "1" + ret;
                carry = 1;
            }
            j--;
        }
        if(carry == 0)
        return ret;
        else return "1" + ret;
    }
}

```

====

## Sqrt(x)

**22.2%**

*2012-04-03*

[url](https://oj.leetcode.com/problems/sqrtx/submissions/)

`java`

```

public class Solution {
    public int sqrt(int x) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(x<=0)
            return 0;
        if(x == 1)
            return 1;
            
        long i = 0;
        long j = x/2 + 1;
        
        while(i <= j)
        {
            long mid = (i + j)/2;
            long sq = mid*mid;
            if(sq == x)
                return (int)mid;
            else if(sq < x)
                i = mid + 1;
            else
                j = mid - 1;
        }
        
        return (int)j;
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

## Populating Next Right Pointers in Each Node

**35.3%**

*2012-10-28*

[url](https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/submissions/)

`java`

```

/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(root == null)    return;
        
        int level = 0;
        root.next = null;
        TreeLinkNode curLevelFirst = root, cur, prev = null;
        TreeLinkNode preLevelFirst = root;
        while(true)
        {
            if(preLevelFirst.left == null)
                break;
                
            curLevelFirst = preLevelFirst.left;
            prev = null;
            while(preLevelFirst != null){
                 cur = preLevelFirst.left;
                if(prev != null)    prev.next = cur;
                 cur.next = preLevelFirst.right;
                 cur.next.next = null;
                 prev = cur.next;
                 preLevelFirst = preLevelFirst.next;
            }
            preLevelFirst = curLevelFirst;
        }
    }
}

```

====

## Remove Element

**33.3%**

*2012-02-16*

[url](https://oj.leetcode.com/problems/remove-element/submissions/)

`java`

```

public class Solution {
    public int removeElement(int[] A, int elem) {
         int pos = 0;
        int oldLength = A.length;
        
        for(int i=0; i<oldLength; i++)
        {
            if(A[i] == elem)
            {
                pos++;
                continue;
            }
            if(i>=pos)
            A[i-pos] = A[i];
            else
                break;
        }
        return oldLength - pos;
    }
}

```

`cpp`

```

class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int r = 0;
        int i = 0;
        while( i < n && r < n ){
            if( A[i] != elem )
                A[r++] = A[i];
            i++;
        }
        return r;
    }
};

```

`java`

```

public class Solution {
    public int removeElement(int[] A, int elem) {
        // Start typing your Java solution below
        // DO NOT write main() function
        
        if(A == null)
            return 0;
        int i = 0, j = 0;
        while(j < A.length)
        {
            if(A[j] != elem)
            {
                A[i] = A[j];
                i++;
            }
            j++;
        }
        return i;
        
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

## Same Tree

**42.1%**

*2012-09-03*

[url](https://oj.leetcode.com/problems/same-tree/submissions/)

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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(p == null && q == null)
            return true;
        if(p != null && q != null)
            return p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        return false;
    }
}

```

====

## Validate Binary Search Tree

**25.7%**

*2012-08-31*

[url](https://oj.leetcode.com/problems/validate-binary-search-tree/submissions/)

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
    public boolean isValidBST(TreeNode root) {
       return isValidBSTHelper(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }
    
    public boolean isValidBSTHelper(TreeNode cur, int min, int max)
    {
        if(cur == null) return true;
        if(cur.val > min && cur.val < max)
        {
            return isValidBSTHelper(cur.left, min, cur.val) && isValidBSTHelper(cur.right, cur.val, max);
        }
        return false;
    }
}

```

====

## Triangle

**26.7%**

*2012-10-29*

[url](https://oj.leetcode.com/problems/triangle/submissions/)

`java`

```

public class Solution {
    public int minimumTotal(ArrayList<ArrayList<Integer>> triangle) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int n = triangle.size();
        int [] p = new int [n + 1];
        
        while(n > 0)
        {
            n--;
            for(int i = 0; i <= n; i++)
            p[i] = triangle.get(n).get(i) + (p[i] < p[i+1] ? p[i] : p[i+1]);
          
        }
        return p[0];
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

## Restore IP Addresses

**20.4%**

*2012-08-07*

[url](https://oj.leetcode.com/problems/restore-ip-addresses/submissions/)

`java`

```

public class Solution {
    public ArrayList<String> restoreIpAddresses(String s) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int len = s.length();
        ArrayList<String> ret = new ArrayList<String>();
        if(len < 4 || len > 12)
            return ret;
        helper(ret, s, 0, new StringBuilder());
        return ret;
    }
    
    public void helper(ArrayList<String> ret, String s, int count, StringBuilder cur)
    {
        if(count == 3 && isValid(s))
        {
            ret.add(cur+s);
            return;
        }
        
        for(int i = 1; i < 4 && i < s.length(); i++)
        {
            String subString = s.substring(0, i);
            if(isValid(subString))
            {
            	StringBuilder newCur = new StringBuilder(cur);
                helper(ret, s.substring(i), count+1, newCur.append(subString+"."));
            }
        }
    }
    
    public boolean isValid(String s){  
        if (s.charAt(0)=='0') return s.equals("0");  
        int num = Integer.parseInt(s);  
        return num<=255 && num>0;  
    }
}

```

====

## Interleaving String

**19.1%**

*2012-08-30*

[url](https://oj.leetcode.com/problems/interleaving-string/submissions/)

`java`

```

public class Solution {
    public boolean isInterleave1(String s1, String s2, String s3) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(s1.length() + s2.length() != s3.length())
            return false;
        if(s3.length() == 0)
            return true;
        if(s3.length() == 1)
        {
            if(s3.equals(s1) || s3.equals(s1))
                return true;
            else return false;
        }
        
        return isInterleave(s1, 0, s2, 0, s3, 0);
    }
    
    public boolean isInterleave(String s1, int i, String s2, int j, String s3, int k)
    {
        if(k == s3.length())
            return true;
        if(i == s1.length() && j != s2.length())
	            return s2.substring(j).equals(s3.substring(k));
	    if(i != s1.length() && j == s2.length())
	        	return s1.substring(i).equals(s3.substring(k));
	    if(i == s1.length() && j == s2.length())
	        	return false;       
        char cur = s3.charAt(k);
        if(s1.charAt(i) != cur && s2.charAt(j) != cur)
            return false;
        else if(s1.charAt(i) != cur && s2.charAt(j) == cur)
            return isInterleave(s1, i, s2, j+1, s3, k+1);
        else if(s1.charAt(i) == cur && s2.charAt(j) != cur)
            return isInterleave(s1, i+1, s2, j, s3, k+1);
        
        return isInterleave(s1, i+1, s2, j, s3, k+1) || isInterleave(s1, i, s2, j+1, s3, k+1);
        
    }
    
    public boolean isInterleave(String s1, String s2, String s3)
	{
		if(s1.length() + s2.length() != s3.length())
			return false;
		if(s3.length() == 0)
			return true;
		if(s3.length() == 1)
		{
			if(s3.equals(s1) || s3.equals(s2))
				return true;
			else return false;
		}
		boolean [][] status = new boolean [s1.length()+1][s2.length()+1];
		
		status[0][0] = true;
		for(int i = 1; i <= s1.length(); i++)
		{
			status[i][0] = status[i-1][0] && s1.charAt(s1.length() - i) == s3.charAt(s3.length() - i);
		}
		
		for(int j = 1; j <= s2.length(); j++)
		{
			status[0][j] = status[0][j-1] && s2.charAt(s2.length() - j) == s3.charAt(s3.length() - j);
		}
		   int len1 = s1.length();
	        int len2 = s2.length();
	        int len3 = s3.length();
		for(int i = 1; i <= s1.length(); i++)
			for(int j = 1; j <= s2.length(); j++)
			{
				status[i][j] = s3.charAt(len3 - i - j) == s1.charAt(len1 - i) && status[i-1][j] ||
                        s3.charAt(len3 - i - j) == s2.charAt(len2 - j) && status[i][j-1];
			}
		
		return status[len1][len2];
		
	}
}

```

====

## Unique Binary Search Trees II

**27.1%**

*2012-08-27*

[url](https://oj.leetcode.com/problems/unique-binary-search-trees-ii/submissions/)

`java`

```

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; left = null; right = null; }
 * }
 */
public class Solution {
    public ArrayList<TreeNode> generateTrees(int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        
        return generate(1, n);
    }
    
    public ArrayList<TreeNode> generate(int from, int to)
    {
        ArrayList<TreeNode> ret = new ArrayList<TreeNode> ();
        if(from > to){
            ret.add(null);
            return ret;
        }
        for(int i = from; i <= to; i++){
            for(TreeNode left: generate(from, i - 1)){
                for(TreeNode right: generate(i + 1, to)){
                    TreeNode root = new TreeNode(i);
                    root.left = left;
                    root.right = right;
                    ret.add(root);
                }
            }
        }
        return ret;
    }
}

```

====

## Construct Binary Tree from Inorder and Postorder Traversal

**26.3%**

*2012-09-30*

[url](https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/)

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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(inorder.length == 0 || postorder.length != inorder.length)
            return null;
        return builder(inorder, 0, inorder.length-1, postorder, 0, postorder.length - 1);
    }
    public TreeNode builder(int [] inorder, int inStart, int inEnd, int[] postorder, int postStart, int postEnd)
    {
        if(postStart > postEnd)
            return null;
            
        int rootVal = postorder[postEnd], leftCount = 0, rightCount = 0, rootLoc = 0;
        if(postStart == postEnd)
            return new TreeNode(rootVal);
       
        
        TreeNode root = new TreeNode(rootVal);
        
        for(int i = inStart; i <= inEnd; i++)
        {
            if(inorder[i] == rootVal)
            {
                rootLoc = i;
                break;
            }
        }
        
        leftCount = rootLoc - inStart;
        rightCount = inEnd - rootLoc;
        
        root.left = builder(inorder, inStart, rootLoc - 1, postorder, postStart, postStart + leftCount - 1);
        root.right = builder(inorder, rootLoc + 1, inEnd, postorder, postStart + leftCount, postEnd - 1);
        return root;
        
    }
}

```

====

## Subsets

**27.8%**

*2012-04-18*

[url](https://oj.leetcode.com/problems/subsets/submissions/)

`java`

```

public class Solution {
    public ArrayList<ArrayList<Integer>> subsets(int[] S) {
       // Note: The Solution object is instantiated only once and is reused by each test case.
		Arrays.sort(S);
		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();

		for(int k = 0; k <= S.length; k++)
			getSubsets(S, k, 0, new HashSet<Integer>(), res);

		return res;
	}
	
	private static void getSubsets(int[] superSet, int k, int idx,
			HashSet<Integer> cur, List<ArrayList<Integer>> res) {
		//success
		if(cur.size() == k)
		{
			ArrayList<Integer> temp = new ArrayList<Integer>(cur);
			Collections.sort(temp);
			res.add(temp);
			return;
		}
		//not success
		if(idx == superSet.length)
			return;
		//put in idx
		cur.add(superSet[idx]);
		getSubsets(superSet, k, idx+1, cur, res);

		//do not put in idx
		cur.remove(superSet[idx]);
		getSubsets(superSet, k, idx+1, cur, res);
	}
}

```

`java`

```

public class Solution {
    public ArrayList<ArrayList<Integer>> subsets(int[] S) {
       // Note: The Solution object is instantiated only once and is reused by each test case.
		Arrays.sort(S);
		ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();

		for(int k = 0; k <= S.length; k++)
			getSubsets(S, k, 0, new HashSet<Integer>(), res);

		return res;
	}
	
	private static void getSubsets(int[] superSet, int k, int idx,
			HashSet<Integer> cur, List<ArrayList<Integer>> res) {
		//success
		if(cur.size() == k)
		{
			ArrayList<Integer> temp = new ArrayList<Integer>(cur);
			Collections.sort(temp);
			res.add(temp);
			return;
		}
		//not success
		if(idx == superSet.length)
			return;
		//put in idx
		cur.add(superSet[idx]);
		getSubsets(superSet, k, idx+1, cur, res);

		//do not put in idx
		cur.remove(superSet[idx]);
		getSubsets(superSet, k, idx+1, cur, res);
	}
	
	// can do: {}, {1} | {}+2 {1}+2
}

```

====

## Balanced Binary Tree

**32.6%**

*2012-10-08*

[url](https://oj.leetcode.com/problems/balanced-binary-tree/submissions/)

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
    public boolean isBalanced(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        
        if(root == null)
            return true;
        int left = helper(root.left);
        int right = helper(root.right);
        if(Math.abs(left-right)>1)
            return false;
        else
            return isBalanced(root.left) && isBalanced(root.right);
    }
    
    int helper(TreeNode root)
    {
        if(root == null)
            return 0;
        if(root.left == null && root.right == null)
            return 1;
        if(root.left != null && root.right == null)
            return 1 + helper(root.left);
        if(root.left == null && root.right != null)
            return 1 + helper(root.right);
        return 1 + Math.max(helper(root.left), helper(root.right));
    }
    
   
}

```

====

## Climbing Stairs

**33.7%**

*2012-04-03*

[url](https://oj.leetcode.com/problems/climbing-stairs/submissions/)

`java`

```

public class Solution {
    public int climbStairs(int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(n <= 1)
            return n;
        if(n == 2)
            return 2;
        int[] dp = new int [n+1];
        dp[0] = 1;
        dp[1] = 1;
        
        for(int i = 2; i <= n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
}

```

====

## Valid Parentheses

**28.2%**

*2012-01-30*

[url](https://oj.leetcode.com/problems/valid-parentheses/submissions/)

`java`

```

public class Solution {
    public boolean isValid(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
         // Start typing your Java solution below
        // DO NOT write main() function
        
        if(s== null || s.isEmpty())
            return true;
            
        char[] c = s.toCharArray();
        
        Stack<Character> charStack = new Stack<Character> ();
        
        for(int i = 0; i < c.length; i++)
        {
            if(c[i] == '(' || c[i] == '{' || c[i] == '[')
                charStack.push(c[i]);
            else if(c[i] == ')')
            {
                if(charStack.isEmpty() || !charStack.pop().equals('('))
                    return false;
            }
            else if(c[i] == ']')
            {
                if(charStack.isEmpty() || !charStack.pop().equals('['))
                    return false;
            }
            else if(c[i] == '}')
            {
                if(charStack.isEmpty() || !charStack.pop().equals('{'))
                    return false;
            }
        }    
            
        if(charStack.isEmpty())
            return true;
            
        return false;
        
    }
}

```

====

## Remove Nth Node From End of List

**29.8%**

*2012-01-27*

[url](https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/)

`java`

```

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
         // the same Solution instance will be reused for each test case.
        ListNode pre, p1, p2 = head, dh = new ListNode(0);
        dh.next = head;
        for(int i = 0; i < n ; i++)
            p2 = p2.next;
        
        pre = dh;
        p1 = head;
        if(p2 == null)
        {
            head = head.next;
            return head;
        }
        while(p2 != null)
        {
            pre = p1;
            p1 = p1.next;
            p2 = p2.next;
        }
        pre.next = p1.next;
        return dh.next;
    }
}

```

====

## Roman to Integer

**33.7%**

*2012-01-15*

[url](https://oj.leetcode.com/problems/roman-to-integer/submissions/)

`java`

```

public class Solution {
    public int romanToInt(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int len = s.length();
        if(len <= 0)
            return 0;
        HashMap<Character, Integer> m = new HashMap<Character, Integer>();
        m.put('I', 1);
        m.put('V', 5);
        m.put('X', 10);
        m.put('L', 50);
        m.put('C', 100);
        m.put('D', 500);
        m.put('M', 1000);
        
        int sum = m.get(s.charAt(len-1));
        
        for(int i = 0; i < len -1; i++)
        {
            if(m.get(s.charAt(i)) >= m.get(s.charAt(i+1)))
                sum += m.get(s.charAt(i));
            else
                sum -= m.get(s.charAt(i));
        }
        return sum;
    }
}

```

====

## Unique Binary Search Trees

**36.3%**

*2012-08-27*

[url](https://oj.leetcode.com/problems/unique-binary-search-trees/submissions/)

`java`

```

public class Solution {
    public int numTrees(int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(n <= 1)
            return 1;
        int[] count = new int[n+1];
        count[0] = 1;
        count[1] = 1;
        
        for(int i = 2; i <= n; i++)
        {
            for(int j = 0; j < i; j++)
                 count[i] += count[j] * count[i-j-1];
        }
        return count[n];
    }
}

```

====

## Set Matrix Zeroes

**30.7%**

*2012-04-05*

[url](https://oj.leetcode.com/problems/set-matrix-zeroes/submissions/)

`java`

```

public class Solution {
    public void setZeroes(int[][] matrix) {
       // Start typing your Java solution below
		// DO NOT write main() function
		
int row = matrix.length;
		int column = matrix[0].length;
		boolean isFirstRowZero = false;
		boolean isFirstColZero = false;
		for(int i = 0; i < column; i++)
		{
			if(matrix[0][i] == 0){
				isFirstRowZero = true;
				break;
			}
		} 

		for(int i = 0; i < row; i++)
		{
			if(matrix[i][0] == 0){
				isFirstColZero = true;
				break;
			}
		}
		for(int i = 1; i < row; i++)
		{
			for(int j = 1; j < column; j++)
			{
				if(matrix[i][j] == 0)
				{
					matrix[i][0] = 0;
					matrix[0][j] = 0;
				}
			}
		}

		for(int i = 1; i < column; i++)
		{
			if(matrix[0][i] == 0){
				for(int j = 1; j < row; j++)
					matrix[j][i] = 0;
			}
		} 

		for(int i = 0; i < row; i++)
		{
			if(matrix[i][0] == 0){
				for(int j = 0; j < column; j++)
					matrix[i][j] = 0;
			}
		}

		if(isFirstRowZero)
		{
			for(int i = 0; i < column; i++)
			{
				matrix[0][i] = 0;
			}
		}

		if(isFirstColZero)
		{
			for(int i = 0; i < row; i++)
			{
				matrix[i][0] = 0;
			}
		}
    }
}

```

====

## Unique Paths II

**27.7%**

*2012-03-28*

[url](https://oj.leetcode.com/problems/unique-paths-ii/submissions/)

`java`

```

public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
         int n = obstacleGrid.length;
        int m = obstacleGrid[0].length;
        int[][] path = new int[n][m];
        if(obstacleGrid[0][0] == 1)
            return 0;
        path[0][0] = 1;
        
        for(int i = 1; i < m; i++)
            if(obstacleGrid[0][i] == 0)
                path[0][i] = path[0][i-1];
        for(int j = 1; j < n; j++)
            if(obstacleGrid[j][0] == 0)
                path[j][0] = path[j-1][0];
        
        
        for(int i = 1; i < n; i++)
            for(int j = 1; j < m; j++)
            {
                if(obstacleGrid[i][j] == 1)
                    path[i][j] = 0;
                else
                    path[i][j] = path[i-1][j] + path[i][j-1];
            }
        
        return path[n-1][m-1];
    }
}

```

====

## Reverse Integer

**40.2%**

*2011-12-25*

[url](https://oj.leetcode.com/problems/reverse-integer/submissions/)

`java`

```

public class Solution {
    public int reverse(int x) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int ret = 0, temp = 0;
        while(x != 0)
        {
            temp = x%10;
            ret = ret*10 + temp;
            x = x/10;
        }
        return ret;
    }
}

```

====

## Largest Rectangle in Histogram

**21.0%**

*2012-04-22*

[url](https://oj.leetcode.com/problems/largest-rectangle-in-histogram/submissions/)

`java`

```

public class Solution {
    public int largestRectangleArea(int[] height) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
            Stack<Integer> s = new Stack<Integer>();
	        int len = height.length;
	        int max = 0;
	        if(len == 0)
	            return 0;
	        s.push(0);
	        int i = 0;
	        for(; i <= len; i++)
	        {
	            if(i < len && (s.isEmpty() || height[s.peek()] <= height[i]))
	                s.push(i);
	            else{
	            	if(s.isEmpty())
	            		break;
	                int tmp = s.pop();
	                max = Math.max(max, (s.isEmpty()? i : i - s.peek() - 1)*height[tmp]);
	                i--;
	            }
	        }
        return max;
        
    }
}

```

====

## Merge Two Sorted Lists

**33.2%**

*2012-03-30*

[url](https://oj.leetcode.com/problems/merge-two-sorted-lists/submissions/)

`java`

```

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ListNode temp;
		ListNode l3 = null;
		ListNode dh3 = new ListNode(0);
		dh3.next = l3;
		l3 = dh3;

		while(l1 != null && l2 != null)
		{
			if(l1.val <= l2.val)
			{
				temp = new ListNode(l1.val);
				l1 = l1.next; //remember!
			}
			else
			{
				temp = new ListNode(l2.val);
				l2 = l2.next;
			}
			l3.next = temp;    
			l3 = l3.next;
		}

		if(l1 == null && l2 == null)
			return dh3.next;
		else if(l2 != null)
		{
			while(l2 != null)
			{
				temp = new ListNode(l2.val);
				l3.next = temp;    
				l3 = l3.next;
				l2 = l2.next;
			}
			return dh3.next;
		}
		else if(l1 != null)
		{
			while(l1 != null)
			{
				temp = new ListNode(l1.val);
				l3.next = temp;    
				l3 = l3.next;
				l1 = l1.next;
			}
		}

		return dh3.next; 
    }
}

```

====

## Median of Two Sorted Arrays

**17.2%**

*2011-03-27*

[url](https://oj.leetcode.com/problems/median-of-two-sorted-arrays/submissions/)

`java`

```

public class Solution {
    public double findMedianSortedArrays(int A[], int B[]) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int [] AB = new int [A.length + B.length];
		if(A.length == 0)
			AB = B;
		else if(B.length == 0)
			AB = A;
		else{
			int i = 0; int j = 0; int k = 0;
			while(i< A.length && j<B.length){
				if(A[i] <= B[j])
					AB[k++] = A[i++];
				else
					AB[k++] = B[j++];
			}
			while(i< A.length)
				AB[k++] = A[i++];
			while(j< B.length)
				AB[k++] = B[j++];
		}
		if(AB.length%2 != 0)
			return AB[AB.length/2];
		else
			return (double)(AB[AB.length/2 - 1] + AB[AB.length/2])/2;
    }
}

```

====

## Binary Tree Level Order Traversal

**30.8%**

*2012-09-28*

[url](https://oj.leetcode.com/problems/binary-tree-level-order-traversal/submissions/)

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
    public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
       
        ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>>();
        
        if(root == null)
        	return ret;
        
        Deque<TreeNode> queue = new ArrayDeque<TreeNode>();
        int curCount = 1;
        int nextCount = 0;
        TreeNode temp;
        queue.addLast(root);
        
        while(!queue.isEmpty())
        {
            ArrayList<Integer> cur = new ArrayList<Integer>();
            
            for(int i = 0; i<curCount; i++)
            {
                temp = queue.removeFirst();
                cur.add(temp.val);
                if(temp.left != null)
                {
                    nextCount ++;
                    queue.addLast(temp.left);
                }
                if(temp.right != null)
                {
                    nextCount ++;
                    queue.addLast(temp.right);
                }
            }
            ret.add(cur);
            curCount = nextCount;
            nextCount = 0;
        }
        return ret;
    }
}

```

====

## Remove Duplicates from Sorted List

**34.8%**

*2012-04-22*

[url](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/)

`java`

```

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(head == null || head.next == null)
            return head;
        int tmp = head.val;
        ListNode pre = head;
        ListNode dh = new ListNode(0);
        dh.next = head;
        head = head.next;
        while(head != null)
        {
            if(tmp == head.val){
                pre.next = head.next;
                head = head.next;
            }
            else{
            tmp = head.val;
            pre = head;
            head = head.next;
            }
        }
        return dh.next;
    }
}

```

====

## Recover Binary Search Tree

**23.4%**

*2012-09-01*

[url](https://oj.leetcode.com/problems/recover-binary-search-tree/submissions/)

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
  	public void recoverTree(TreeNode root) {
		// Note: The Solution object is instantiated only once and is reused by each test case.
		if(root == null)
			return;
		TreeNode [] swap = new TreeNode[3];
		helper(root, swap);
		int tmp = swap[0].val;
		swap[0].val = swap[1].val;
		swap[1].val = tmp;
	}

	public void helper(TreeNode root, TreeNode[] swap)
	{
		if(root == null)
			return;
	    helper(root.left, swap);
	    if(swap[2] != null && swap[2].val > root.val) {
	        if(swap[0] == null) swap[0] = swap[2];
	        swap[1] = root; //remember!!!
	    }
	    swap[2] = root;
	    helper(root.right, swap);
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
  	public void recoverTree(TreeNode root) {
		// Note: The Solution object is instantiated only once and is reused by each test case.
		if(root == null)
			return;
		TreeNode [] swap = new TreeNode[3];
		helper(root, swap);
		int tmp = swap[0].val;
		swap[0].val = swap[1].val;
		swap[1].val = tmp;
	}

	public void helper(TreeNode root, TreeNode[] swap)
	{
		if(root == null)
			return;
	    helper(root.left, swap);
	    if(swap[2] != null && swap[2].val > root.val) {
	        if(swap[0] == null) swap[0] = swap[2];
	        swap[1] = root; //remember!!!
	    }
	    swap[2] = root;
	    helper(root.right, swap);
	}
}

```

====

## Permutations

**31.3%**

*2012-03-16*

[url](https://oj.leetcode.com/problems/permutations/submissions/)

`java`

```

public class Solution {
    private ArrayList<ArrayList<Integer>> ret;
    public ArrayList<ArrayList<Integer>> permute(int[] num) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
         int len = num.length;
        ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>> ();
        boolean[] used = new boolean[len];
        if(len == 0)
            return ret;
        
        permutation(num, used, new ArrayList<Integer>(), ret);
        return ret;
    }
	private void permutation(int[] num, boolean[] used, ArrayList<Integer> buf, ArrayList<ArrayList<Integer>> ret) {
		if(buf.size() == num.length)
		{
			ret.add(buf);
			return;
		}
		
		for(int i = 0; i < num.length; i++)
		{
			if(!used[i])
			{
				used[i] = true;
				ArrayList newBuff = new ArrayList(buf);
				newBuff.add(num[i]);
				permutation(num, used, newBuff, ret);
				used[i] = false;
			}
		}
	}
}

```

====

## Convert Sorted Array to Binary Search Tree

**32.4%**

*2012-10-02*

[url](https://oj.leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/)

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
    public TreeNode sortedArrayToBST(int[] num) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        return helper(num, 0, num.length - 1);
    }
    
    public TreeNode helper(int [] num, int start, int end)
    {
        TreeNode root = null;
        if(start > end)
            return null;
        if(start == end)
            return new TreeNode(num[start]);
        if(start < end)
        {
            root = new TreeNode(num[(start + end)/2]);
            root.left = helper(num, start, (start + end)/2 - 1);
            root.right = helper(num, (start+end)/2 + 1, end);
        }
        return root;
    }
}

```

====

## Merge Sorted Array

**32.0%**

*2012-05-20*

[url](https://oj.leetcode.com/problems/merge-sorted-array/submissions/)

`java`

```

public class Solution {
    public void merge(int A[], int m, int B[], int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        
        int i = m-1, j = n-1;
        
        for(int k = m+n-1; k >= 0; --k)
        {
            if(j>=0 && (i<0 || B[j] >= A[i]))
                A[k] = B[j--];
            else
                A[k] = A[i--];
        }
        
    }
}

```

====

## Path Sum II

**27.1%**

*2012-10-14*

[url](https://oj.leetcode.com/problems/path-sum-ii/submissions/)

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
    private int sum;
    public ArrayList<ArrayList<Integer>> pathSum(TreeNode root, int sum) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        
        ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>> ();
        this.sum = sum;
        if(root == null)
            return ret;
        helper(ret, root, 0, new ArrayList<Integer>());
        return ret;
    }
    
    private void helper(ArrayList<ArrayList<Integer>> ret, TreeNode node, int cur, ArrayList<Integer> buf)
    {
        if(node == null)
            return;
        ArrayList<Integer> newBuf = new ArrayList<Integer>(buf);
        newBuf.add(node.val);
        cur += node.val;
        
        if(node.left == null && node.right == null)
        {
            if(cur == sum)
                ret.add(newBuf);
            return;
        }
        
        helper(ret, node.left, cur, newBuf);
        helper(ret, node.right, cur, newBuf);
        return;
    }
}

```

====

## Permutations II

**24.9%**

*2012-03-16*

[url](https://oj.leetcode.com/problems/permutations-ii/submissions/)

`java`

```

public class Solution {
    public ArrayList<ArrayList<Integer>> permuteUnique(int[] num) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>>();
        HashSet set = new HashSet();
        boolean[] visited = new boolean[num.length];
        if(num.length == 0)
            return ret;
            
        permute(num, visited, new ArrayList<Integer>(), set, ret);
        return ret;
    }
    
    public void permute(int[] num, boolean[] visited, ArrayList<Integer> buf, HashSet set, ArrayList<ArrayList<Integer>> ret)
    {
        if(buf.size() == num.length)
        {
            if(set.add(buf))
                ret.add(buf);
            return;
        }
        
        for(int i = 0; i < num.length; i++)
        {
            if(!visited[i])
            {
                visited[i] = true;
                ArrayList newBuf = new ArrayList(buf);
                newBuf.add(num[i]);
                permute(num, visited, newBuf, set, ret);
                visited[i] = false;
            }
        }
    }
}

```

====

## Pow(x, n)

**25.9%**

*2012-03-19*

[url](https://oj.leetcode.com/problems/powx-n/submissions/)

`java`

```

public class Solution {
    public double pow(double x, int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        boolean isNeg = false;
        boolean isXNeg = false;
        boolean isDouble = (n%2 ==0);
        if(n == 0)
            return 1;
        if(x == 0)
            return 0;
        if(x == 1)
            return 1;
        if(x == -1 && (n%2 ==1))
            return -1;
        if(x == -1 && (n%2 ==0))
            return 1;
        if(n < 0){
            isNeg = true;
            n = -1*n;
        }
        if(x < 0)
        {
            isXNeg = true;
            x = -1*x;
        }
        
        double ret = x;
        
        while(n > 1)
        {
            if(ret*x < Double.MIN_VALUE && isNeg)
                return Double.MAX_VALUE;
            
            if(ret*x < Double.MIN_VALUE && !isNeg)
                return Double.MIN_VALUE;
                
            
            if(ret*x < Double.MAX_VALUE)
            {
                ret*=x;
                n--;
                continue;
            }
            
            if(ret*x > Double.MAX_VALUE && isNeg)
                return Double.MIN_VALUE;
            if(ret*x > Double.MAX_VALUE && !isNeg)
                return Double.MAX_VALUE;
            
        }
        if(isXNeg && !isDouble)
            ret = -1*ret;
        if(!isNeg)
            return ret;
        else
            return 1.0/ret;
    }
}

```

====

## Binary Tree Zigzag Level Order Traversal

**26.6%**

*2012-09-28*

[url](https://oj.leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/)

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
    public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
       
        ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>>();
        
        if(root == null)
        	return ret;
        
        Deque<TreeNode> queue = new ArrayDeque<TreeNode>();
        int curCount = 1;
        int nextCount = 0;
        int line = 0;
        TreeNode temp;
        queue.addLast(root);
        
        while(!queue.isEmpty())
        {
            ArrayList<Integer> cur = new ArrayList<Integer>();
            
            for(int i = 0; i<curCount; i++)
            {
                temp = queue.removeFirst();
                cur.add(temp.val);
                if(temp.left != null)
                {
                    nextCount ++;
                    queue.addLast(temp.left);
                }
                if(temp.right != null)
                {
                    nextCount ++;
                    queue.addLast(temp.right);
                }
            }
            line++;
            if(line % 2 == 0)
                Collections.reverse(cur);
            ret.add(cur);
            curCount = nextCount;
            nextCount = 0;
        }
        return ret;
         
    }
}

```

====

## Add Two Numbers

**22.9%**

*2011-11-01*

[url](https://oj.leetcode.com/problems/add-two-numbers/submissions/)

`java`

```

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Start typing your Java solution below
        // DO NOT write main() function
        
        ListNode dh, l3 = new ListNode(0), tmp;
        dh = l3;
        int carry = 0;
        while(l1!=null && l2!=null)
        {
            tmp = l3;
            l3 = new ListNode((l1.val + l2.val + carry)%10);
            tmp.next = l3;
            if(l1.val + l2.val + carry >= 10)
                carry = 1;
            else carry = 0;
            l1 = l1.next;
            l2 = l2.next;
        }
        while(l1 != null)
        {
            tmp = l3;
            l3 = new ListNode((l1.val + carry)%10);
            tmp.next = l3;
           if(l1.val + carry >= 10)
                carry = 1;
            else carry = 0;
            l1 = l1.next;
        }
        while(l2 != null)
        {
            tmp = l3;
            l3 = new ListNode((l2.val + carry)%10);
            tmp.next = l3;
           if(l2.val + carry >= 10)
                carry = 1;
            else carry = 0;
            l2 = l2.next;
        }
        
        if(carry == 1){
            tmp = l3;
            l3 = new ListNode(1);
            tmp.next = l3;
        }
        
        return dh.next;
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

## Best Time to Buy and Sell Stock III

**22.2%**

*2012-11-06*

[url](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/)

`java`

```

public class Solution {
    public int maxProfit(int[] prices) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int len = prices.length;
        if(len <= 1)
            return 0;
        int [] historyProfit = new int[len];
        int [] futureProfit = new int[len];
        
        int low = prices[0], profit = 0, max = 0;
        
        for(int i = 1; i < len; i++)
        {
            profit = prices[i] - low;
            max = profit > max ? profit : max;
            historyProfit[i] = max;
            low = low > prices[i] ? prices[i] : low;
        }
        
        if(len <= 3)
            return max;
        int high = prices[len - 1];
        max = 0;
        for(int i = len - 2; i >= 0; i--)
        {
            profit = high - prices[i];
            max = profit > max ? profit : max;
            futureProfit[i] = max;
            high = high < prices[i] ? prices[i] : high;
        }
        
        max = 0;
        for(int i = 1; i < len - 1; i++)
        {
            profit = historyProfit[i] + futureProfit[i];
            max = profit > max ? profit : max;
        }
        return max;
    }
}

```

====

## Path Sum

**30.6%**

*2012-10-13*

[url](https://oj.leetcode.com/problems/path-sum/submissions/)

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
    public boolean hasPathSum(TreeNode root, int sum) {
        // Start typing your Java solution below
        // DO NOT write main() function
        
    if(root == null)
            return false;
            
        return helper(root, 0, sum);
    }
    
    private boolean helper(TreeNode node, int carry, int sum)
    {
        if(node.left == null && node.right == null)
            return sum == (carry + node.val);
        if(node.left == null && node.right != null)
            return helper(node.right, carry+node.val, sum);
        if(node.left != null && node.right == null)
            return helper(node.left, carry+node.val, sum);
        return helper(node.left, carry+node.val, sum) || helper(node.right, carry+node.val, sum);
    }
}

```

====

## Symmetric Tree

**32.1%**

*2012-09-23*

[url](https://oj.leetcode.com/problems/symmetric-tree/submissions/)

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
    public boolean isSymmetric(TreeNode root) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(root == null)
            return true;
        return helper(root.left, root.right);
    }
    public boolean helper(TreeNode left, TreeNode right)
    {
        if(left == null && right == null)
            return true;
        if(left != null && right != null)
            return (left.val == right.val) && helper(left.left, right.right) && helper(left.right, right.left);
        return false;
    }
}

```

====

## Minimum Path Sum

**31.1%**

*2012-03-28*

[url](https://oj.leetcode.com/problems/minimum-path-sum/submissions/)

`java`

```

public class Solution {
    public int minPathSum(int[][] grid) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        
       int m = grid.length;
	        int n = grid[0].length;
	        
	        int[][] dp = new int[m+1][n+1];
	        dp[0][0] = grid[0][0];
	        for(int i = 1; i < m; i++)
	        {
	            dp[i][0] = grid[i][0] + dp[i-1][0];
	        }
	        
	        for(int i = 1; i < n; i++)
	        {
	            dp[0][i] = grid[0][i]+ dp[0][i-1];
	        }
	        
	        for(int i = 1; i < m; i++)
	            for(int j = 1; j < n; j++)
	            {
	                dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]);
	                dp[i][j] += grid[i][j];
	            }
	            
	        return dp[m-1][n-1];
    }
}

```

====

## Remove Duplicates from Sorted Array

**32.2%**

*2012-02-16*

[url](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/)

`java`

```

public class Solution {
    public int removeDuplicates(int[] A) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
    int i=0;
    int j, n = A.length;
    if (n<=1) return n;

    for (j=1;j<n;j++)
    {            
        if (A[j] != A[i])
        {                
            A[++i]=A[j];
        }
    }
    return i+1;
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

## Valid Number

**11.0%**

*2012-04-02*

[url](https://oj.leetcode.com/problems/valid-number/submissions/)

`java`

```

public class Solution {
    public boolean isNumber(String s) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        return s.matches("^\\s*[+-]?(\\d+|\\d*\\.\\d+|\\d+\\.\\d*)([eE][+-]?\\d+)?\\s*$");
    }
}

```

`java`

```

public class Solution {
    public boolean isNumber(String s) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        return s.matches("^\\s*[+-]?(\\d+|\\d*\\.\\d+|\\d+\\.\\d*)([eE][+-]?\\d+)?\\s*$");
    }
}

```

`java`

```

public class Solution {
    public boolean isNumber(String s) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        return s.matches("^\\s*[+-]?(\\d+\\.\\d+|\\d+|\\.\\d+|\\d+\\.)([Ee][+-]?(\\d+))?\\s*$");
    }
}

```

====

## Implement strStr()

**21.8%**

*2012-02-18*

[url](https://oj.leetcode.com/problems/implement-strstr/submissions/)

`java`

```

public class Solution {
    public String strStr(String haystack, String needle) {
        // Start typing your Java solution below
        // DO NOT write main() function
        assert(haystack!=null && needle!=null);
        if(needle.length()==0) return haystack;
        
        int i=0;
        while(i<haystack.length()){
            if(haystack.length()-i<needle.length()) 
                break;
            if(haystack.charAt(i)==needle.charAt(0)){
                int j=i;
                while(j-i<needle.length() && haystack.charAt(j)==needle.charAt(j-i))
                    j++;
                if(j-i==needle.length()) 
                    return haystack.substring(i);
            }
            i++;
        }
        return null;
    }
}

```

====

## Plus One

**31.4%**

*2012-04-02*

[url](https://oj.leetcode.com/problems/plus-one/submissions/)

`java`

```

public class Solution {
    public int[] plusOne(int[] digits) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int len = digits.length;
        int carry = 1;
        
        for(int i = len-1; i>=0; i--)
        {
            if(digits[i] + carry < 10)
            {
                digits[i] += carry;
                carry = 0;
            }
            else{
                digits[i] = 0;
                carry = 1;
            }
        }
        
        if(carry == 0)
            return digits;
        
        int [] ret = new int [len+1];
        for(int i = 1; i <= len; i++)
            ret[i] = digits[i-1];
        ret[0] = 1;
        return ret;
    }
}

```

====

## Best Time to Buy and Sell Stock II

**36.7%**

*2012-10-30*

[url](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/)

`java`

```

public class Solution {
    public int maxProfit(int[] prices) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int len = prices.length;
        if(len <= 1)
            return 0;
        int profit = 0, low = prices[0];
        for(int i = 1; i < len; i++)
        {
            if(prices[i] > low){
                profit += prices[i] - low;
                low = prices[i];
            }
            else
                low = prices[i];
        }
        return profit;
    }
}

```

====

## Search Insert Position

**35.0%**

*2012-03-03*

[url](https://oj.leetcode.com/problems/search-insert-position/submissions/)

`java`

```

public class Solution {
    public int searchInsert(int[] A, int target) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int len = A.length;
        if(len == 0 || target <= A[0])
            return 0;
            
        if(len == 1)
            return 1;
            
        //len >= 2
        for(int i = 1; i < len; i++)
        {
            if(target <= A[i])
                return i;
        }
        return len;
    }
}

```

====

## Maximum Depth of Binary Tree

**43.8%**

*2012-09-29*

[url](https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/submissions/)

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
    public int maxDepth(TreeNode root) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(root == null)
            return 0;
        return Math.max(maxDepth(root.left) + 1, maxDepth(root.right) + 1);
    }
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

## Unique Paths

**31.3%**

*2012-03-28*

[url](https://oj.leetcode.com/problems/unique-paths/submissions/)

`java`

```

public class Solution {
    
    private int [][] up;
    public int uniquePaths(int m, int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        
        up = new int[m+1][n+1];
        up[1][1] = 1;
        
        for(int i = 2; i <= m; i++)
            up[i][1] = 1;
        
        for(int i = 2; i <= n; i++)
            up[1][i] = 1;
        
        for(int i = 2; i <= m; i++)
            for(int j = 2; j <= n; j++)
            {
                up[i][j] = up[i-1][j] + up[i][j-1];
            }
        
        return up[m][n];
        
    }
}

```

====

## Regular Expression Matching

**19.9%**

*2012-01-08*

[url](https://oj.leetcode.com/problems/regular-expression-matching/submissions/)

`java`

```

public class Solution {
    public boolean isMatch(String s, String p) {
        // Start typing your Java solution below
        // DO NOT write main() function
         if(s == null) return p == null;
    return m(s, p, 0, 0);
}
public boolean m(String s, String p, int i, int j){
    if(j == p.length()) return i == s.length();   
    if(j == p.length() - 1 || p.charAt(j + 1) != '*'){
        if(i == s.length()) return false;   
        return (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)) && m(s, p, ++i, ++j);
    }                               
    while(i < s.length() && (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)))  
        if (m(s, p, i++, j + 2)) return true;
    return m(s, p, i, j + 2);   
}
}

```

`java`

```

public class Solution {
    public boolean isMatch(String s, String p) {
        // Start typing your Java solution below
        // DO NOT write main() function
         if(s == null) return p == null;
         return helper(s, p, 0, 0);
    }
    public boolean helper(String s, String p, int i, int j){
     if(j == p.length()) return i == s.length();   
     if(j == p.length() - 1 || p.charAt(j + 1) != '*'){
         if(i == s.length()) return false;   
            return (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)) && helper(s, p, ++i, ++j);
         }                               
      while(i < s.length() && (p.charAt(j) == '.' || s.charAt(i) == p.charAt(j)))  
        if (helper(s, p, i++, j + 2)) return true;
        return helper(s, p, i, j + 2);   
    }
}

```

====

## Jump Game

**27.1%**

*2012-03-24*

[url](https://oj.leetcode.com/problems/jump-game/submissions/)

`java`

```

public class Solution {
    public boolean canJump(int[] A) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int len = A.length;
        if(len <= 0)
            return true;
        boolean [] canStep = new boolean[len];
        canStep[0] = true;
        for(int i = 0; i < len - 1; i++)
        {
            int tmp = A[i];
            if(canStep[i])
                for(int j = 0; j <= tmp && i+j < len; j++)
                {
                    canStep[i+j] = true;
                }
            i = Math.max(i, i + tmp - 1);
        }
        return canStep[len-1];
    }
}

```

====

## Letter Combinations of a Phone Number

**26.1%**

*2012-01-26*

[url](https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/)

`java`

```

public class Solution {
    public ArrayList<String> letterCombinations(String digits) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int len = digits.length();
        ArrayList<String> ret = new ArrayList<String>();
        
        if(len == 0)
        {
            ret.add("");
            return ret;
        }
            
        helper(digits, 0, ret, "");
        return ret;
    }
    
    public void helper(String digits, int index, ArrayList<String> ret, String carry)
    {
        int len = digits.length();
        if(index == len)
        {
            ret.add(carry);
            return;
        }
        
        if(index < len)
        {
            char cur = digits.charAt(index);
            if(cur == '2')
            {
                helper(digits, index+1, ret, carry+"a");
                helper(digits, index+1, ret, carry+"b");
                helper(digits, index+1, ret, carry+"c");
            }
            if(cur == '3')
            {
                helper(digits, index+1, ret, carry+"d");
                helper(digits, index+1, ret, carry+"e");
                helper(digits, index+1, ret, carry+"f");
            }
            if(cur == '4')
            {
                helper(digits, index+1, ret, carry+"g");
                helper(digits, index+1, ret, carry+"h");
                helper(digits, index+1, ret, carry+"i");
            }
            if(cur == '5')
            {
                helper(digits, index+1, ret, carry+"j");
                helper(digits, index+1, ret, carry+"k");
                helper(digits, index+1, ret, carry+"l");
            }
            if(cur == '6')
            {
                helper(digits, index+1, ret, carry+"m");
                helper(digits, index+1, ret, carry+"n");
                helper(digits, index+1, ret, carry+"o");
            }
            if(cur == '7')
            {
                helper(digits, index+1, ret, carry+"p");
                helper(digits, index+1, ret, carry+"q");
                helper(digits, index+1, ret, carry+"r");
                helper(digits, index+1, ret, carry+"s");
            }
            if(cur == '8')
            {
                helper(digits, index+1, ret, carry+"t");
                helper(digits, index+1, ret, carry+"u");
                helper(digits, index+1, ret, carry+"v");
            }
            if(cur == '9')
            {
                helper(digits, index+1, ret, carry+"w");
                helper(digits, index+1, ret, carry+"x");
                helper(digits, index+1, ret, carry+"y");
                helper(digits, index+1, ret, carry+"z");
            }
        }
        return;
    }
}

```

====

## Best Time to Buy and Sell Stock

**31.1%**

*2012-10-30*

[url](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/)

`java`

```

public class Solution {
    public int maxProfit(int[] prices) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int len = prices.length;
        if(len <= 1)
            return 0;
        int low = prices[0], profit = 0, max = 0;
        for(int i = 1; i < len; i++)
        {
            profit = prices[i] - low;
            max = max < profit ? profit: max;
            low = low > prices[i] ? prices[i] : low;
        }
        return max;
    }
}

```

====

## 3Sum

**16.7%**

*2012-01-17*

[url](https://oj.leetcode.com/problems/3sum/submissions/)

`java`

```

public class Solution {
    public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<Integer> set = new ArrayList<Integer>();
		ArrayList<ArrayList<Integer>> ret =  new ArrayList<ArrayList<Integer>>();
        HashSet<ArrayList<Integer>> hset = new HashSet<ArrayList<Integer>>();
		Arrays.sort(num);
		int len = num.length;
        if(len < 3)
            return ret;
        int j, k;
		for(int i = 0; i < len - 2; i++)
		{
            j = i+1;
            k = len - 1;
			while(j < k)
			{
			    int tmp = num[i] + num[j] + num[k];

			    if(tmp == 0){			    
			        set.add(num[i]);
			        set.add(num[j]);
			        set.add(num[k]);
			        if(hset.add(set))
			            ret.add(set);
			        set = new ArrayList<Integer>();
			        j++;
			        k--;
			    }
			    else if(tmp < 0)
			        j++;
			    else
			        k--;
			}
			
		}
		return ret;

        
    }
}

```

`java`

```

public class Solution {
    public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<Integer> set = new ArrayList<Integer>();
		ArrayList<ArrayList<Integer>> ret =  new ArrayList<ArrayList<Integer>>();
        HashSet<ArrayList<Integer>> hset = new HashSet<ArrayList<Integer>>();
		Arrays.sort(num);
		int len = num.length;
        if(len < 3)
            return ret;
        int j, k;
		for(int i = 0; i < len - 2; i++)
		{
            j = i+1;
            k = len - 1;
			while(j < k)
			{
			    int tmp = num[i] + num[j] + num[k];

			    if(tmp == 0){			    
			        set.add(num[i]);
			        set.add(num[j]);
			        set.add(num[k]);
			        if(hset.add(set))
			            ret.add(set);
			        set = new ArrayList<Integer>();
			        j++;
			        k--;
			    }
			    else if(tmp < 0)
			        j++;
			    else
			        k--;
			}
			
		}
		return ret;

        
    }
}

```

====

## Binary Tree Level Order Traversal II

**31.1%**

*2012-10-01*

[url](https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/submissions/)

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
    public ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
        // Note: The Solution object is instantiated only once and is reused by each test case.

        ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>>();
        if(root == null)    return ret;
        
        Deque<TreeNode> queue = new ArrayDeque<TreeNode>();
        int curCount = 1;
        int nextCount = 0;
        TreeNode temp;
        queue.addLast(root);
        
        while(!queue.isEmpty())
        {
            ArrayList<Integer> cur = new ArrayList<Integer>();
            for(int i = 0; i<curCount; i++)
            {
                temp = queue.removeFirst();
                cur.add(temp.val);
                if(temp.left != null)
                {
                    nextCount ++;
                    queue.addLast(temp.left);
                }
                if(temp.right != null)
                {
                    nextCount ++;
                    queue.addLast(temp.right);
                }
            }
            ret.add(cur);
            curCount = nextCount;
            nextCount = 0;
        }
        
        Collections.reverse(ret);
        return ret;
    }
}

```

====

