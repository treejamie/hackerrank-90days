[![Tests](https://github.com/treejamie/hackerrank-90days/actions/workflows/test.yml/badge.svg)](https://github.com/treejamie/hackerrank-90days/actions/workflows/test.yml)

# [HackerRank 90 Days](https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit/three-month-week-three/challenges)

This repo’s layout isn’t idiomatic to any one language — it’s a mix of Elixir, Go, Python, and TypeScript.

## Quality

When I first started these challenges, I was in a teaching job and I was completing them between classes and during times when my students had been tasked and was literally doing nothing. These challenges go all the way up to week 4/5. These are not my best work, I was more interested in making stuff work.  However, when I quit the teaching job and was able to sit down and focus on quality, I started everything again. I went over the week one python work and moved everything to a standard that any colleage, customer or employer would be more than happy with. 

So below is a table of challenges that I consider to be complete, and to have been completed to a high professional standard that you'd expect from any work I was doing. Inline docs, testing, linting, static code analysis, CI/ CD etc.  Each PR for each challenge is listed below. If it's not in this table and it's in the repo, consider it a working draft of my thoughts.


### Week 1

| |                         | Python                  | Elixir                  | TypeScript    | Go    |
|-|-                        |-                        |-                        |-              |-      |  
| W1/1| Plus Minus          |[![PR](img/pr.svg)][11py]|[![PR](img/pr.svg)][11ex]|     ➖        |[![PR](img/pr.svg)][11go]|  
| W1/2| Mini Max Sum        |[![PR](img/pr.svg)][12py]|[![PR](img/pr.svg)][12ex]|     ➖        |[![PR](img/pr.svg)][11go]|  
| W1/3| Time Conversion     |[![PR](img/pr.svg)][13py]|[![PR](img/pr.svg)][13ex]|[![PR](img/pr.svg)][13ts]|[![PR](img/pr.svg)][11go]|  
| W1/4| Breaking Records    |[![PR](img/pr.svg)][14py]|[![PR](img/pr.svg)][14ex]|     ➖        |   ➖   |  
| W1/5| Camel Case          |[![PR](img/pr.svg)][15py]|[![PR](img/pr.svg)][15ex]|     ➖        |   ➖   |  
| W1/6| Divisible Sum Pairs |[![PR](img/pr.svg)][16py]|[![PR](img/pr.svg)][16ex]|     ➖        |   ➖   |  
| W1/7| Sparse Array        |[![PR](img/pr.svg)][17py]|[![PR](img/pr.svg)][17ex]|     ➖        |   ➖   |  

[11py]: https://github.com/treejamie/hackerrank-90days/pull/108
[12py]: https://github.com/treejamie/hackerrank-90days/pull/108
[13py]: https://github.com/treejamie/hackerrank-90days/pull/109
[14py]: https://github.com/treejamie/hackerrank-90days/pull/111
[15py]: https://github.com/treejamie/hackerrank-90days/pull/113
[16py]: https://github.com/treejamie/hackerrank-90days/pull/114
[17py]: https://github.com/treejamie/hackerrank-90days/pull/115

[11ex]: https://github.com/treejamie/hackerrank-90days/pull/103
[12ex]: https://github.com/treejamie/hackerrank-90days/pull/138
[13ex]: https://github.com/treejamie/hackerrank-90days/pull/141
[14ex]: https://github.com/treejamie/hackerrank-90days/pull/142
[15ex]: https://github.com/treejamie/hackerrank-90days/pull/148
[16ex]: https://github.com/treejamie/hackerrank-90days/pull/151
[17ex]: https://github.com/treejamie/hackerrank-90days/pull/152

[11ts]: #
[12ts]: #
[13ts]: https://github.com/treejamie/hackerrank-90days/pull/136
[14ts]: #
[15ts]: #
[16ts]: #
[17ts]: #

[11go]: https://github.com/treejamie/hackerrank-90days/pull/102
[12go]: https://github.com/treejamie/hackerrank-90days/pull/105
[13go]: https://github.com/treejamie/hackerrank-90days/pull/147
[14go]: #
[15go]: #
[16go]: #
[17go]: #

### Week 2

I'll update this README with week two once I've completed all the challenges in all the languages from week one.


Spot something I could improve? Open an issue and point it out — that would be swell.

## 🙋 Why?

The HackerRank 90-day course was designed as a three-month prep for recruitment pipelines. Whilst I started out with that intention, I’m not using it for that purpose anymore (_at least not directly_). I’m using it to apply my Python and Elixir knowledge to scaffold my development in Go and TypeScript.

What I’m noticing, though, is that it’s also improving my authoring skills more broadly.

I started in January. At first, I just wanted to get through it in Python — a collection of scripts to store solutions. Then I added per-file unit testing. Then I started doing the challenges in different languages, and it evolved from there. Now it’s basically a code dojo for me, where I’m working through each challenge in each language. I'm learning a lot. Especially about parsing text files (_test cases_).

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
