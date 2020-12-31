# Implement_Algorithm

구현 알고리즘과 배열 

### 파이썬에서 2차원 배열 (리스트)

1. 2차원 배열 입력 받기

    1) 행렬의 크기 입력 받기 
        ```
        m,n = map(int,input().split())
        ```
    2) 행렬 입력 받기 
        ```
        map_list=[0 for _ in range(m)]
        for i in range(m):
            map_list[i]=list(map(int, input().split()))
        ```
2. 2차원 배열 초기화 

    N X M 크기의 2차원 리스트 초기화 ( 리스트 컴프리핸션 사용 )
    
    ```
    array = [[0] * m for _ in range(n)] 
    ```

    ```
    look_lists= [[0 for col in range(4)] for row in range(4)]
    ```
   
        
### 파이썬에서 3차원 배열 (리스트)

1. 파이썬에서 3차원 배열 입력 받기

    ```
    go_list = [[[0 for col in range(m)] for row in range(n)] for depth in range(4)]
    ```

