Feature: 게임

   한 턴이 지날 때마다 랜덤으로 움직이고 랜덤으로 공격한다.

    Scenario: 초기화
        Given "2" * "2" 게임판이 초기화된다
        Given "아군"이 "0", "0" 위치에 배치된다
        Given "아군"은 랜덤하게 움직인다
        Given "적군"이 "1", "1" 위치에 배치된다
        Given "적군"은 랜덤하게 움직인다
        When 턴이 진행되면
        Then "아군"이 "0", "0" 위치에 없다
        Then "적군"이 "1", "1" 위치에 없다


    Scenario: 1턴 경과

    Scenario: 2턴 경과

    Scenario: 게임 종료 때까지