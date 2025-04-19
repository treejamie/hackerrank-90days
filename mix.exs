defmodule Hackerank.MixProject do
  use Mix.Project

  @doc """
  The most basic mix project that I need to get these elixir
  challenges behaving like an actual Elixir project.
  """
  def project do
    [
      app: :hackerank,
      version: "1.0.0",
      elixirc_paths: elixirc_paths(Mix.env())
    ]
  end

  defp elixirc_paths(:test), do: ["tests", "w1", "w2", "w3", "w4", "w5"]
  defp elixirc_paths(_), do: ["lib", "w1", "w2", "w3", "w4", "w5"]
end
