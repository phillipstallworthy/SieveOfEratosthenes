# Sieve of Eratosthenes - Psuedo Code

Categorise a list of number as prime, or not. 

## Attempt 1 - Nieve - unoptomised - but hopefully working.

### Data Structure
Simple array (list?), the index is the number to be tested, and the value is either 1=true=prime, or 0=false=not prime.

`Index | Value`  
`0  | 0`    
`1  | 0`  
`2  | 0`  
`3  | 1`  
`4  | 0`  
`5  | 1`  

Initialise the list - all are u (unknown)

    limit = 200
    array data = int array [limit] with 0,0,u,u,u......

    Iterator x = 1 
        while x <= limit / 2 // iterate through all the numbers
            x = next uknown number x list.index(0,x) - what does it return if there are none?
            
             
            data [x] = 1 //first one is prime

            for y from x + x to limit increment x  
                data[y] = 0    
        end
