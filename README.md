# DAG Versioning Example (Airflow 3.x)

Airflow 3.x에서 새롭게 도입된 **DAG Versioning** 기능을 실습하기 위한 예제입니다.  
`LocalDagBundle`과 `GitDagBundle`을 통해 DAG 버전 관리 방식을 비교해볼 수 있습니다.

> 자세한 설명과 실습 과정은 [Apache Airflow DAG Versioning 기능 알아보기](https://discourse.airflow-kr.org/t/apache-airflow-dag-versioning/355?u=choo121600)에서 확인하실 수 있습니다.


## 주요 내용

- Airflow 3.x의 DAG Versioning 기능 실습
- DAG 실행 시점의 코드 버전 추적
- `LocalDagBundle` vs `GitDagBundle` 비교
- GitDagBundle 기반 DAG 버전 고정 및 재실행 실습


## 실행 방법
1. 프로젝트 Fork & Clone
2. Astro CLI 설치 혹은 설치 되어있다면 버전 확인
3. astro dev start 명령어로 Airflow 실행
4. `.env_example` 파일을 참고하여 env 파일로 설정


## Airflow 한국 사용자 모임
- 포럼: [https://discourse.airflow-kr.org](https://discourse.airflow-kr.org)
- 오픈카카오톡: [https://open.kakao.com/o/gM4hR8Pg](https://open.kakao.com/o/gM4hR8Pg)
- meetup: [https://www.meetup.com/korea-apache-airflow-user-group](https://www.meetup.com/korea-apache-airflow-user-group)
