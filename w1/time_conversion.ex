defmodule HackerRank.W1.TimeConversion do
  @moduledoc """
  Time Conversion – Challenge 3 – Week 1
  <https://www.hackerrank.com/challenges/three-month-preparation-kit-time-conversion/problem>
  """

  @doc """
  Converts 12-hour AM/PM time format to 24-hour military time.

  ## Examples

      iex> challenge("07:05:45PM")
      "19:05:45"

  ## Constraints

  - Input format: `"hh:mm:ssAM"` or `"hh:mm:ssPM"`
  - Always returns a string in 24-hour format
  """
  @spec challenge(String.t()) :: String.t()
  def challenge(s) do
    # Dates / Times are not Elixis strong suit
    # However, binary string pattern matching is so let's do that then
    [hh, mm, ss_am_pm] = String.split(s, ":")

    # now we need am / pm
    <<ss::binary-size(2), period::binary>> = ss_am_pm

    # now parse into the correct types
    hour = parse_hour(hh, period)
    minute = String.to_integer(mm)
    second = String.to_integer(ss)

    # run everything through pad and return with Enum.map_join
    Enum.map_join([hour, minute, second], ":", &pad2/1)
    end

  defp parse_hour("12", "AM"), do: 0
  defp parse_hour(h, "AM"), do: String.to_integer(h)
  defp parse_hour("12", "PM"), do: 12
  defp parse_hour(h, "PM"), do: String.to_integer(h) + 12

  defp pad2(number) do
    :io_lib.format("~2..0B", [number]) |> to_string()
  end
end
