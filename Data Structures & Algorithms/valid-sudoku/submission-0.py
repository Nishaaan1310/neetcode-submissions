class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[set() for _ in range (9)]
        column=[set() for _ in range (9)]
        box=[set() for _ in range (9)]
        
        for r in range(9):
            for c in range(9):
                number=board[r][c]
                if number==".":
                    continue
                box_number= (r//3)*3 + (c//3)
                if number in row[r] or number in column[c] or number in box[box_number]:
                    return False
                else:
                    row[r].add(number)
                    column[c].add(number)
                    box[box_number].add(number)

        return True
                