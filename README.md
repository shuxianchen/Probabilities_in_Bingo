# Probabilities in Bingo
Script to calculate the expected number of calls for bingo win and stimulate the probability distribution of the number of calls for bingo win. 

The bingo card is represented by an array of integer. This model stimulates the bingo card having 25 squares, arranged in 5 columns of 5 squares. The middle square is labeled "free". The goal is to have a complete row, column, or diagonal of 5 called off first. 

For the ease of simulation, each integer represents **when** a specific cell will be called by host (caller). 

For example, here is sample Bingo Card

|  B   |  I   |  N   |  G   |  O   |
| :--: | :--: | :--: | :--: | :--: |
|  45  |  37  |  27  |  69  |  28  |
|  39  |  14  |  8   |  50  |  34  |
|  56  |  47  | Free |  1   |  63  |
|  64  |  43  |  4   |  75  |  23  |
|  16  |  66  |  35  |  10  |  30  |

It tells you

- the 3rd row in column G is the 1st number called by the host;
- the 2nd & 3rd numbers called by the host are not on the card (indicated by the absence of 2 and 3);
- the 4th numbers called is right beneath the Free cell, etc.

The data representation of this sample Bingo Card is a list:

```python
[45,37,27,69,28,39,14,8,50,34,56,47,1,63,64,43,4,75,23,16,66,35,10,30]
```


Note that the Free cell doesn't take up a space in the data representation.
