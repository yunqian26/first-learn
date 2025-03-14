import numpy as np
if __name__ == '__main__':
    a=np.array(([4,2,3],[4,5,6],[7,8,0]))
    b=np.array(([9,9,3]))
    c=np.array(([1,1,1],[2,2,2],[1,1,50]))
    cc=np.tile(c,(2,2))
    print(cc)