board1 = [0,1,4,23,18,14,15,13,1,0]
board2 = [0,1,92384,23,45,53,6,35,31,6345,12,8,1,0]
board3 = [0,1,4,14,15,1.4, 2314.4, 3,1,0]
board4 = [0,1,2,3,4,6,7,6,5,4,3,1,0]

def relmax(board):
    start = 0
    end = len(board) - 1

    while start != end:
        
        midl = board[(start + end) // 2 - 1]
        mid = board[(start + end) // 2]
        midr = board[(start + end) // 2 + 1]

        if mid > midl and mid > midr:
            print("rel max found at index " + str((start + end) // 2))
            return mid
        elif midl > mid and mid > midr:
            end = (start + end) // 2 - 1
        else:
            start = (start + end) // 2 + 1
    
    if start == end:
        print("rel max found at index " + str(start))
        return board[start]

print(relmax(board1))
print(relmax(board2))
print(relmax(board3))
print(relmax(board4))

