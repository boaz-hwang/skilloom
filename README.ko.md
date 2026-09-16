<h1 align="center">Skilloom</h1>

<p align="center">
  <strong>에이전트 스킬을 짜는 베틀.</strong><br>
  이미 끝낸 일에서 스킬을 짜냅니다. 버티는 실만 남기고, 나머지는 잘라냅니다.
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="#네-가지-스킬">스킬</a> ·
  <a href="#원칙">원칙</a> ·
  <a href="#설치">설치</a> ·
  <a href="#기여하기">기여</a>
</p>

<p align="center">
  <a href="https://github.com/boaz-hwang/skilloom/actions/workflows/validate.yml"><img alt="Validate" src="https://github.com/boaz-hwang/skilloom/actions/workflows/validate.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-black.svg"></a>
  <a href="https://github.com/agentskills/agentskills"><img alt="Agent Skills format" src="https://img.shields.io/badge/format-Agent%20Skills-blue.svg"></a>
</p>

---

## 왜 베틀인가

베틀은 날실 몇 가닥만 팽팽하게 고정합니다. 나머지는 그 위를 가로지르며 짜입니다.

스킬도 천처럼 망가집니다. 모자라서가 아니라 넘쳐서입니다. 문제를 하나 고칠 때마다 문장이 하나 붙고, 예외를 하나 만날 때마다 규칙이 하나 붙습니다. 어느 날 보면 유능한 모델이 일을 하기도 전에 읽고 넘겨야 할 지침의 벽이 서 있습니다.

Skilloom은 꼭 필요한 요구사항만 날실로 고정하고, 짜는 일은 모델에게 맡깁니다. 출발점은 이미 손에 있는 근거입니다. 승인한 결과물, 그때 준 피드백, 실패한 실행 기록. 거기서 결과가 의존하는 것만 남깁니다.

## 네 가지 스킬

각 스킬은 베틀의 동작 하나입니다. 따로 설치하고 따로 씁니다.

| 스킬 | 동작 | 이럴 때 |
| --- | --- | --- |
| [**distill**](skills/distill/README.ko.md) | 잣다 | 방금 끝내고 승인한 작업을 재사용 가능한 스킬로 만든다. |
| [**refine**](skills/refine/README.ko.md) | 조이다 | 장황하거나 지나치게 규정적인 스킬 하나를 목적 중심으로 재구성한다. |
| [**evolve**](skills/evolve/README.ko.md) | 깁다 | 실제 사용에서 드러난 문제를, 근거가 뒷받침하는 가장 작은 변경으로 고친다. |
| [**consolidate**](skills/consolidate/README.ko.md) | 잇다 | 겹치는 스킬들을 합치되, 잘 되던 기능은 하나도 잃지 않는다. |

넷을 합치면 스킬의 한살이가 됩니다. 실제 일에서 만들고, 정돈하고, 실제 실행에서 고치고, 중복을 다시 하나로 접습니다.

## 원칙

구호가 아닙니다. 하나하나가 스킬 안에 지침으로 적혀 있습니다.

- **삭제부터 검토한다.** 규칙을 더하기 전에, 하나를 지우면 승인된 요구사항을 놓치는지 묻는다. 아니라면 지운다. 넘치는 내용을 참고 파일로 옮겨 숨기지 않는다.
- **방법은 모델에게 맡긴다.** 결과, 결정적인 제약, 완료의 모습만 적는다. 도구, 언어, 구현 방식은 열어 둔다.
- **직감보다 근거.** 승인된 산출물, 수정 요청, 실행 기록이 입력이다. 없는 이력은 물어보지, 지어내지 않는다.
- **코드가 검증할 것은 코드가, 나머지는 사람이.** 생성된 스킬마다 자체 검사와 짧은 사람 검토 질문 목록이 따라간다. 개수와 서식은 정확성이나 안목을 대신하지 못한다.
- **침묵은 승인이 아니다.** 확인이 필요한 관문은 확인을 기다린다. 필요 없는 관문은 만들지 않는다.
- **짧아진 것과 나아진 것은 다르다.** 파일이 줄어든 건 구조 정리다. 개선을 말하려면 같은 조건에서 비교해야 한다. 스킬은 둘 중 무엇을 했는지 밝힌다.
- **바꾸지 않는 것도 결과다.** 근거가 수정을 뒷받침하지 않으면 스킬은 그대로 두고, 이유를 보고한다.

## 설치

코딩 에이전트에 아래를 붙여넣으세요.

```text
https://github.com/boaz-hwang/skilloom 을 git clone해서 skills/ 안의 네 폴더를 각각 별도 스킬로 스킬 디렉터리에 설치해줘.
```

스킬은 [Agent Skills](https://github.com/agentskills/agentskills) 형식을 따르므로 `SKILL.md`를 읽는 클라이언트라면 어디서든 동작합니다.

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

## 기여하기

저장소에는 형식 검증기와 테스트가 들어 있습니다. 구조와 Python 문법만 확인하고 결과 품질은 보지 않습니다. 품질은 `evals/`의 행동 시나리오로 직접 돌려 확인합니다.

```bash
python -m pip install -r requirements-dev.txt
python tools/validate_skill.py skills/distill
python -m unittest discover -s tests -v
```

CI는 push와 pull request마다 같은 검증을 실행합니다.

요구사항을 잃지 않으면서 스킬을 더 짧게 만드는 기여를 환영합니다. 근거상 빠져 있던 요구사항을 더하는 기여도 환영합니다. 근거를 함께 가져와 주세요.

## 라이선스

[MIT](LICENSE)
