class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # NOTE: need to check that period represents empty square

        for i in range(9):
            valid = set()
            for j in range(9):
                if board[i][j] not in valid:
                    if board[i][j] != ".":
                        valid.add(board[i][j])
                else: 
                    return False
        for j in range(9):
            valid = set()
            for i in range(9):
                if board[i][j] not in valid:
                    if board[i][j] != ".":
                        valid.add(board[i][j])
                else: 
                    return False
        
        valid = [[set() for i in range(3)] for j in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] not in valid[i // 3][j // 3]:
                    if board[i][j] != ".":
                        valid[i // 3][j // 3].add(board[i][j])
                else:
                    return False
        return True