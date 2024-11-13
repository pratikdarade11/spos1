//Assignment No.  : 4



//1.First in first out


import java.io.*;
class FIFO
{

        public static void main(String args[]) throws IOException
        {
                
                int n;
                int f;

                float rat;
                BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
                System.out.println("Enter the number of FRAMES :");
                f=Integer.parseInt(br.readLine());
                int fifo[]=new int[f];
                System.out.println("Enter the number of INPUTS :");
                n=Integer.parseInt(br.readLine());
                int inp[]=new int[n];
                System.out.println("Enter INPUT:");
                for(int i=0;i<n;i++)
                inp[i]=Integer.parseInt(br.readLine());
                System.out.println("----------------------");
                for(int i=0;i<f;i++)
                        fifo[i]=-1;
                int Hit=0;
                int Fault=0;
                int j=0;
                boolean check;
                for(int i=0;i<n;i++)
                {
                        check=false;


                                for(int k=0;k<f;k++)
                                if(fifo[k]==inp[i])
                                {
                                        check=true;
                                        Hit=Hit+1;
                                }
                                if(check==false)
                                {
                                        fifo[j]=inp[i];
                                        j++;
                                        if(j>=f)
                                        j=0;
                                        Fault=Fault+1;
                                }

                }
                rat = (float)Hit/(float)n;
                System.out.println("HIT:"+Hit+"  FAULT:"+Fault+"   HIT RATIO:"+rat);
        }
}


/* output


First In First Out (FIFO) page replacement algorithm Output:
run:
Enter the number of FRAMES :
3
Enter the number of INPUTS :
12
Enter INPUT:
1
2
3
4
1
2
5
1
2
3
4
5
----------------------
HIT:3  FAULT:9   HIT RATIO:0.25


*/


//2.optimal page replacement


import java.io.*;
import java.util.*;
 
class GFG {
 
    // Function to check whether a page exists
    // in a frame or not
    static boolean search(int key, int[] fr)
    {
        for (int i = 0; i < fr.length; i++)
            if (fr[i] == key)
                return true;
        return false;
    }
 
    // Function to find the frame that will not be used
    // recently in future after given index in pg[0..pn-1]

    static int predict(int pg[], int[] fr, int pn,
                       int index)
    {
        // Store the index of pages which are going
        // to be used recently in future
        int res = -1, farthest = index;
        for (int i = 0; i < fr.length; i++) {
            int j;
            for (j = index; j < pn; j++) {
                if (fr[i] == pg[j]) {
                    if (j > farthest) {
                        farthest = j;
                        res = i;
                    }
                    break;
                }
            }
 
            // If a page is never referenced in future,
            // return it.
            if (j == pn)
                return i;
        }
 
        // If all of the frames were not in future,
        // return any of them, we return 0. Otherwise
        // we return res.
        return (res == -1) ? 0 : res;
    }
 
    static void optimalPage(int pg[], int pn, int fn)
    {
        // Create an array for given number of
        // frames and initialize it as empty.
        int[] fr = new int[fn];
 
        // Traverse through page reference array
        // and check for miss and hit.
        int hit = 0;
        int index = 0;
        for (int i = 0; i < pn; i++) {
 
            // Page found in a frame : HIT
            if (search(pg[i], fr)) {
                hit++;
                continue;
            }
 
            // Page not found in a frame : MISS
 
            // If there is space available in frames.
            if (index < fn)
                fr[index++] = pg[i];
 
            // Find the page to be replaced.
            else {
                int j = predict(pg, fr, pn, i + 1);
                fr[j] = pg[i];
            }
        }
        System.out.println("No. of hits = " + hit);
        System.out.println("No. of misses = " + (pn - hit));
    }
 
    // driver function
    public static void main(String[] args)
    {
 
        int pg[]
            = { 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2 };
        int pn = pg.length;
        int fn = 4;
        optimalPage(pg, pn, fn);
    }
}



/* output

No. of hits = 7
No. of misses = 6


*/




//3 . least recently used


import java.util.HashSet; 
import java.util.LinkedList; 
import java.util.Queue; 
  
  
class Test 
{ 
    
    static int pageFaults(int pages[], int n, int capacity) 
    { 
      
        HashSet<Integer> s = new HashSet<>(capacity); 
       
   
        Queue<Integer> indexes = new LinkedList<>() ; 
       
       
        int page_faults = 0; 
        for (int i=0; i<n; i++) 
        { 
        
            if (s.size() < capacity) 
            { 
              
                if (!s.contains(pages[i])) 
                { 
                    s.add(pages[i]); 
        
                    page_faults++; 
       
              
                    indexes.add(pages[i]); 
                } 
            } 
       
           
            else
            { 
                
                if (!s.contains(pages[i])) 
                { 
                   
                    int val = indexes.peek(); 
       
                    indexes.poll(); 
       
                  
                    s.remove(val); 
       
                 
                    s.add(pages[i]); 
       
                
                    indexes.add(pages[i]); 
       
                 
                    page_faults++; 
                } 
            } 
        } 
       
        return page_faults; 
    } 
      
    /
    public static void main(String args[]) 
    { 
        int pages[] = {7, 0, 1, 2, 0, 3, 0, 4, 
                        2, 3, 0, 3, 2}; 
   
        int capacity = 4; 
         System.out.print("no of page faults=");
        System.out.println(pageFaults(pages, pages.length, capacity));
       
        
    } 
}

/* output

no of page faults=7



*/



