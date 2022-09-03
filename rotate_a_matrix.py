# 시계 방향 90도 회전 함수
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행
    m = len(a[0])  # 열
    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result
