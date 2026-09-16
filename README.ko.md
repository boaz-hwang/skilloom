<p align="center">
  <img src="assets/skilloom.png" alt="Skilloom" width="480">
</p>

<h1 align="center">Skilloom</h1>

<p align="center">
  <strong>에이전트 스킬을 짜는 베틀.</strong><br>
  이미 끝낸 일에서 스킬을 만듭니다. 버티는 것만 남기고, 나머지는 잘라냅니다.
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

스킬은 자꾸 길어집니다. 문제를 하나 고칠 때마다 문장이 길어지고, 예외를 만날 때마다 규칙이 추가됩니다. 어느새 유능한 모델이 알아서 잘 할수 있는데 지침에 갇혀서 제대로 능력 발휘를 못하게 됩니다.

Skilloom은 이미 성공한 경험 즉, 승인한 결과물과 그때 준 피드백에서 출발해 핵심만 남깁니다. 나머지는 모델이 스스로 정합니다.

## 스킬

스킬의 한살이 단계마다 하나씩, 네 개입니다. 각각 따로 설치하고 따로 씁니다.

| 스킬 | | 이럴 때 |
| --- | --- | --- |
| [**distill**](skills/distill/README.ko.md) | 잣다 | 방금 끝내고 승인한 작업을 재사용 가능한 스킬로 만든다. |
| [**refine**](skills/refine/README.ko.md) | 조이다 | 장황한 스킬 하나를 목적 중심으로 재구성한다. |
| [**evolve**](skills/evolve/README.ko.md) | 깁다 | 실제 사용에서 드러난 문제를, 근거가 뒷받침하는 가장 작은 변경으로 고친다. |
| [**consolidate**](skills/consolidate/README.ko.md) | 잇다 | 겹치는 스킬들을 합치되, 잘 되던 건 잃지 않는다. |

넷이 공통으로 지키는 것:

- 더하기 전에 지울 것부터 본다.
- 코드가 검증할 수 있는 건 코드가. 나머지는 짧은 질문 목록으로 사람이 판단한다.
- 파일이 짧아졌다고 개선이라 부르지 않는다. 비교한 뒤에 부른다.
- 바꾸지 않는 것도 결과다.

## 설치

코딩 에이전트에 아래를 붙여넣으세요.

```text
https://github.com/boaz-hwang/skilloom 을 git clone해서 skills/ 안의 네 폴더를 각각 별도 스킬로 스킬 디렉터리에 설치해줘.
```

스킬은 [Agent Skills](https://github.com/agentskills/agentskills) 형식을 따르며, `SKILL.md`를 읽는 클라이언트라면 어디서든 동작합니다.

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
evolve로 <스킬명>의 실행 기록을 검토하고, 근거가 뒷받침하는 최소한의 개선만 해줘.
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

CI는 push와 pull request마다 같은 검사를 실행합니다. 요구사항을 잃지 않으면서 스킬을 더 짧게 만드는 변경을 환영합니다. 근거를 함께 가져와 주세요.

## 라이선스

[MIT](LICENSE)
