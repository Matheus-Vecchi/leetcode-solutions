# ======================================
# LeetCode Problem: valid sudoku
# Language: python3
# Link: https://leetcode.com/problems/valid-sudoku/
# Synced by: LinkCode
# Date: 16/05/2026, 01:30:46
# ======================================


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        grids = {}

        for row in range(len(board)):
            for col in range(len(board[row])):
                curr = board[row][col]
                if curr.isdigit() == False:
                    continue

                grid = (row // 3, col // 3)
                
                if row in rows:
                    if curr in rows[row]:
                        return False
                    rows[row].append(curr)
                else:
                    rows[row] = [curr]
                if col in cols:
                    if curr in cols[col]:
                        return False
                    cols[col].append(curr)
                else:
                    cols[col] = [curr]
                if grid in grids:
                    if curr in grids[grid]:
                        return False
                    grids[grid].append(curr)
                else:
                    grids[grid] = [curr]
        
        return True


                
