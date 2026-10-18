# llm-final

## Checks after editing

Run all four on the changed files:

1. `uv run pytest`
2. `uv run byname tool basedpyright FILE...`
3. `uv run byname tool ruff check FILE...`
4. `uv run annotation-check FILE.pyn...` (from ../ml-tools)

annotation-check reports three things:

- **`name is Any`** (or `unknown`, `partially unknown`): the name shows white in the editor. basedpyright and ruff don't catch these. Fix it by
  annotating where the name is first bound (`out: Tensor = self.proj(x)`). A line with `# any:ok` is skipped.
- **`T is Unknown to the checker`**: the annotation itself is untyped (`table: pa.Table` without pyarrow's
  stubs), so the name still shows white. Fix the type, not the annotation.
- **`T is inferred anyway`**: a redundant annotation. Leave it and mention it. Whether these get removed
  is undecided, because an annotation also guards later reassignments.

Fix the checks themselves in ../ml-tools, never by copying them into this repo.
