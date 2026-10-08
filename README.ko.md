<p align="center">
  <img src="assets/skilloom.png" alt="Skilloom" width="480">
</p>

<h1 align="center">Skilloom</h1>

<p align="center">
  <strong>에이전트 스킬을 짜는 베틀.</strong><br>
  이미 끝낸 일에서 스킬을 만듭니다. 결과가 의존하는 규칙만 남기고 나머지는 지웁니다.
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="#스킬">스킬</a> ·
  <a href="#설치">설치</a> ·
  <a href="#사용">사용</a> ·
  <a href="#기여">기여</a>
</p>

<p align="center">
  <a href="https://github.com/boaz-hwang/skilloom/actions/workflows/validate.yml"><img alt="Validate" src="https://github.com/boaz-hwang/skilloom/actions/workflows/validate.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-black.svg"></a>
  <a href="https://github.com/agentskills/agentskills"><img alt="Agent Skills format" src="https://img.shields.io/badge/format-Agent%20Skills-blue.svg"></a>
</p>

---

스킬은 자꾸 길어집니다. 문제를 하나 고칠 때마다 문장이 길어지고 예외를 만날 때마다 규칙이 추가됩니다. 어느새 유능한 모델이 알아서 잘할 수 있는 일인데도 지침에 갇혀 제대로 능력을 발휘하지 못합니다.

Skilloom은 이미 성공한 경험, 즉 승인한 결과물과 그때 준 피드백에서 출발해 핵심만 남깁니다. 나머지는 모델이 스스로 정합니다.

## 실제 사용 기록

공개 전에 저자가 실제로 쓰던 스킬에 이 스킬들을 적용했습니다. 아래 숫자는 git 기록에서 가져왔습니다.

| 대상 스킬 | 사용한 Skilloom 스킬 | SKILL.md 줄 수 | 코드로 옮긴 것 | 요구사항 보존 |
| --- | --- | --- | --- | --- |
| 위키 관리 스킬 (6개를 5개로 통합) | distill, refine, consolidate | 229 -> 128, 새 참조 파일 2개에 27줄 추가 | 클리핑 폴더 접근 오류를 0건으로 세지 않고 실패로 처리. 검토 조사 기록을 검사하는 스크립트 추가(필수 원천, 항목별 기존 위키 대조). 테스트 12개 추가. | 대부분. 3개는 빠짐(아래). |
| 회의록을 대시보드로 정리하는 스킬 | distill, 이후 evolve | 신규 69줄, 검사 스크립트 79줄. evolve 후 69 -> 70, 되돌려 69 | 처음부터 보고서 내용 검사를 스크립트로 둠 | 전부. evolve 변경 대부분은 되돌림(아래 참고). |

지운 줄이 모두 옮겨진 것은 아닙니다. 위키 스킬에서 지운 내용은 대부분 공통 검토 참조, 새 참조 파일 2개, 코드 검사로 갔습니다. 다만 세 가지는 더 이상 적혀 있지 않습니다. update 스킬의 구분 목록이 줄면서 "제안과 계약", "교육용 설계와 현재 운영 규칙" 구분이 빠졌습니다. lint 스킬은 아직 연결하지 않은 원문 경로가 실제로 있는지 확인하지 않습니다. ingest 보고에서 새 원문이 기존 주장을 어떻게 바꿨는지 밝히는 항목이 빠졌습니다. 클리핑 1회 10건 상한과 고정 개수(핵심 주장 3~5개, 3~8페이지)는 의도적으로 없앴습니다.

회의록 스킬은 이후 사용 기록을 보고 evolve로 규칙을 더했습니다. 독자에게 필요한 결론과 판단 사항을 먼저 두고, 확정되지 않은 구조는 도표에서도 초안으로 표시하고, 반복 환각이 여러 구간에 걸치면 더 정확한 모델로 전체를 다시 전사하게 했습니다. 새 버전은 자체 비교 실행에서 이겼습니다. 그런데 결과물이 이미 승인한 보고서 형식에서 벗어나 있어 앞의 두 규칙은 8분 뒤 되돌렸고, 재전사 규칙만 남았습니다. 비교 기준이 승인한 결과물이 아니라 같은 세션의 피드백이었기 때문입니다.

## 스킬

스킬을 만들고 쓰는 단계마다 하나씩, 네 개입니다. 각각 따로 설치하고 따로 씁니다.

| 스킬 | | 이럴 때 |
| --- | --- | --- |
| [**distill**](skills/distill/README.ko.md) | 잣다 | 방금 끝내고 승인한 작업을 재사용 가능한 스킬로 만든다. |
| [**refine**](skills/refine/README.ko.md) | 조이다 | 장황한 스킬 하나를 목적 중심으로 재구성한다. |
| [**evolve**](skills/evolve/README.ko.md) | 깁다 | 실제 사용에서 드러난 문제를 근거가 있는 최소 변경으로 고친다. |
| [**consolidate**](skills/consolidate/README.ko.md) | 잇다 | 겹치는 스킬을 합친다. 잘 되던 기능은 그대로 둔다. |

넷이 공통으로 지키는 것이 있습니다.

- 지침을 더하기 전에 지울 것부터 봅니다.
- 코드가 검증할 수 있는 항목은 코드가 검사합니다. 나머지는 짧은 질문 목록을 받아 사람이 판단합니다. 예를 들어 표의 숫자가 맞는지는 코드가, 문장이 읽기 좋은지는 사람이 봅니다.
- 파일이 짧아졌다고 개선이라 부르지 않습니다. 이전 버전과 비교한 뒤에야 개선입니다.
- 바꿀 게 없으면 그대로 두고 이유만 남깁니다.

## 설치

코딩 에이전트에 아래를 붙여넣으세요.

```text
https://github.com/boaz-hwang/skilloom 을 git clone해서 skills/ 안의 네 폴더를 각각 별도 스킬로 스킬 디렉터리에 설치해줘.
```

스킬은 [Agent Skills](https://github.com/agentskills/agentskills) 형식을 따릅니다. `SKILL.md`를 읽는 클라이언트라면 어디서든 동작합니다.

예전 버전에서 저장소 루트로 distill을 설치했다면 `skills/distill`에서 다시 설치하세요.

## 사용

지금 상황에 맞는 스킬을 부르세요. 각 스킬 README에 복사할 수 있는 요청문이 있습니다.

```text
distill로 이 작업을 재사용 가능한 스킬로 만들어줘.
```

```text
refine으로 <스킬명>을 목적과 필수 요구사항 중심으로 재구성해줘.
```

```text
evolve로 <스킬명>의 실행 기록을 검토하고 근거가 있는 부분만 최소한으로 개선해줘.
```

```text
consolidate로 <스킬 폴더>를 검토해서 합칠 만한 것을 제안하고, 내가 계획을 확인하면 통합해줘.
```

추천 모델:

- Fable 5.1
- Astra 6

## 기여

검증기와 테스트는 구조와 Python 문법만 확인합니다. 결과 품질은 `evals/`의 시나리오로 직접 돌려 봅니다.

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_skill.py skills/distill
python -m unittest discover -s tests -v
```

CI는 push와 pull request마다 같은 검사를 실행합니다. 스킬을 더 짧게 만드는 변경을 환영합니다. 요구사항은 잃지 않아야 하며 근거도 함께 가져와 주세요.

## 라이선스

[MIT](LICENSE)
