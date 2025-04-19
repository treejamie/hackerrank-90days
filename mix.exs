defmodule Hackerank.MixProject do
  use Mix.Project

  @doc """
  The most basic mix project that I need to get these elixir
  challenges behaving like an actual Elixir project.
  """
  def project do
    [
      app: :hackerrank,
      version: "1.0.0",
      elixirc_paths: elixirc_paths(Mix.env()),
      deps: [
        {:dialyxir, "~> 1.3", only: [:dev], runtime: false}
      ],
      dialyzer: [
        plt_add_apps: [:mix],
        ignore_warnings: ".dialyzer_ignore.exs",
        list_unused_filters: true,
        flags: [
          :unmatched_returns,
          :error_handling,
          :underspecs,
          :unknown
        ],
        paths: ["_build/dev/lib/hackerrank/ebin"]
      ]
    ]
  end

  defp elixirc_paths(:test), do: ["tests", "w1", "w2", "w3", "w4", "w5"]
  defp elixirc_paths(_), do: ["lib", "w1", "w2", "w3", "w4", "w5"]
end
