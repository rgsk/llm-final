### Comments Convention

Here's the convention now in train.pyn, taken from world_model:

1. **Shape header:** one line per tensor input, plus `out:`, written as `name: [shape]`. A few words may follow the shape, as in `out: [], the gradient norm before clipping`. `name:` lines are used only for shapes, never to describe a kwarg or setting.
2. **Function summary:** at most a line or two saying what the function does, and only when the name and signature don't already say it.
3. **Everything else goes inline**, next to the line it explains: why a branch exists, what a setting is for, a trick, an off-by-one. The comment goes above the line, or at the end of it if it's short.
4. **Prose blocks are only for design choices** that don't belong to one line, like `param_groups` (which params get decay) or `autocast` (bf16 per op, no GradScaler). These read as flowing sentences: the next sentence continues on the same line, and there's no `label:` structure.
5. **Comments that only repeat the code get dropped**, like "zero, backprop, clip, update" or "run: log every evaluation".

The question to ask of each comment is which line it's about. If the answer is one line, it goes next to that line. If it's about the whole function, it's the summary. If it's about a choice that affects several lines, it's a prose block.
