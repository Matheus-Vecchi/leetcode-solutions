# ======================================
# LeetCode Problem: spiral matrix
# Language: python3
# Link: https://leetcode.com/problems/spiral-matrix/
# Synced by: LinkCode
# Date: 20/08/2026, 17:14:37
# ======================================


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # direita = m - 1
        # baixo = n - 1
        # esquerda = m - 1
        # cima = n - 2
        # direita = m - 2
        # baixo = n - 3
        # esquerda = m - 3

        ans = []

        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = -1      
        direcao = "direita"
        passos = len(matrix[0])

        while len(ans) < len(matrix) * len(matrix[0]):
            print(ans, direcao, passos)
            if direcao == "direita":
                for _ in range(passos):
                    j += 1
                    ans.append(matrix[i][j])
                n -= 1
                direcao = "baixo"
                passos = n
            elif direcao == "baixo":
                for _ in range(passos):
                    i += 1
                    ans.append(matrix[i][j])
                m -= 1
                direcao = "esquerda"
                passos = m
            elif direcao == "esquerda":
                for _ in range(passos):
                    j -= 1
                    ans.append(matrix[i][j])
                n -= 1
                direcao = "cima"
                passos = n
            else:
                for _ in range(passos):
                    i -= 1
                    ans.append(matrix[i][j])
                m -= 1
                direcao = "direita"
                passos = m

        return ans
