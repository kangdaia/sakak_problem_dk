# answer.py
import time
from collections import deque


def solution_new(n: int) -> int:
    """deque를 사용해 개미 수열을 구한 방법
    1. 두개의 큐를 사용, 하나는 개미 수열을 한 숫자씩 담고있고,
        다른 하나는 수열의 수가 이어져 반복되는 횟수를 담고 있다.
    2. stage 변수를 사용해 개미 수열이 갱신되는 횟수를 기록한다.
    3. 수열이 빌때까지, 왼쪽의 값을 pop하면서,
        - 해당 수가 count 큐의 마지막 값과 동일하면, count 큐의 마지막 값의 횟수를 +1
        - 아니면 count 큐에 새롭게 값을 넣는다.
    4. 수열이 비게 되면, 개미 수열을 갱신한다고 가정하고,
        - count 큐에 있는 모든 값들을 횟수와 해당 수 순서로 수열에 넣는다.
        - 갱신 횟수를 +1 한다.
    5. n 번째에 도달할 때 까지 반복한다.

    Args:
        n (int): 계산할 개미 수열의 n번째 항을 의미한다.

    Returns:
        int: n번째 항 개미 수열의 가운데 두자리 수
    """
    sequence = deque()  # 수열의 숫자들을 순서대로 담고 있음
    sequence.append(1)
    count = deque()  # 수열의 이웃한 같은 수를 구하는 큐
    stage = 1
    while True:
        if stage == n:
            break  # n번째 항까지만 반복 후 멈춤
        num = sequence.popleft()
        if count and count[-1][0] == num:  # 이전에 본 수가 지금 수랑 같으면 개수를 업데이트
            target, cnt = count.pop()
            count.append([target, cnt + 1])
        else:
            count.append([num, 1])  # 새로운 수
        if not sequence:  # 해당 항의 모든 수를 보았음
            while count:  # 이웃한 수의 같은 수를 구한 큐로 새로운 수열을 만듬
                target, cnt = count.popleft()
                sequence.append(cnt)
                sequence.append(target)
            stage += 1  # 다음 항으로 넘어감
    mid = len(sequence) // 2 - 1
    return int(f"{sequence[mid]}{sequence[mid+1]}")


def solution_old(n: int) -> int:
    """포인터를 사용해 전체 모든 값을 비교하는 방식
    ** 대략 45번째부터 계산 속도가 매우 느려진다.
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
    num = "1"
    cnt_loop = 1
    result = ""
    while cnt_loop < n:
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
        num = result
        result = ""
        cnt_loop += 1
    mid = len(num) // 2 - 1
    return int(num[mid : mid + 2])


def main(n: int) -> int:
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
    start = time.time()
    if n == 1:  # base
        answer = 1
    else:
        answer = solution_new(n)
        # answer = solution_old(n)
    print(f"실행시간: {time.time() - start:.4f}")
    return answer


if __name__ == "__main__":
    n = int(input("개미 수열의 몇번째 항을 계산할지 입력해주세요: "))
    print("Answer: ", main(n))
