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

## Single Number

**45.8%**

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

`python`

```

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        res = ""    # result string
        word = ""   # single word string
        for ch in s:
            if (ch!=' '):
                word+=ch
            if (ch==' '):
                if (len(word)!=0):
                    if (res!=""):   # add space between words
                        res = ' ' + res
                    res = word + res
                    word = ""
                
        if (len(word)!=0):  #handle the final word
            if (res!=""):
                res = ' ' + res
            res = word + res
             
        return res

```

`cpp`

```

class Solution {
public:
    void reverseWords(string &s) {
        string word; //tmp string to store each word
        string res; // result string
        int i=0;
        while (i<s.size()){
            if (char(s[i])==' ' && word.empty()){i++;continue;} //multiple spaces
            if (char(s[i])==' ' && !word.empty()){ //first space after a word
                res = word+" "+ res; //store the word
                word=""; //reset the word
                i++; continue;
            }
            if (char(s[i])!=' '){word=word+char(s[i]);i++; continue;} //non-space chars 
        }
         
        if (!word.empty()){ //last word
            s = word+" "+res;
        }else{
            s = res;
        }
        s = s.substr(0,s.size()-1); //eliminate the last space
    }
};

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

## Sort List

**20.4%**

*2013-11-16*

[url](https://oj.leetcode.com/problems/sort-list/submissions/)

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

## Max Points on a Line

**10.8%**

*2013-11-22*

[url](https://oj.leetcode.com/problems/max-points-on-a-line/submissions/)

`java`

```

/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
class Solution {
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

