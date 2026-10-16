class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First go through the board vertically and horizontally
        for i in range(0,9):
            horizontal_total_nums = set()
            vertical_total_nums = set()
            for j in range(0,9):
                current_num = board[i][j]
                if(current_num != "."):
                    prev_size = len(horizontal_total_nums)
                    horizontal_total_nums.add(current_num)
                    if prev_size == len(horizontal_total_nums):
                        print(f"Duplicate at i = {i} and j = {j}")
                        return False
                
                current_num = board[j][i]
                if(current_num != "."):
                    prev_size = len(vertical_total_nums)
                    vertical_total_nums.add(current_num)
                    if prev_size == len(vertical_total_nums):
                        print(f"Duplicate at i = {j} and j = {i}")
                        return False

        # Now check through the 9 boxes at a time
        start_nums = [0,3,6]
        second_start_nums = [0,3,6]
        for i in start_nums:
            for j in second_start_nums:
                total_nums = set()
                for k in range(0,3):
                    for l in range(0,3):
                        current_num = board[i+k][j+l]
                        print(f"Checking Box i = {i+k}, j = {j+l}.")
                        if(current_num != "."):
                            prev_size = len(total_nums)
                            total_nums.add(current_num)
                            if prev_size == len(total_nums):
                                print(f"Duplicate at i = {i+k} and j = {j+l}")
                                return False
            second_start_nums.pop(0)

        return True
                        
                
