import { describe, expect, it } from 'vitest';
import { readFileSync, readdirSync } from "fs";
import { resolve } from "path";

import { timeConversion } from './time_conversion';

const globDir = resolve(__dirname, "tc");

describe("Time Conversion", () => {
  const testFiles = readdirSync(globDir).filter(f => f.startsWith("3_") && f.endsWith(".txt"));

  testFiles.forEach(file => {
    it(`(W1/3): ${file}`, () => {
      const fullPath = resolve(globDir, file);
      const contents = readFileSync(fullPath, "utf-8").split("\n");

      const args = contents[0].trim();     // first line
      const expected = contents[2].trim();  // third line

      const result = timeConversion(args);
      expect(result).toBe(expected);
    });
  });
});