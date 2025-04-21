defmodule HackerRank.W1.CamelCase do
@moduledoc """
Camel Case – Challenge 5, Week 1.

[HackerRank Problem – Camel Case](https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem)
"""

@doc """
Creates or splits Java-style CamelCase variable, method, and class names.

## Parameters

  - `token` (string): A semicolon-separated string specifying the operation and target string.
    Format:
    - `C` = combine, `S` = separate
    - `M` = method, `C` = class, `V` = variable

## Returns

  - A string converted to or from CamelCase based on the specified configuration.

## Examples

    iex> CamelCase.challenge("C;V;can of coke")
    "canOfCoke"

    iex> CamelCase.challenge("S;M;sweetTea()")
    "sweet tea"

    iex> CamelCase.challenge("C;C;mirror")
    "Mirror"

    iex> CamelCase.challenge("C;M;santa claus")
    "santaClaus()"
"""

  @spec challenge(String.t()) :: String.t()
  def challenge(token) do
    # split the token up
    [o, v, t] = String.split(token, ";")

    # pass it off to the specific operation
    case [o, v] do
      ["C", "M"] -> combine_method(t)
      ["C", "V"] -> combine_variable(t)
      ["C", "C"] -> combine_class(t)
      ["S", "M"] -> split_method(t)
      ["S", "V"] -> split_variable(t)
      ["S", "C"] -> split_class(t)
    end
  end

  @doc """
  Combines a string into class name

  ## Parameters
  - `t`: a string to convert

  ## Returns
  - The formatted string

  ## Example

    iex> CamelCase.combine_class("mirror")
    "Mirror"
  """
  @spec combine_class(String.t()) :: String.t()
  def combine_class(t) do
    t
    |> String.split()
    |> Enum.map(&String.capitalize/1)
    |> Enum.join()
  end

  @doc """
  Combines a string into method name

  ## Parameters
  - `t`: a string to convert

  ## Returns
  - The formatted string

  ## Example

    iex> CamelCase.combine_method("santa claus")
    "santaClaus()"
  """
  @spec combine_method(String.t()) :: String.t()
  def combine_method(t) do
    # split up the first from the rest
    [first | rest] = String.split(t)

    # downcase the first, capitalise the rest and join it
    name =
      [String.downcase(first) | Enum.map(rest, &String.capitalize/1)]
      |> Enum.join()

    # whack a set of parenthesis on the end
    name <> "()"
  end

  @doc """
  Combines a string into variable name

  ## Parameters
  - `t`: a string to convert

  ## Returns
  - The formatted string

  ## Example

    iex> CamelCase.combine_variable("can of coke")
    "canOfCoke"
  """
  @spec combine_variable(String.t()) :: String.t()
  def combine_variable(t) do
    # split up the first from the rest
    [first | rest] = String.split(t)

    # downcase the first, capitalise the rest and join it
    [String.downcase(first) | Enum.map(rest, &String.capitalize/1)]
    |> Enum.join()
  end
  @doc """
  Splits a string from a class name

  ## Parameters
  - `t`: a string to convert

  ## Returns
  - The formatted string

  ## Example

    iex> CamelCase.split_class("sweetTea")
    "sweet tea"
  """
  @spec split_class(String.t()) :: String.t()
  def split_class(t) do
    t
    |> split_camel_case()
    |> Enum.map(&String.downcase/1)
    |> Enum.join(" ")
  end
  @doc """
  Splits a string from method name

  ## Parameters
  - `t`: a string to convert

  ## Returns
  - The formatted string

  ## Example

    iex> CamelCase.split_method("sweetTea()")
    "sweet tea"
  """
  @spec split_method(String.t()) :: String.t()
  def split_method(t) do
    t
    |> split_camel_case()
    |> Enum.map(&String.downcase/1)
    |> Enum.join(" ")
    |> strip_parens()
  end

  @doc """
  Splits a string from variable name

  ## Parameters
  - `t`: a string to convert

  ## Returns
  - The formatted string

  ## Example

    iex> CamelCase.split_variable("epsonPrinter")
    "epson printer"
  """
  @spec split_variable(String.t()) :: String.t()
  def split_variable(t) do
    t
    |> split_camel_case()
    |> Enum.map(&String.downcase/1)
    |> Enum.join(" ")
  end

  defp split_camel_case(t), do: Regex.scan(~r/[a-z]+|[A-Z][a-z]*/, t) |> List.flatten |> Enum.map(&String.trim/1)
  defp strip_parens(t), do: String.replace(t, "()", "")

end
