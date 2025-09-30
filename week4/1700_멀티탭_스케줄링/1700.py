import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

# N: 멀티탭 구멍 수, K: 전기용품 총 사용 횟수
n, k = map(int, input().split())

# 전기용품 사용 순서
schedule = list(map(int, input().split()))

# 현재 멀티탭에 꽂혀있는 전기용품 (set으로 관리하면 확인이 빠름)
multitap = set()
unplugs = 0 # 플러그를 뺀 횟수

for i, appliance in enumerate(schedule):
    # Case 1: 이미 꽂혀있는 경우 -> 아무것도 안 함
    if appliance in multitap:
        continue

    # Case 2: 멀티탭에 자리가 있는 경우 -> 그냥 꽂음
    if len(multitap) < n:
        multitap.add(appliance)
        continue

    # Case 3: 멀티탭이 꽉 찬 경우 -> 하나를 빼야 함
    unplugs += 1 # 일단 하나를 빼야 하므로 카운트 증가

    unplug_candidate = 0 # 뽑을 후보
    max_future_idx = -1 # 가장 먼 미래의 인덱스

    # 현재 꽂혀있는 플러그들(multitap)을 하나씩 확인
    for plugged_app in multitap:
        # 남은 사용 순서(schedule[i+1:])에서 해당 플러그가 또 사용되는지 확인
        try:
            # 다음에 사용될 인덱스를 찾음
            future_idx = schedule[i+1:].index(plugged_app)
            # 더 나중에 사용되는 플러그를 후보로 저장
            if future_idx > max_future_idx:
                max_future_idx = future_idx
                unplug_candidate = plugged_app
        except ValueError:
            # 만약 남은 사용 순서에 없다면 (ValueError 발생),
            # 이 플러그가 최적의 교체 대상이므로 바로 결정하고 반복 종료
            unplug_candidate = plugged_app
            break

    # 결정된 후보를 멀티탭에서 제거
    multitap.remove(unplug_candidate)
    # 새로운 전기용품을 멀티탭에 추가
    multitap.add(appliance)

print(unplugs)