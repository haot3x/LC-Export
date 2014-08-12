## Remove Element

**33.3%**

*2012-02-16*

[url](https://oj.leetcode.com/problems/remove-element/submissions/)

`java`

```

public class Solution {
    public int removeElement(int[] A, int elem) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int i=0, j=0;
        while(j<A.length){
            if(A[j]!=elem){
                A[i]=A[j];
                i++; 
            }
            j++;
        }
        return i;
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

public class ListNode {
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
        
        if(head == null || head.next == null)
            return head;
        
        ListNode cur,prev;
        ListNode n1,n2;
        
        ListNode newHead = head.next;
        cur = head;
        prev = null;
        
        while(cur != null && cur.next != null )
        {
            n1 = cur;
            n2 = cur.next;
            cur = n2.next;
            
            n1.next = n2.next;
            n2.next = n1;

            if(prev != null)
                prev.next = n2;
            
            prev = n1;
        }
        
        return newHead;
    }
}

```

====

## Word Ladder

**18.1%**

*2013-02-10*

[url](https://oj.leetcode.com/problems/word-ladder/submissions/)

`java`

```

public class Solution {
    
    public int ladderLength(String start, String end, Set<String> dict) {
        
        Deque<String> qCur = new LinkedList<String>();
        Deque<String> qNext = new LinkedList<String>();
        
        qCur.addLast(start);
        int step = 0;
        
        while(qCur.size() != 0)
        {
            String cur = qCur.removeFirst();
            if(cur.equals(end))
                return ++step;
                
            
            for(int i=0;i<cur.length();++i)
            {
                for(char c='a';c<='z';c++)
                {
                    char[] chars = cur.toCharArray();
                    chars[i] = c;
                    String child = new String(chars);
                    if(dict.contains(child))
                    {
                        qNext.addLast(child);
                        dict.remove(child);
                    }
                }
                
            }
            
            if(qCur.size() == 0)
            {
                Deque<String> tmp = qCur;
                qCur = qNext;
                qNext = tmp;
                step++;
            }
            
        }
        
        return 0;
        
    }
    
    //Time Limit Exceeded
    /*
    public int ladderLength(String start, String end, Set<String> dict) {
    
        Set<String> visited = new HashSet<String>();
        
        Deque<String> qCur = new LinkedList<String>();
        Deque<String> qNext = new LinkedList<String>();
        
        qCur.addLast(start);
        int step = 0;
        
        while(qCur.size() != 0)
        {
            String cur = qCur.removeFirst();
            if(cur.equals(end))
                return step++;

            for(String s:dict)
            {
                if(visited.contains(s) == false && diffOneChar(s,cur) == true)
                {
                    qNext.addLast(s);
                    visited.add(s);
                }
            }

            if(qCur.size() == 0)
            {
                Deque<String> tmp = qCur;
                qCur = qNext;
                qNext = tmp;
                step++;
            }
            
        }
        
        return 0;
        
    }
    
    
    private boolean diffOneChar(String s1,String s2)
    {
        if(s1 == null || s2 == null || s1.equals("") || s2.equals(""))
            return false;
        
        if(s1.length() != s2.length())
            return  false;

            
            
        int cnt = 0;
        for(int i=0;i<s1.length();++i)
            if(s1.charAt(i) != s2.charAt(i))
            {
                cnt++;
                if(cnt > 1)
                    return false;
            }    

        return (cnt == 1);
    }
    */
    
    
}

```

`java`

```

public class Solution {

    public int ladderLength(String start, String end, Set<String> dict) {
        
        Deque<String> qCur = new LinkedList<String>();
        Deque<String> qNext = new LinkedList<String>();
        
        qCur.addLast(start);
        int step = 0;
        
        while(qCur.size() != 0)
        {
            String cur = qCur.removeFirst();
            if(cur.equals(end))
                return (step+1);
                
            for(int i=0;i<cur.length();++i)
            {
                for(char c='a';c<='z';c++)
                {
                    char[] chars = cur.toCharArray();
                    chars[i] = c;
                    String child = new String(chars);
                    if(dict.contains(child))
                    {
                        qNext.addLast(child);
                        dict.remove(child);
                    }
                }
            }
            
            if(qCur.size() == 0)
            {
                Deque<String> tmp = qCur;
                qCur = qNext;
                qNext = tmp;
                step++;
            }
            
        }
        
        return 0;
        
    }

    //With Time Limit Exceeded
    /*    
    public int ladderLength(String start, String end, Set<String> dict) {
    
        Set<String> visited = new HashSet<String>();
        
        Deque<String> qCur = new LinkedList<String>();
        Deque<String> qNext = new LinkedList<String>();
        
        qCur.addLast(start);
        int step = 0;
        
        while(qCur.size() != 0)
        {
            String cur = qCur.removeFirst();
            if(cur.equals(end))
                return (step+1);

            for(String s:dict)
            {
                if(visited.contains(s) == false && diffOneChar(s,cur) == true)
                {
                    qNext.addLast(s);
                    visited.add(s);
                }
            }

            if(qCur.size() == 0)
            {
                Deque<String> tmp = qCur;
                qCur = qNext;
                qNext = tmp;
                step++;
            }
            
        }
        
        return 0;
        
    }
    
    
    private boolean diffOneChar(String s1,String s2)
    {
        if(s1 == null || s2 == null || s1.equals("") || s2.equals(""))
            return false;
        
        if(s1.length() != s2.length())
            return  false;

            
            
        int cnt = 0;
        for(int i=0;i<s1.length();++i)
            if(s1.charAt(i) != s2.charAt(i))
            {
                cnt++;
                if(cnt > 1)
                    return false;
            }    

        return (cnt == 1);
    }
    */
    
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
        
        int bestStart,bestEnd,bestSum,curSum;
        int len = A.length;
        
        curSum = 0;
        bestSum = 0;
        
        for(int i=0;i<len;++i)
        {
            if(curSum < 0)
            {
                curSum = 0;
                bestStart = i;
            }
            
            curSum += A[i];
            
            if(bestSum < curSum || i == 0)
            {
                bestSum = curSum;
                bestEnd = i;
            }
            
            
        }
        
        return bestSum;
    }
}

```

====

## Merge Two Sorted Lists

**33.1%**

*2012-03-30*

[url](https://oj.leetcode.com/problems/merge-two-sorted-lists/submissions/)

`java`

```

public class ListNode {
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
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ListNode head = new ListNode(-1);
        ListNode tail = head;
        while(l1 != null && l2 != null)
        {
            if(l1.val < l2.val)
            {
                tail.next = l1;
                l1 = l1.next;
                tail = tail.next;
                tail.next = null;
            }
            else
            {
                tail.next = l2;
                l2 = l2.next;
                tail = tail.next;
                tail.next= null;
            }
        }
        
        if(l1 != null)
            tail.next = l1;
        if(l2 != null)
            tail.next = l2;
        return head.next;    
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

public class Solution {
    public boolean hasCycle(ListNode head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(head == null || head.next == null)
            return false;
        ListNode fast,slow;
        slow = head;
        fast = head.next;
        while(fast != null && fast.next !=  null)
        {
            if(fast.val == slow.val)
                return true;
            fast = fast.next.next;
            slow = slow.next;
        }
        return false;
    }
}

```

`java`

```

public class Solution {
    public boolean hasCycle(ListNode head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(head == null || head.next == null)
            return false;
        ListNode fast,slow;
        slow = head;
        fast = head.next;
        while(fast != null && fast.next !=  null)
        {
            if(fast.val == slow.val)
                return true;
            fast = fast.next.next;
            slow = slow.next;
        }
        return false;
    }
}

```

====

## Pow(x, n)

**26.0%**

*2012-03-19*

[url](https://oj.leetcode.com/problems/powx-n/submissions/)

`java`

```

public class Solution {
    public double pow(double x, int n) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(n==0)
            return 1;
        if(n==1)
            return x;
        
        if(n>0)
        {
            double tmp = pow(x,n/2);
            if(n%2 != 0)
                return tmp*tmp*x;
            else
                return tmp*tmp;
        }
        else
        {
            double tmp = pow(x,(-n)/2);
            if(n%2 != 0)
                return 1.0/(tmp*tmp*x);
            else
                return 1.0/(tmp*tmp);
        }
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
    
    public List<String> generateParenthesis(int n) {
        ArrayList<String> res = new ArrayList<String>();
        helper(n,res,0,0,"");
        return res;
    }
    
    
    public void helper(int n,ArrayList<String> res, int left, int right, String cur)
    {
        if(left == n)
        {
            for(int i=0;i<n-right;++i)
                cur = cur + ")";
            res.add(cur);
        }
        else if(left > right)
        {
            helper(n,res,left+1,right,cur+"(");
            helper(n,res,left,right+1,cur+")");
        }
        else if(left == right)
        {
            helper(n,res,left+1,right,cur+"(");
        }
        
    }
    
    
    
    public List<String> _generateParenthesis(int n) {
        
        HashSet<String> result = helper(n);
        return new ArrayList(result);
    }

    public HashSet<String> helper(int n)
    {
        HashSet<String> result = new HashSet<String>();
        
        if(n == 1)
        {
            result.add("()");
            return result;
        }
        
        HashSet<String> sub = helper(n-1);
        for(String s:sub)
        {
            String tmp;
            tmp = "()" + s;
            if(!result.contains(tmp))
                result.add(tmp);
            tmp = "(" + s + ")";
            if(!result.contains(tmp))
                result.add(tmp);
            tmp = s + "()";
            if(!result.contains(tmp))
                result.add(tmp);
        }
        return result;
        
    }
    
}

```

`java`

```

public class Solution {
    
    // optimal 
    public List<String> _generateParenthesis(int n) {
        ArrayList<String> res = new ArrayList<String>();
        helper(n,res,0,0,"");
        return res;
    }
    
    public void helper(int n,ArrayList<String> res, int left, int right, String cur)
    {
        if(left == n)
        {
            for(int i=0;i<n-right;++i)
                cur = cur + ")";
            res.add(cur);
        }
        else if(left > right)
        {
            helper(n,res,left+1,right,cur+"(");
            helper(n,res,left,right+1,cur+")");
        }
        else if(left == right)
        {
            helper(n,res,left+1,right,cur+"(");
        }
        
    }
    
    
    // my original approach
    public List<String> generateParenthesis(int n) {
        
        HashMap<Integer,HashSet<String>> map = new HashMap<Integer,HashSet<String>>();
        helper(n,map);
        return new ArrayList(map.get(n));
    }

    public void helper(int n,HashMap<Integer,HashSet<String>> map)
    {
        HashSet<String> result = new HashSet<String>();
        if(n == 1)
        {
            result.add("()");
            map.put(1,result);
            return;
        }
        
        helper(n-1,map);
        HashSet<String> sub = map.get(n-1);
        for(String s:sub)
        {
            String tmp = "(" + s + ")";
            if(!result.contains(tmp))
                result.add(tmp);
        }
        map.put(n,result);    
                
        for(int i=1;i<n;i++)
            cartesianProduct(i,n-i,map);
    
    }
    
    // put cartesian product of map.get(n1) X map.get(n2) into map
    private void cartesianProduct(int n1, int n2, HashMap<Integer,HashSet<String>> map)
    {
        HashSet<String> res1 = map.get(n1);
        HashSet<String> res2 = map.get(n2);
        
        HashSet<String> res = map.get(n1+n2);
        
        for(String s1:res1)
            for(String s2:res2)
            {
                String tmp;
                
                tmp = s1+s2;
                if(!res.contains(tmp))
                    res.add(tmp);
                tmp = s2+s1;
                if(!res.contains(tmp))
                    res.add(tmp);
            }   
        
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
        
        int len = s.length();
        boolean[] cando = new boolean[len];
        /*
            s[0:i] = true if s[0:k) && s[k:i] for 0<k<=i
        */
        
        cando[0] = dict.contains(s.substring(0,1));
        for(int i=1;i<len;++i)
            for(int k=0;k<=i;++k)
            {
                cando[i] = dict.contains(s.substring(0,i+1)) || (cando[k] && dict.contains(s.substring(k+1,i+1)));
                if(cando[i])
                    break;
            }
        
        return cando[len-1];
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

public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(root == null || (root.left == null && root.right == null))
            return;
        
        root.left.next = root.right;
        if(root.next != null)
            root.right.next = root.next.left;
        
        connect(root.left);
        connect(root.right);
    }
}

```

`java`

```

public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(root == null || (root.left == null ))
            return;
        
        root.left.next = root.right;
        if(root.next != null)
            root.right.next = root.next.left;
        
        connect(root.left);
        connect(root.right);
    }
}

```

`java`

```

public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(root == null || (root.left == null && root.right == null))
            return;
        
        root.left.next = root.right;
        if(root.next != null)
            root.right.next = root.next.left;
        
        connect(root.left);
        connect(root.right);
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
        // Note: The Solution object is instantiated only once and is reused by each test case.
        HashMap<Integer,ArrayList<Integer>> indexMap = new HashMap<Integer,ArrayList<Integer>>();
        
        for(int i=0;i<numbers.length;++i)
        {
            if(indexMap.containsKey(numbers[i]))
            {
                ArrayList<Integer> tmp = indexMap.get(numbers[i]);
                tmp.add(i);
                indexMap.put(numbers[i],tmp);
            }
            else
            {
                ArrayList<Integer> l = new ArrayList<Integer>();
                l.add(i);
                indexMap.put(numbers[i],l);
            }
        }
        
        int diff;
        ArrayList<Integer> listall = new ArrayList<Integer>();
        for(Map.Entry<Integer,ArrayList<Integer>> entry : indexMap.entrySet())
        {
            diff = target - entry.getKey(); 
            if(indexMap.containsKey(diff))
            {
                if(diff == entry.getKey())
                {
                    listall.addAll(entry.getValue());
                }
                else
                {
                    listall.addAll(entry.getValue());
                    listall.addAll(indexMap.get(diff));
                }
                break;
            }
        }
        
        
        int j=0;
        int[] indexes = new int[2];
        for(Integer i : listall)
            indexes[j++] = i;
        
        indexes[0]++;
        indexes[1]++;
        
        if(indexes[0]>indexes[1])
        {
            int tmp = indexes[0];
            indexes[0] = indexes[1];
            indexes[1] = tmp;
        }    
    
        return indexes;
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

public class TreeNode {
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
        ArrayList<Integer> list = new ArrayList<Integer>();
        helper(root,list);
        return list;
    }
    
    public void helper(TreeNode root, ArrayList<Integer> list)
    {
        if(root == null)
            return;
        list.add(root.val);
        helper(root.left,list);
        helper(root.right,list);
    }
}

```

====

## Pascal's Triangle

**31.7%**

*2012-10-28*

[url](https://oj.leetcode.com/problems/pascals-triangle/submissions/)

`java`

```

public class Solution {
    public ArrayList<ArrayList<Integer>> generate(int numRows) {
        ArrayList<ArrayList<Integer>> lists = new ArrayList<ArrayList<Integer>>();
        
        for(int i=0;i<numRows;++i)
        {
            ArrayList<Integer> layer = new ArrayList<Integer>();
            if(i==0)
                layer.add(1);
            else
            {
                ArrayList<Integer> prev = lists.get(i-1);
                layer.add(1);
                for(int j=0;j<i-1;++j)
                    layer.add(prev.get(j)+prev.get(j+1));
                layer.add(1);
            }
            
            lists.add(layer);
        }
        return lists;
        
    }
}

```

====

## Reverse Words in a String

**14.0%**

*2014-03-05*

[url](https://oj.leetcode.com/problems/reverse-words-in-a-string/submissions/)

`java`

```

public class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        if(s.equals(""))
            return "";
        
        String[] tokens = s.split("\\s+");
        StringBuffer sb = new StringBuffer();
        int cnt = tokens.length;
        
        for(int i=cnt-1;i>=0;--i)
        {
            sb.append(tokens[i]);
            sb.append(" ");
        }
        
        String rs = sb.toString();
        int len = rs.length();
        return rs.substring(0,len-1);
    }
}

```

====

## Balanced Binary Tree

**32.6%**

*2012-10-08*

[url](https://oj.leetcode.com/problems/balanced-binary-tree/submissions/)

`java`

```

public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isBalanced(TreeNode root) {
        if(root == null)
            return true;
        
        int diff = height(root.left) - height(root.right); 
        if (diff > 1 || diff < -1)
            return false;
        return isBalanced(root.left) && isBalanced(root.right);
    }
    
    public int height(TreeNode root)
    {
        if(root == null)
            return 0;
        int l = height(root.left);
        int r = height(root.right);
        int max = (l>r)?l:r;
        return max+1;
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
        // Note: The Solution object is instantiated only once and is reused by each test case.
        //cnt[x] = cnt[x-1] + cnt[x-2]
        
        int[] cnt = new int[n+1];
        cnt[0] = cnt[1] = 1;
        
        for(int i=2;i<=n;++i)
        {
            cnt[i] = cnt[i-1] + cnt[i-2];
        }
        
        return cnt[n];
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
        int left,right,mid;
        left = 0;
        right = A.length-1;
        Boolean found = false;
        while(left <= right)
        {
            if(A[left] == target)
                return left;
            if(A[right] == target)
                return right;

            mid = (left+right)/2;
            if(A[mid] == target)
                return mid;
            
            if(A[mid] < target)
                left = mid+1;
            if(A[mid] > target)
                right = mid-1;    
        }
        
        return left;
        
    }
}

```

`java`

```

public class Solution {
    public int searchInsert(int[] A, int target) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int left,right,mid;
        left = 0;
        right = A.length-1;
        Boolean found = false;
        while(left <= right)
        {
            if(A[left] == target)
                return left;
            if(A[right] == target)
                return right;

            mid = (left+right)/2;
            if(A[mid] == target)
                return mid;
            
            if(A[mid] < target)
                left = mid+1;
            if(A[mid] > target)
                right = mid-1;    
        }
        
        return left;
        
    }
}

```

====

## Max Points on a Line

**10.8%**

*2013-11-22*

[url](https://oj.leetcode.com/problems/max-points-on-a-line/submissions/)

`java`

```

public int maxPoints(Point[] points) {
        
        if(points.length <= 1)
        	return points.length;
        
    	HashMap<Double,Integer> map = new HashMap<Double,Integer>();
        int maxNum = 0;
    	
        for(int i=0;i<points.length;i++)
        {
        	map.clear();
        	
        	int max = 0;
    	    int dupCnt = 1; // for the point itself

        	for(int j=0;j<points.length;j++)
        	{
        		if(i==j)
        			continue;
        	
        		Point p1 = points[i];
        		Point p2 = points[j];
        	
        		if(p1.x == p2.x && p1.y == p2.y)
        		{
        		    dupCnt++;
        		    continue;
        		}
        			
        		double k = (p1.x == p2.x) ? Double.MAX_VALUE:(double)(p1.y-p2.y)/(p1.x-p2.x);
        		if(map.containsKey(k))
        			map.put(k,map.get(k)+1);
        		else
        			map.put(k,1);

        			
        		if(map.get(k) > max)
        	        max = map.get(k);
        		
        	}
        	
        	if((max+dupCnt) > maxNum)
        	    maxNum = max+dupCnt;
        	
        }
    	
    	return maxNum;
    	
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
        int bestP,buyIdx,sellIdx;
        bestP = buyIdx = 0;
        
        for(int i=1;i<prices.length;++i)
        {
            if(prices[i] < prices[buyIdx])
                buyIdx = i;
            
            if(bestP < (prices[i] - prices[buyIdx]))
            {
                bestP = prices[i] - prices[buyIdx];
                sellIdx = i;
            }
            
        }
        
        return bestP;
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
        int[] nums = new int[n+1];
        if(n==0 || n==1)
            return 1;
        nums[0] = 1;
        nums[1] = 1;
   
        // if select k, left = [0,k-1], k, right = [k+1,n]
        // nums(n) = sum nums(0,k-1)*nums(k+1,n) for k=1..n-1 , k is select k as the root
        // build the DP from bottom up
        for(int i=2;i<=n;++i)
        {
            int sum = 0;
            for(int k=1;k<=i;++k)
                sum += nums[k-1] * nums[i-k];
            nums[i] = sum;
        }
        return nums[n];
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
        // Note: The Solution object is instantiated only once and is reused by each test case.
        char[] chars = Integer.toString(x).toCharArray();
        int length = Integer.toString(x).length();
        char temp;
        for(int i=0;i<length/2;++i)
        {
            temp = chars[i];
            chars[i] = chars[length-1-i];
            chars[length-1-i] = temp;
        }
        String str;
        if (chars[length-1] == '-')
            str = "-" + String.valueOf(chars,0,length-1);
        else
            str = String.valueOf(chars);
        return Integer.parseInt(str);
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

public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if(root == null)
            return true;
        return helper(root.left,root.right);
    }
    
    public boolean helper(TreeNode n1, TreeNode n2)
    {
        if(n1 == null && n2 == null)
            return true;
        if(n1 == null || n2 == null)
            return false;
        
        if(n1.val != n2.val)
            return false;
            
        return helper(n1.left,n2.right) && helper(n1.right,n2.left);
    }
}

```

`java`

```

public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        return interative(root);
        
        // recursive
        //if(root == null)
        //    return true;
        //return helper(root.left,root.right);
    }
    
    public boolean interative(TreeNode root)
    {
        if(root == null)
            return true;
        
        // linkedlist permits null value
        LinkedList<TreeNode> lt = new LinkedList<TreeNode>();
        LinkedList<TreeNode> rt = new LinkedList<TreeNode>();
        lt.addFirst(root.left);
        rt.addFirst(root.right);
        TreeNode n1 = null, n2 = null;
        while(lt.size()!= 0 && rt.size() != 0)
        {
            n1 = lt.removeLast();
            n2 = rt.removeLast();
            if(n1 == null && n2 == null)
                continue;
            if(n1 == null || n2 == null)
                return false;
            if(n1.val != n2.val)
                return false;
            lt.addFirst(n1.left);
            lt.addFirst(n1.right);
            
            rt.addFirst(n2.right);
            rt.addFirst(n2.left);
        }
        return true;
    }
    
    public boolean helper(TreeNode n1, TreeNode n2)
    {
        if(n1 == null && n2 == null)
            return true;
        if(n1 == null || n2 == null)
            return false;
        
        if(n1.val != n2.val)
            return false;
            
        return helper(n1.left,n2.right) && helper(n1.right,n2.left);
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

public class ListNode {
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
        
        ListNode nd = head;
        int prev = nd.val; 
        
        while(nd != null && nd.next != null)
        {
            if(nd.next.val == nd.val)
                nd.next = nd.next.next;
            else
                nd = nd.next;
        }
        return head;
    }
}

```

`java`

```

public class ListNode {
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
        
        ListNode nd = head;
        while(nd.next != null)
        {
            if(nd.next.val == nd.val)
                nd.next = nd.next.next;
            else
                nd = nd.next;
        }
        return head;
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
    public ArrayList<ArrayList<Integer>> permute(int[] num) {
        ArrayList<ArrayList<Integer>> ret = new ArrayList<ArrayList<Integer>>();
        
        int len = num.length;
        if(len == 1)
        {
            ArrayList<Integer> l = new ArrayList<Integer>();
            l.add(num[0]);
            ret.add(l);
            return ret;
        }
        
        for(int i=0;i<len;++i)
        {
            int head = num[i];
            int[] tail = new int[len-1];
            for(int j=0,k=0;j<len;++j)
                if(j!=i)
                    tail[k++] = num[j];
            
            ArrayList<ArrayList<Integer>> sublist = permute(tail);
            for(ArrayList<Integer> sl:sublist)
            {
                addLast(sl,head);
                ret.add(sl);
            }
    
        }
        
        return ret;
    }
    
    void addLast(ArrayList<Integer> list, int i)
    {
        list.add(0,i);
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

public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode sortedArrayToBST(int[] num) {
        return helper(num,0,num.length);
    }
    
    public TreeNode helper(int[] num, int start, int end)
    {
        if(start >= end)
            return null;
        
        int mid = (start+end)/2;
        TreeNode root = new TreeNode(num[mid]);
        root.left = helper(num, start,mid);
        root.right = helper(num, mid+1,end);
        return root;
    }
    
}

```

====

## Evaluate Reverse Polish Notation

**19.8%**

*2013-11-27*

[url](https://oj.leetcode.com/problems/evaluate-reverse-polish-notation/submissions/)

`java`

```

public class Solution {
    public int evalRPN(String[] tokens) {
    	
        LinkedList<Integer> ll = new LinkedList<Integer>(); 
    	
    	for(String s:tokens)
    	{
    		//System.out.println(s);
    		if(isNum(s))
    		{
    			ll.push(Integer.parseInt(s));
    		}
    		else
    		{
    			Integer n2 = ll.pop();
    			Integer n1 = ll.pop();
    			if(s.equals("+"))
    				ll.push(n1+n2);
    			else if(s.equals("-"))
    				ll.push(n1-n2);
    			else if(s.equals("*"))
    				ll.push(n1*n2);
    			else if(s.equals("/"))
    				ll.push(n1/n2);
    			else
    				System.out.println("invalid operand" + s);
    			
    		}
    	}
    	
    	return (int)ll.peek();
    }
    
    	

    
    public static boolean isNum(String strNum) {
        boolean ret = true;
        try {

            Double.parseDouble(strNum);

        }catch (NumberFormatException e) {
            ret = false;
        }
        return ret;
    }
}

```

`java`

```

public class Solution {
    public int evalRPN(String[] tokens) {
    	
        LinkedList<Integer> ll = new LinkedList<Integer>(); 
    	
    	for(String s:tokens)
    	{
    		//System.out.println(s);
    		if(isNum(s))
    		{
    			ll.push(Integer.parseInt(s));
    		}
    		else
    		{
    			Integer n2 = ll.pop();
    			Integer n1 = ll.pop();
    			if(s.equals("+"))
    				ll.push(n1+n2);
    			else if(s.equals("-"))
    				ll.push(n1-n2);
    			else if(s.equals("*"))
    				ll.push(n1*n2);
    			else if(s.equals("/"))
    				ll.push(n1/n2);
    			else
    				System.out.println("invalid operand" + s);
    			
    		}
    	}
    	
    	return (int)ll.peek();
    }
    
    	

    
    public static boolean isNum(String strNum) {
        boolean ret = true;
        try {

            Double.parseDouble(strNum);

        }catch (NumberFormatException e) {
            ret = false;
        }
        return ret;
    }
}

```

====

## Path Sum

**30.5%**

*2012-10-13*

[url](https://oj.leetcode.com/problems/path-sum/submissions/)

`java`

```

public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null)
            return false;


        if(root.left == null && root.right == null)
            return root.val == sum;
        
        boolean left,right;
        left = right = false;
        if(root.left != null)
            left = hasPathSum(root.left,sum-root.val);
        if(root.right != null)
            right = hasPathSum(root.right,sum-root.val);
        
        return (left || right);
        
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
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int len = A.length;
        if(len  == 0 || len == 1)
            return len;
        
        int k=0;
        int prev = A[0];
        for(int i=1;i<len-k;++i)
        {
            if(prev == A[i])
            {
                for(int j=i;j<len-1;++j)
                    A[j] = A[j+1];
                i--;
                k++;
            }
            else
            {
                prev = A[i];
            }
        }
        return (len-k);
        
    }
}

```

`java`

```

public class Solution {
    public int removeDuplicates(int[] A) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int len = A.length;
        if(len  == 0 || len == 1)
            return len;
        
        int insertPos = 0;
        for(int i=1;i<len;i++)
        {
            if(A[insertPos] != A[i])
                A[++insertPos] = A[i];
        }
        return ++insertPos;
        
        /*        
        int k=0;
        int prev = A[0];
        for(int i=1;i<len-k;++i)
        {
            if(prev == A[i])
            {
                for(int j=i;j<len-1;++j)
                    A[j] = A[j+1];
                i--;
                k++;
            }
            else
            {
                prev = A[i];
            }
        }
        return (len-k);
        */
    }
}

```

====

## Single Number

**45.7%**

*2013-10-01*

[url](https://oj.leetcode.com/problems/single-number/submissions/)

`java`

```

public class Solution {
    public int singleNumber(int[] A) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i=0;i<A.length;++i)
        {
            if(map.containsKey(A[i]))
                map.put(A[i],map.get(A[i])+1);
            else
                map.put(A[i],1);
        }
        
        for(Integer k:map.keySet())
        {
            if(map.get(k)==1)
                return k;
        }    
        
        return -1;
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
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if(prices == null || prices.length < 2)
            return 0;
        
        int profit = 0;
        for(int i=1;i<prices.length;++i)
        {
            if(prices[i]>prices[i-1])
                profit += prices[i]-prices[i-1];
        }
        
        return profit;
    }
}

```

`java`

```

public class Solution {
    public int maxProfit(int[] prices) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int profit = 0;
        for(int i=1;i<prices.length;++i)
        {
            if(prices[i]>prices[i-1])
                profit += prices[i]-prices[i-1];
        }
        
        return profit;
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

public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ArrayList<Integer> inorderTraversal(TreeNode root) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
        
        TreeNode cur = root;
        while(stack.size() != 0 || cur != null)
        {
            while(cur != null)
            {
                stack.push(cur);
                cur = cur.left;
            }
            
            cur = stack.pop();
            
            list.add(cur.val);
            cur = cur.right;
            
        }
        
        return list;
        
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

public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int maxDepth(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if(root == null)
            return 0;
        
        return Math.max(maxDepth(root.left),maxDepth(root.right)) + 1;
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

public class TreeNode {
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
        if ( (p == null && q != null) || (p != null && q == null) )
            return false;
        
        if(p.val == q.val)
            return isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
        else
            return false;
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
        int a,b,i;
        a = m-1;
        b = n-1;
        i = m+n-1;
        
        while(a >=0 && b >= 0)
        {
            if(A[a]<B[b])
                A[i--] = B[b--];
            else
                A[i--] = A[a--];
        }
        
        while(a >=0)
        {
            A[i--] = A[a--];
        }
        
        while(b >= 0)
        {
            A[i--] = B[b--];
        }
        
    }
}

```

`java`

```

public class Solution {
    public void merge(int A[], int m, int B[], int n) {
        int a,b,i;
        a = m-1;
        b = n-1;
        i = m+n-1;
        
        while(a >=0 && b >= 0)
            A[i--] = (A[a]<B[b])?B[b--]:A[a--];
        
        while(a >=0)
            A[i--] = A[a--];
        
        while(b >= 0)
            A[i--] = B[b--];
        
    }
}

```

====

## Sort List

**20.4%**

*2013-11-16*

[url](https://oj.leetcode.com/problems/sort-list/submissions/)

`java`

```

public class Solution {
    public ListNode sortList(ListNode head) {
        return mergeSort(head);
    }
    
    private ListNode merge(ListNode n1,ListNode n2)
    {
        if(n1 == null)
            return n2;
        if(n2 == null)
            return n1;
        
        ListNode head,tail;
        if(n1.val<n2.val)
        {
            head = n1;
            n1 = n1.next;
        }
        else
        {
            head = n2;
            n2 = n2.next;
        }
        
        tail = head;
        
        while(n1 != null && n2 != null)
        {
            if(n1.val<n2.val)
            {
                tail.next = n1;
                n1 = n1.next;
            }
            else
            {
                tail.next = n2;
                n2 = n2.next;
            }

            tail = tail.next;
        }
        
        if(n1 != null)
            tail.next = n1;
        
        if(n2 != null)
            tail.next = n2;
            
        return head;
        
    }
    
    private ListNode mergeSort(ListNode head)
    {
        if(head == null || head.next == null)
            return head;
        
        ListNode mid,tail,n1,n2,midPrev;
        midPrev = mid = tail = head;
        
        while(tail != null && tail.next != null)
        {
            midPrev = mid;
            mid = mid.next;
            tail = tail.next.next;
        }
        
        midPrev.next = null;
        
        n1 = mergeSort(head);
        n2 = mergeSort(mid);
        
        return merge(n1,n2);
        
    }
    
    
}

```

`java`

```

public class Solution {
    public ListNode sortList(ListNode head) {
        return mergeSort(head);
    }
    
    private ListNode merge(ListNode n1,ListNode n2)
    {
        if(n1 == null)
            return n2;
        if(n2 == null)
            return n1;
        
        ListNode head,tail;
        if(n1.val<n2.val)
        {
            head = n1;
            n1 = n1.next;
        }
        else
        {
            head = n2;
            n2 = n2.next;
        }
        
        tail = head;
        
        while(n1 != null && n2 != null)
        {
            if(n1.val<n2.val)
            {
                tail.next = n1;
                n1 = n1.next;
            }
            else
            {
                tail.next = n2;
                n2 = n2.next;
            }

            tail = tail.next;
        }
        
        if(n1 != null)
            tail.next = n1;
        
        if(n2 != null)
            tail.next = n2;
            
        return head;
    }
    
    private ListNode mergeSort(ListNode head)
    {
        if(head == null || head.next == null)
            return head;
        
        ListNode mid,tail,midPrev;
        midPrev = mid = tail = head;
        
        while(tail != null && tail.next != null)
        {
            midPrev = mid;
            mid = mid.next;
            tail = tail.next.next;
        }
        midPrev.next = null;
        
        return merge(mergeSort(head),mergeSort(mid));
        
    }
    
    
}

```

====

