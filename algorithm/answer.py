# answer.py
def looknsay(num: str) -> str:
    i, j = 0, 0
    result = ""
    while i < len(num) and j < len(num):
        if num[i] == num[j]:
            j += 1
        else:
            result = result + f"{j-i}" + num[i]
            i = j
    if j == len(num):
        result = result + f"{j-i}" + num[i]
    return result

def solution(n: int) -> int:
    """
    Look and say sequence calculation program
    - 첫번째 항은 1이다.
    - 이전 항의 이웃한 같은 숫자들을 묶고,
    - 묶인 숫자들의 숫자와 개수를 붙여쓴다.
    (예시) 1 -> (1, 1) -> 11

    Args:
        n (int): 계산할 개미 수열의 n번째 항을 의미한다.

    Returns:
        int: n번째 항 개미 수열의 가운데 두자리 수
    """
    answer = "1"
    cnt_loop = 1
    if n == 1:
        return 1
    while cnt_loop < n:
        answer = looknsay(answer)
        cnt_loop += 1
    mid = len(answer)//2-1
    return int(answer[mid:mid+2])

if __name__ == "__main__":
    n = int(input("개미 수열의 몇번째 항을 계산할지 입력해주세요: "))
    print("Answer: ", solution(n))