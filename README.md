<div align="center">

# DjangoProject

### Django 질문·답변 Q&A 게시판 (Pybo)

**Django로 게시판 서비스의 전 과정(모델 → 뷰 → URL → 템플릿)을 직접 구현한 학습 프로젝트**

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

<sub>한양대학교 ERICA · 스마트융합공학부 스마트ICT융합전공 · 웹프레임워크개발 실습</sub>

</div>

---

## 프로젝트 개요

> 사용자가 질문을 등록하면 다른 사용자가 답변을 다는 질문·답변(Q&A) 게시판입니다.

게시판 서비스의 핵심 흐름인 **모델 설계 → 뷰 로직 → URL 라우팅 → 템플릿 렌더링**의 전 과정을
직접 구현했습니다. 회원가입·로그인과 목록 페이징까지 포함해 실제 서비스에 가까운 형태로 완성했습니다.

---

## 주요 기능

| 기능 | 설명 |
|:--|:--|
| **질문 목록** | 최신순 정렬 · 한 페이지 10개씩 페이징 |
| **질문 상세** | 질문 내용과 등록된 답변 목록 표시 |
| **질문 등록** | 폼 검증(Form validation) 후 작성일시 자동 기록 |
| **답변 등록** | 질문에 종속된 답변 작성 (POST 전용 처리) |
| **회원 기능** | Django 인증 기반 회원가입 / 로그인 / 로그아웃 |

---

## 기술 스택

| 분류 | 내용 |
|:--|:--|
| **언어 · 프레임워크** | Python · Django |
| **데이터베이스** | SQLite |
| **UI** | Bootstrap 5 |
| **핵심 개념** | MTV 패턴 · Django ORM · ForeignKey(질문–답변 1:N) · ModelForm + CSRF · Paginator · django.contrib.auth |

---

## 프로젝트 구조

```
DjangoProject/
├─ config/        # 프로젝트 설정 (settings · 루트 URL · WSGI/ASGI)
├─ pybo/          # 게시판 앱 (Question·Answer 모델 · 목록/상세/등록 뷰 · URL · 폼)
├─ common/        # 회원 앱 (회원가입 폼 · 로그인/로그아웃)
├─ templates/     # base·navbar 상속 구조, 질문/회원 화면
├─ static/        # Bootstrap · 정적 파일
├─ db.sqlite3
└─ manage.py
```

### 데이터 모델

| 모델 | 필드 |
|:--|:--|
| **Question** | subject(제목) · content(내용) · create_date(작성일) |
| **Answer** | question(FK) · content(내용) · create_date(작성일) |

---

## 실행 방법

```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/Scripts/activate      # Windows
# source venv/bin/activate        # macOS/Linux

# Django 설치
pip install django

# 마이그레이션 후 서버 실행
python manage.py migrate
python manage.py runserver
```

실행 후 브라우저에서 `http://127.0.0.1:8000/` 접속.

---

## 데모 페이지

실행 화면과 상세 소개는 포트폴리오 페이지에서 확인할 수 있습니다.

**[프로젝트 페이지 →](https://taewoongyoun.github.io/django/)**

---

<div align="center">

**Contact** · 윤태웅 · [taewoong25@hanyang.ac.kr](mailto:taewoong25@hanyang.ac.kr)

</div>
