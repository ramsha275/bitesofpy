def rotate(string, n):
    '''Write a function that rotates characters in a string, in both directions:

        - if n is positive move characters from beginning to end, 
          e.g.: rotate('hello', 2) would return llohe
        - if n is negative move characters to the start of the string,
          e.g.: rotate('hello', -2) would return lohel '''
          
    return string[n:]+string[:n]