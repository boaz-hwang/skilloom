<p align="center">
  <img src="assets/skilloom.png" alt="Skilloom" width="480">
</p>

<h1 align="center">Skilloom</h1>

<p align="center">
  <strong>승인한 결과에서, 믿고 다시 쓸 스킬로.</strong><br>
  좋은 결과를 만든 조건을 담습니다. 스킬을 정리하고, 고치고, 합친 뒤에도 그 조건이 지켜지는지 확인합니다.
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="#필요한-변경에-따라-고르세요">스킬</a> ·
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

Skilloom은 사용자가 승인한 결과물과 그 결과를 만든 피드백에서 출발합니다. 그 경험을 재사용 가능한 스킬로 만들고, 이후 스킬을 바꿀 때도 필요한 요구사항을 유지하도록 돕습니다. 짧은 지침은 의도한 결과를 계속 만들 수 있을 때 의미가 있습니다.

## 필요한 변경에 따라 고르세요

네 스킬은 각각 독립적입니다. 순서대로 실행하는 과정이 아니라, 지금 필요한 변경에 맞춰 하나를 고릅니다.

| 지금 필요한 일 | 스킬 | 변경 범위 |
| --- | --- | --- |
| 완료하고 승인한 작업을 다시 만들고 싶다 | [**distill**](skills/distill/README.ko.md) | 승인한 결과와 수정 피드백에서 새 스킬 생성 |
| 스킬 하나의 구조와 불필요한 지침을 정리하고 싶다 | [**refine**](skills/refine/README.ko.md) | 필수 요구사항을 유지하며 전체 재구성 |
| 실제 사용에서 특정 문제가 드러났다 | [**evolve**](skills/evolve/README.ko.md) | 실행 증거가 뒷받침하는 부분만 최소 수정 |
| 여러 스킬의 역할이 겹친다 | [**consolidate**](skills/consolidate/README.ko.md) | 필요한 기능을 보존하며 적합한 역할 통합 |

refine과 evolve의 차이는 로그 유무보다 **허용하는 변경 범위**입니다. refine은 전체 구조를 바꿀 수 있습니다. evolve는 관찰된 문제에 집중하고, 더 넓은 재작성은 별도 refine 작업으로 제안합니다.

네 스킬이 공통으로 지키는 원칙입니다.

- 지침을 더하기 전에 삭제를 검토합니다. 쉽게 알 수 없는 도메인 지식과 필수 예외는 남깁니다.
- 객관적인 요구사항은 코드로 검사하고, 사람이 판단해야 하는 품질은 구체적인 질문으로 확인합니다.
- 원래 요구사항을 기준으로 비교합니다. 줄 수가 줄었다고 개선은 아닙니다.
- 바꿀 근거가 없으면 기존 스킬을 유지합니다. 효과가 확인되지 않은 후보는 따로 둡니다.

## 어떤 상황에서 Skilloom을 쓰나요?

이미 `SKILL.md`를 읽는 에이전트를 쓰고 있고, 승인한 작업을 다음에도 재현하고 싶으며, 기존 스킬을 어디까지 바꿀지 구분하고 싶을 때 사용합니다. 각 스킬을 독립적으로 설치하며 별도 최적화 서비스가 필요하지 않습니다. 생성한 스킬에는 업무에 맞는 도구와 검사가 필요할 수 있습니다.

관련 프로젝트와의 차이는 작업 방식에 있습니다. 아래는 성능 우열 비교가 아니라 2026-10-08에 확인한 문서 기준의 역할 비교입니다.

| 프로젝트 | 해당 프로젝트가 강조하는 것 | Skilloom이 강조하는 것 |
| --- | --- | --- |
| [Claudeception](https://github.com/blader/Claudeception) | 세션에서 재사용할 발견을 추출하고 선택적으로 훅 사용 | 승인한 결과물과 사용자의 수정 피드백에서 추출 시작 |
| [Anthropic skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | 평가와 description 최적화를 포함한 스킬 생성·개선 | 전체 재구성, 부분 수정, 여러 스킬 통합을 별도 작업으로 구분 |
| [SkillHone](https://github.com/Tencent/SkillHone) | 회귀 검사·판단 이력·로컬 PR을 갖춘 스킬 저장소 개선 | 기존 에이전트 세션에서 네 스킬을 각각 호출 |
| [EvoSkill](https://github.com/sentient-agi/EvoSkill) | 벤치마크와 별도 검증 데이터로 스킬·프롬프트 자동 개선 | 제공한 작업·피드백에서 시작하고 변경 영향에 맞춰 검증 |
| [SkillX](https://github.com/zjunlp/SkillX) | 계층형 스킬 지식베이스 추출·필터링·병합·확장 | 지정한 스킬들을 검토하고 구체적인 통합안을 확인 |

사람 검토, 평가, 경험 추출은 다른 도구에도 있습니다. Skilloom이 제안하는 가치는 승인한 결과를 기준으로 삼고, 삭제부터 검토하며, 변경 범위를 구분하는 조합입니다. 실제 업무가 나아지는지는 해당 업무의 증거로 확인해야 합니다.

## 근거를 직접 확인하세요

**[실행 가능한 재고 보고서 예제](examples/inventory/README.ko.md)**에 기준 결과물, 요구사항, 변경 전후 지침, 새 입력, 출력 예시, diff, 검사 코드를 담았습니다. 지침 길이와 별개로 요구사항을 검사하고, 합계가 맞아도 행이 빠진 출력을 기각하는 방법을 보여줍니다. 작성된 설명용 예제이며, 에이전트 벤치마크나 실제 사용자가 승인한 업무 기록은 아닙니다.

```bash
python3 examples/inventory/check.py
```

재고 0인 행을 빠뜨린 후보를 기각하고 **기존 버전을 유지하는 판단**, 서비스 장애를 이미 올바르게 처리해 **스킬을 수정하지 않는 판단**도 함께 공개합니다. [유지가 결과가 되는 경우](examples/decisions/README.ko.md)를 참고하세요.

### 실제 유지보수 기록

저자 자신의 업무에서 나온 기록입니다. 공개 요약에는 비공개 원문과 전체 실행 기록이 없으므로 독립적으로 재현 가능한 벤치마크는 아닙니다.

| 사례 | 관찰한 결과 | 확인할 수 있는 것 |
| --- | --- | --- |
| 위키 관리: 6개를 5개로 통합, SKILL.md 229 → 128줄, 새 참조 파일 2개에 27줄 추가 | 이후 대조에서 요구사항 세 가지 누락 발견 | 짧아져도 요구사항이 빠질 수 있습니다. 축약 성공의 증명이 아닌 누락 발견 사례입니다. |
| 회의록: evolve 후보가 자체 비교에서 이겼지만 8분 뒤 변경 대부분을 되돌림 | 승인한 보고서 형식에서 벗어남. 재전사 규칙만 유지 | 비교 기준이 중요합니다. 자체 비교의 승리만으로 승인된 결과의 보존을 확인할 수 없었습니다. |

의도적으로 삭제한 내용과 미검증 범위는 [사례 상세와 한계](examples/maintenance-records.ko.md)에 정리했습니다.

직접 비교할 때는 **평가 전에** [평가 기준 기록 양식](evals/acceptance-record.ko.md)으로 승인한 결과물, 기존 요구사항, 이번 변경 목표를 구분하세요. 형식 검사 통과, 모델의 자기평가, 사람의 승인은 서로 다른 근거입니다.

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

패키지 검증기와 기존 단위 테스트는 구조와 Python 문법을 검사합니다. 재고 예제는 명시한 출력 요구사항을 검사하며, 이 검사들로 에이전트 성능을 입증할 수는 없습니다. 실제 행동은 `evals/` 시나리오로 평가하고 평가 기준 기록에 근거를 남깁니다.

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_skill.py skills/distill
python -m unittest discover -s tests -v
```

CI는 push와 pull request마다 패키지 검사와 재고 예제 검사를 실행합니다. 요구사항을 보존하면서 스킬을 명확하거나 간결하게 만드는 변경을 환영합니다. 근거를 함께 가져와 주세요. 이유가 있는 유지 결정도 유용한 평가 결과입니다.

## 라이선스

[MIT](LICENSE)
