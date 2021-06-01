import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import Counter
import fitter
import math
"""
A Bingo Card is represented by an array of integer.
For the ease of simulation, each integer represents when a specific cell will be called by host (caller). 

For example, here is sample Bingo Card
| B  | I  |  N   | G  | O  |
|----|----|------|----|----|
| 45 | 37 | 27   | 69 | 28 |
| 39 | 14 | 8    | 50 | 34 |
| 56 | 47 | Free |  1 | 63 |
| 64 | 43 | 4    | 75 | 23 |
| 16 | 66 | 35   | 10 | 30 |
It tells you the 3rd row in column G is the 1st number called by the host.
The 2nd & 3rd numbers called by the host are not on the card (indicated by the absence of 2 and 3).
The 4th numbers called is right beneath the Free cell, etc.

The data representation of this sample Bingo Card is
[45,37,27,69,28,39,14,8,50,34,56,47,1,63,64,43,4,75,23,16,66,35,10,30].
Note that the Free cell doesn't take up a space in the data representation.

"""


# Bingo card is represented in np array and each number represent when the number will be called
def generate_bingo(maxNum):
    """
    Generate a Bingo card

    :param maxNum:
    :type maxNum: int
    :return: a Bingo Card, represented as a np array
    :rtype: np.ndarray
    """
    bingo = np.arange(maxNum) + 1
    # randomly shuffle the bingo
    np.random.shuffle(bingo)
    return bingo


"""
A Line Definition is a set of cells that, when all are called, creates a winning Bingo Card.
For example, in a standard 5 X 5 bingo card, a Line Definition can be a row, a column, or a diagonal. 
Each integer in the Line Definition tells where the cell is located. 
For example, the following Bingo Card show the indices of each cell in a numpy array:
| B  | I  |  N   | G  | O  |
|----|----|------|----|----|
|  0 |  1 | 2    |  3 |  4 |
|  5 |  6 | 7    |  8 |  9 |
| 10 | 11 | Free | 12 | 13 |
| 14 | 15 | 16   | 17 | 18 |
| 19 | 20 | 21   | 22 | 23 |
Then,
- the Line Definition of the 1st row is [0,1,2,3,4]; 
- the Line Definition of the column B is [0,5,10,14,19];
- the Line Definition of the top-left to bottom-right diagonal is [0,6,17,23];
- etc.

A Line of a Bingo Card given a Line Definition is all the cells in the row/column/diagonal,
 defined by the Line Definition.

A Line Score of a Line is when all the cells in the Line are called. 
In our case, it is just the maximum number of all cells in that Line.
(Remember: when we are defining our Bingo Card, each number represents when that cell is called.)
For example, a line is [45,37,27,69,28], then the line score is 69.

A Card Score of a Bingo Card is when the Bingo Card has a bingo, 
  i.e., the first time when all cells of a line are called.
In our case, it is just the the minimum Line Score of all Lines in that Bingo Card.
"""


def get_card_score(bingo):
    """
    Find the minimum line score of a Bingo card

    :param bingo:
    :type bingo: nparray
    :return:score
    :rtype: int
    """
    row1_score = max(bingo[0:5])
    row2_score = max(bingo[5:10])
    row3_score = max(bingo[10:14])
    row4_score = max(bingo[14:19])
    row5_score = max(bingo[19:24])
    column1_score = max(bingo[[0, 5, 10, 14, 19]])
    column2_score = max(bingo[[1, 6, 11, 15, 20]])
    column3_score = max(bingo[[2, 7, 16, 21]])
    column4_score = max(bingo[[3, 8, 12, 17, 22]])
    column5_score = max(bingo[[4, 9, 13, 18, 23]])
    diagonal1_score = max(bingo[[0, 6, 17, 23]])
    diagonal2_score = max(bingo[[4, 8, 15, 19]])
    score = min(row1_score, row2_score, row3_score, row4_score, row5_score, column1_score, column2_score, column3_score,
                column4_score, column5_score, diagonal1_score, diagonal2_score)
    return score

""" Stimulate the bingo game 10000 times to estimate the mean, variance and standard deviation of the bingo card
"""
iterations: int = 10000
card_score = np.empty(iterations, dtype=int)
for i in range(iterations):
    a = generate_bingo(75)
    card_score[i] = get_card_score(a)

mean = card_score.mean()
var = card_score.var()
stdev = math.sqrt(var)
print (mean,stdev)
number_of_frames = 100
"""
f = fitter.Fitter(card_score, distributions=['possion'])
f.fit()
f.summary()

"""
def update_hist(num):

    plt.cla()
    plt.hist(card_score[:num * 100],bins=range(76))
    plt.gca().set_title('Sampling Bingo Card Score Distribution')
    plt.gca().set_ylabel('frequency')
    plt.gca().set_xlabel('value')

fig = plt.figure()
ani = animation.FuncAnimation(fig, update_hist, number_of_frames, interval=1,repeat=False)

plt.show()
# ani.save('Probability distribution of Bingo.gif')