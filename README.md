# Conway's Game of Life

![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=.net&logoColor=white)
![Dart](https://img.shields.io/badge/dart-%230175C2.svg?style=for-the-badge&logo=dart&logoColor=white)
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Ruby](https://img.shields.io/badge/ruby-%23CC342D.svg?style=for-the-badge&logo=ruby&logoColor=white)
![Rust](https://img.shields.io/badge/rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)

<!-- ![Assembly](https://img.shields.io/badge/Assembly-black?style=for-the-badge&logo=arm&logoColor=white)
![Fortran](https://img.shields.io/badge/D-AA0000.svg?style=for-the-badge&logo=d&logoColor=white)
![Elixir](https://img.shields.io/badge/elixir-%234B275F.svg?style=for-the-badge&logo=elixir&logoColor=white)
![F#](https://img.shields.io/badge/f%23-%23239120.svg?style=for-the-badge&logo=.net&logoColor=white)
![Fortran](https://img.shields.io/badge/Fortran-%23734F96.svg?style=for-the-badge&logo=fortran&logoColor=white)
![Go](https://img.shields.io/badge/go-%2300ADD8.svg?style=for-the-badge&logo=go&logoColor=white)
![Haskell](https://img.shields.io/badge/Haskell-5e5086?style=for-the-badge&logo=haskell&logoColor=white)
![Julia](https://img.shields.io/badge/-Julia-9558B2?style=for-the-badge&logo=julia&logoColor=white)
![Nim](https://img.shields.io/badge/nim-%23FFE953.svg?style=for-the-badge&logo=nim&logoColor=black)
![Perl](https://img.shields.io/badge/perl-%2339457E.svg?style=for-the-badge&logo=perl&logoColor=white)
![Zig](https://img.shields.io/badge/Zig-%23F7A442.svg?style=for-the-badge&logo=zig&logoColor=black) -->

Conway's Game of Life in an many programming languages as I can figure out

## Prerequisites

<!-- - Assembly
  - GNU Binutils (as & ld)
  - Raspberry Pi 4
 - D
  - GCC (GDC)
- Elixir
- F#
  - .NET SDK
- Fortran
  - GCC (gfortran)
- Haskell
  - GHC
- Julia
- Nim
- Perl -->
- C
  - GCC
  - GNU Make
- C++
  - GCC
  - Meson
  - Ninja
- C#
  - .NET SDK
- Dart
- Go
- Python
- Ruby
- Rust
  - Cargo
- Typescript
  - Node.js
  - Yarn
<!-- - Zig -->

## Building from Source

<!-- ### Assembly

This is written for a Raspberry Pi 4 running aarch64 Linux

```sh
cd asm/
make
./game_of_life
``` -->

### C

```sh
cd c/
make
./game_of_life
# or
./game_of_life -g 50 -h 20 -w 40
```

### C++

```sh
cd cpp/
meson setup build
cd build
ninja
./game_of_life
# or
./game_of_life --generations 50 --size 40x20
```

### C\#

```sh
cd csharp/
dotnet run
# or
dotnet run -- --generations 50 --size 40x20
```

### Dart

```sh
cd dart/
dart run
# or
dart run --generations 50 --size 40x20
```

<!-- ### Elixir

```sh
cd elixir/
elixir game_of_life.exs
```

### F\#

```sh
cd fsharp/
dotnet run
``` -->

### Go

```sh
cd go/
go run . --generations 50 --size 40x20
```

<!--
### Haskell

```sh
cd haskell/
ghc game_of_life.hs
./game_of_life
```

### Julia

```sh
cd julia/
julia game_of_life.jl
``` -->

### Python

```sh
cd python/
python game_of_life.py
# or
python game_of_life.py --generations 50 --size 40x20
```

### Ruby

```sh
cd ruby/
ruby GameOfLife.rb
# or
ruby GameOfLife.rb --generations 50 --size 40x20
```

### Rust

```sh
cd rust/
cargo run
# or
cargo run -- --generations 50 --size 40x20
```

### Typescript

```sh
cd typescript/
yarn install
yarn run main
# or
yarn run main --generations 50 --size 40x20
```

<!-- ### Zig

TODO: -->

## Benchmarking

There's an included script to build all version and run benchmarks. It requires [zx](https://github.org/google/zx) to run

```sh
zx --install benchmark.mjs
```

`--install` is only needed on the first run to install the script's dependencies

You can also specify how many generations to run the benchmark, as well as the number of generations and size of the game

```sh
zx benchmark.mjs --generations 5 --generations 100 --size 50x25
```
