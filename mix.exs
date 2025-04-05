defmodule Hackerank.MixProject do
  use Mix.Project

  def project do
    [
      app: :hackerank,
      version: "1.0.0",
      elixirc_paths: elixirc_paths(Mix.env())
    ]
  end
  defp elixirc_paths(:test), do: ["w1"]
  defp elixirc_paths(_), do: ["w1"]
end
