def solution(genres, plays):
    genre_play_count = {}  # 장르별 총 재생 횟수 저장하는 해시 맵
    genre_songs = {}      # 장르별 노래 정보 저장하는 해시 맵

    # 장르별 총 재생 횟수와 노래 정보 초기화
    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]

        # 만약 장르가 해시 맵에 없다면 새로 추가 
        if genre not in genre_play_count:
            genre_play_count[genre] = 0
            genre_songs[genre] = []

        # 장르별 총 재생 횟수와 노래 정보 갱신
        genre_play_count[genre] += play_count
        genre_songs[genre].append((i, play_count))

    # 장르별 총 재생 횟수를 기준으로 내림차순 정렬
    sorted_genres = sorted(genre_play_count.keys(), key=lambda x: genre_play_count[x], reverse=True)

    answer = []

    # 장르별로 최대 두 개의 노래를 선택하여 결과 리스트에 추가
    for genre in sorted_genres:
        songs = genre_songs[genre]
        songs.sort(key=lambda x: (-x[1], x[0]))  # 재생 횟수 내림차순, 고유 번호 오름차순 정렬
        answer.extend([song[0] for song in songs[:2]])

    return answer
