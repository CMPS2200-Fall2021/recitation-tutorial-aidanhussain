def sum_of_squares(a):
    sum = 0
    for x in a:
        sum += x**2
        
    return sum

def test_one():
    assert sum_of_squares([1,2,3]) == 14
    
test_one()