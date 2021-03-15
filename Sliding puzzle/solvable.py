# If a sliding puzzle is generated at random, this may be unsolvable.
# The solvable function will determine the sliding puzzle's solvability.
# Ref. Wm. Woolsey Johnson, & Story, W. (1879). Notes on the "15" Puzzle. American Journal of Mathematics, 2(4), 397-404. doi:10.2307/2369492

def inver(): # determine the inversion of the list.
    for i in reversed(range(0, n)):
        pairs_of_invers = bisect.bisect_left(tem_list, l[i])
        inversion += pairs_of_invers
        tem_list.insert(pairs_of_invers, l[i])
    return inversion
  
def solvable(inversions):
    if n%2 == 1 and inver()%2 != 0:
        return True       
    elif n%2 == 0:
        row_and_col = num_list.index(0)
        if (row_and_column//n) %2 == 1 and inversion() % 2 != 0:
            return True
        elif (row_and_column//n) %2 == 0 and inversion() % 2 == 0:
            return True
    else:
        return False
