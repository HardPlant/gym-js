Feature: 게임

   한 턴이 지날 때마다 랜덤으로 움직이고 랜덤으로 공격한다.

    Scenario: 초기화
        Given "3" * "3" 게임판이 초기화된다
        Given "아군"이 "0", "0" 위치에 배치된다
        Given 아군은 x:1로 움직인다
        Given "적군"이 "0", "1" 위치에 배치된다
        Given 적군은 y:-1 움직인다

    Scenario: 이동
        When 턴이 진행되면
        Then "아군"이 "1", "0" 위치에 있다
        Then "적군"이 "0", "0" 위치에 있다
        Then "2" 턴이 경과한다

    Scenario: 이동
        When 턴이 진행되면
        Then "아군"이 "2", "0" 위치에 있다
        Then "적군"이 "0", "0" 위치에 있다
        Then "4" 턴이 경과한다

    Scenario: 충돌
        When 턴이 진행되면
        Then "아군"이 "2", "0" 위치에 있다
        Then "적군"이 "0", "0" 위치에 있다
        Then "6" 턴이 경과한다
