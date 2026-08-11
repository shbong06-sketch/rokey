CREATE TABLE missions (
    mission_id  SERIAL PRIMARY KEY,
    kind        VARCHAR(10) NOT NULL,          -- 무슨 일 (이동·픽업…)
    target      VARCHAR(20) NOT NULL,          -- 어디로 (노드의 자세표와 짝)
    priority    INT NOT NULL DEFAULT 5 CHECK (priority BETWEEN 1 AND 9),
    status      VARCHAR(10) NOT NULL DEFAULT '대기',   -- 대기→진행→완료/실패
    created_at  TIMESTAMP NOT NULL DEFAULT now(),
    started_at  TIMESTAMP,
    finished_at TIMESTAMP
);

-- 일부러 우선순위와 반대 순서로 넣는다 (아래 tip)
INSERT INTO missions (kind, target, priority) VALUES
  ('이동', '대기장소', 8),
  ('픽업', '선반A',    2),
  ('이동', '충전독',   5);
