# AI Growth

AI 개발자/엔지니어 역량 강화를 위한 학습 및 실습 저장소입니다.

## Structure

- `python/` — Python 문법 및 언어 기본 실습
- `data-analysis/` — 데이터 처리·분석 및 기초 통계
  - `preprocessing/` — 결측치·중복·자료형·이상치 처리, 스케일링·인코딩
  - `exploration/` — 데이터 요약, 분포·관계 탐색 및 시각화
  - `statistics/` — 기술통계, 확률·분포, 추정·가설검정 기초
- `pytorch/` — PyTorch 학습 및 실습
- `algorithms/` — 알고리즘 및 코딩테스트
- `projects/` — AI/데이터/서비스 개인 프로젝트
- `learning-log/` — 학습 기록 및 회고

## 학습 파일 분류

실습의 핵심 주제를 기준으로 저장합니다. Pandas를 사용하더라도 결측치·중복 처리가 목적이면 `data-analysis/preprocessing/`에 둡니다. 여러 주제를 통합하는 실전 프로젝트는 `projects/`에 둡니다.

학습 코드의 기본 형식은 Jupyter Notebook(`.ipynb`)입니다. 파일명은 `001_missing_values_duplicates.ipynb`처럼 주제가 드러나게 붙이며, 번호는 각 하위 폴더 안의 정리 순서입니다. 데이터 파일은 해당 실습 옆의 `data/`에 필요할 때 추가합니다. 큰 데이터는 출처·다운로드 방법을 Notebook에 기록합니다.

Notebook에는 목표, 직접 작성한 코드, 실행 결과, 전후 비교와 해석을 함께 남깁니다. 진행 기록은 `learning-log/`에서 관리합니다.

이 저장소는 학습 결과를 꾸준히 기록하고, 이후 공개 포트폴리오로 발전시키기 위한 용도로 사용합니다.
