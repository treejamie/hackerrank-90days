[![Tests](https://github.com/treejamie/hackerrank-90days/actions/workflows/test.yml/badge.svg)](https://github.com/treejamie/hackerrank-90days/actions/workflows/test.yml)

# [HackerRank 90 Days](https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit/three-month-week-three/challenges)

This repo’s layout isn’t idiomatic to any one language — it’s a mix of Elixir, Go, Python, and TypeScript.

Spot something I could improve? Open an issue and point it out — that would be swell.

## 🙋 Why?

The HackerRank 90-day course was designed as a three-month prep for recruitment pipelines. Whilst I started out with that intention, I’m not using it for that purpose anymore (_at least not directly_). I’m using it to apply my Python and Elixir knowledge to scaffold my development in Go and TypeScript.

What I’m noticing, though, is that it’s also improving my authoring skills more broadly.

I started in January. At first, I just wanted to get through it in Python — a collection of scripts to store solutions. Then I added per-file unit testing. Then I started doing the challenges in different languages, and it evolved from there. Now it’s basically a code dojo for me, where I’m free to pick a task and write it up in a bunch of languages.

I’ll be very pleased if I complete these challenges by the end of 2025 in four languages: Python, Elixir, Go, and TypeScript. The aim is to get a nice 25% language distribution across the repository and to demonstrate competence in basic project layout, standard libraries, testing methodologies, and — most importantly — low-complexity solutions.

For example, many challenges can be solved easily with an `O(n^2)` approach, but HackerRank will timeout when you submit inefficient code. That’s a great forcing function — you’re not allowed to be lazy.

## 🧱 Structure

The project is structured by **weeks**, not by language. That is: none of the projects follow idiomatic layouts for their respective languages.

Each week has a folder named `w1`, `w2`, etc. Inside each is a `tc` (_test cases_) folder, which contains test files in a very specific format. For example, here’s the test case data for a made-up challenge where you’re given two integers and must sum them. Arguments are separated from expected output by two blank lines:

```plaintext
1 2

3
```

This format ensures each challenge across all languages consumes the same input/output.

## 📅 Three Months?

This course was meant to be three months long, but I’m not treating it that way. Technically, you’re supposed to use HackerRank’s interface to author your code — but that’s a horrific experience.

If I finish all the challenges in four languages by the end of 2025, I’ll be very pleased.

## 😱 Idiomaticity

(_I made that word up_)

This repository is a mix of several languages, and I’ve prioritized their coexistence over idiomatic project layout. For example, the Elixir code isn’t structured like a proper Mix project — same with TypeScript, Python, and Go.

The point is to compare approaches side by side, not to build polished, standalone apps.

That said, I still try to write idiomatic code within each language’s norms.

## 🤖 LLM usage

### Code

None of the challenge solutions are directly written by AI. I do use LLMs while coding — they’re great scaffolds for learning.

### Documentation & Comments

Most comments were written by me and then passed through an LLM to make them more succinct. I tend to be overly wordy — LLMs are great at "neutral speak".


## ✅ Test & Quality

### Elixir

There are two quality checks ran on the challenges -  tests and static analysis.

Tests are handled with ExUnit:

```bash
mix test w*
```

Static analysis is done with Dialyzer:

```bash
mix compile
mix dialyzer
```

The main aim of using dialyzer is to get some practice in with being clear about `@spec`.

### Go

```bash
cd w1
go test -v
```

### TypeScript

```bash
pnpm vitest run
```


### Python

```bash
python -m unittest -v  */*_test.py
```
