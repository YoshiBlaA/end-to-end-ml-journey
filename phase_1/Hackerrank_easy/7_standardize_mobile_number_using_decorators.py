#https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true

def wrapper(f):
    def fun(l):
        formatted_numbers = [f'+91 {number[-10:-5]} {number[-5:]}' for number in l]           
        f(formatted_numbers)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 