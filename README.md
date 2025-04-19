# [Hackerrank 90 days](https://www.hackerrank.com/interview/preparation-kits/three-month-preparation-kit/three-month-week-three/challenges)


This repo’s layout isn’t idiomatic to any one language — Python was my strongest when I started, and it probably shows. I’m aiming to make that less obvious as I go through the challenges that by the end.

Spot something I could improve? A pull request would be lovely.


## 🙋 Why?

The 90 days worth of interview preparation on hackerrank. Public so that others may witness the learning and re-awakening of well rested neural pathways and the creation of new ones.

I'll working through the challenges in Python and then I'll be starting from scratch in Go, Elixir and TypeScript. Maybe even rust. I didn't start out with this aim, but that's how I ended up.  By the start of week five of doing them in Python I decided to use the challenges as a means of supporting my learning in other languages.

I don't think these challenges will make me a better programmer in themselves, but the act doing each one, in multiple languages probably will. 


## 🧱 Structure

As I go back through the each week, there will be a directory called testcases and in each will be a textfile containing the documented `stdin` and the expected output. Hackerrank isn't consistent between returning values and printing them out, so my code here will always default to returning values as it makes testing much less finicky.

Until I'm back to week five the structure will be over the place, but once I've been through each week in Go it'll get cleaner.

The format for the test cases is stdin inputs seperated by newlines and then the expected output seperated by two newlines.

## 📅 Three Months?

Unlikley I will get through these in six months let alone three, so I'm not binding myself to any timeframe. Learning takes time and one of the things I am focused on right now is taking my programming up a level that I always aspired to when I saw it in others - to be language agnostic.

I'm not the best programmer on Earth, but I think I have the potential to be a pretty good one. 

## Idiomaticity 😱

(_I made that word up_)

This repository is a mixture of a number of languages and I've prioritised coexistance of languages at the expense of any one languages typical project layout. For example the Elixir stuff isn't in a typical mix project. It was more important to the intention of what I'm doing here to have the languages side by side, so you can see similarities and differences.

Obviously, I keep whatever idoimatic language specific skills I possess in my approach to writing the code.

## 🤖 LLM usage

None of the code in this repository has solutions written by AI. You'll just have to take my word for that. In some solutions I used AI to reason about things and to discuss approaches, but all of the code is mine.

My approach to using LLM's and AI is to treat them like a teaching assistant who knows a lot but isn't always right. They're a great tool for learning and helping you understand a thing, but they are not (_in my humble opinion_) suitable for production output in most contexts.

Also, this is about learning and using LLM's for solutions doesn't help me - at all. It only pushes the barrier to learning further away from me.


## Quality & Assurance

### Elixir

There are two quality checks ran on the challenges -  tests and static analysis.

Tests are handled with ExUnit and are ran as follows:

```bash
mix test w*
```

Static analysis is done with dialyzer and is ran as follows:

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