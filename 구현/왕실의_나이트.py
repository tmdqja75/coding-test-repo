"""
행 복 왕 국 의 왕 실 정 원 은 체 스 판 과 같 은 8 x 8 좌 표 평 면 이 다 . 왕 실 정 원 의 특 정 한 한 칸 에 나 이 트
가 서 있 다 . 나 이 트 는 매 우 충 성 스 러 운 신 하 로 서 매 일 무 술 을 연 마 한 다 .
나 이 트 는 말 을 타 고 있 기 때 문 에 이 동 을 할 때 는 1 자 형 태 로 만 이 동 할 수 있 으 며 정 원 밖 으 로 는 나
갈 수 없 다 . 나 이 트 는 특 정 한 위 치 에 서 다 음 과 같 은 2 가 지 경 우 로 이 동 할 수 있 다 .
1 . 수 평 으 로 두 칸 이 동 한 뒤 에 수 직 으 로 한 칸 이 동 하 기
2 . 수 직 으 로 두 칸 이 동 한 뒤 에 수 평 으 로 한 칸 이 동 하 기

이 처 럼 8 x 8 좌 표 평 면 상 에 서 나 이 트 의 위 치 가 주 어 졌 을 때 나 이 트 가 이 동 할 수 있 는 경 우 의 수 를
출 력 하 는 프 로 그 램 을 작 성 하 시 오 . 이 때 왕 실 의 정 원 에 서 행 위 치 를 표 현 할 때 는 1 부 터 8 로 표 현 하
며 , 열 위 치 를 표 현 할 때 는 a 부 터 h 로 표 현 한 다 .
예 를 들 어 만 약 나 이 트 가 a 1 에 있 을 때 이 동 할 수 있 는 경 우 의 수 는 다 음 2 가 지 이 다 . a 1 의 위 치 는
좌 표 평 면 에 서 구 석 의 위 치 에 해 당 하 며 나 이 트 는 정 원 의 밖 으 로 는 나 갈 수 없 기 때 문 이 다 .
1 . 오 른 쪽 으 로 두 칸 이 동 후 아 래 로 한 칸 이 동 하 기 ( c 2 )
2 . 아 래 로 두 칸 이 동 후 오 른 쪽 으 로 한 칸 이 동 하 기 ( b 3 )

첫 째 줄 에 나 이 트 가 이 동 할 수 있 는 경 우 의 수 를 출 력 하 시 오 .
"""

def get_num_possible_move(position):
    pos_x, pos_y = position[0], position[1]
    
    pos_x = ord(pos_x)-97
    pos_y = int(pos_y)-1

    final_move_count = 0

    movement = [(2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1), (-2, -1), (1, 2), (-1, 2)]
    for move in movement:
        pos_x_move = pos_x + move[0]
        pos_y_move = pos_y + move[1]
        if (pos_x_move>=0 and pos_x_move<=7) and (pos_y_move>=0 and pos_y_move<=7):
            final_move_count += 1
    return final_move_count


while True:
    pos = input('Enter position: ')
    print(get_num_possible_move(pos))
