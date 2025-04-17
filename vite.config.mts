import { defineConfig } from "vitest/config";
import tsconfigPaths from "vite-tsconfig-paths";

export default defineConfig({
  test: {
    include: ["w*/*_test.ts"],
    passWithNoTests: true,
    environment: "node",
  },
  plugins: [tsconfigPaths()],
});