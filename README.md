## What does this do?

This is an LLM prompt originally based on SuperPrompt for Claude, adapted to
Gemini, and now forked, modified & extended. Additional features have been added
to it and it's most powerful when used as a 2-stage pipeline. Feed it your
problems and watch things unroll and expand! There are plenty example
test cases available [here](test-cases/gemini-1.5_pro/).

- [GEMINI-1.5_PRO.txt](GEMINI-1.5_PRO.txt): The primary engine for problem exploration à la SuperPrompt.
- [GEMINI-1.5_PRO.schizoanalysis.txt](GEMINI-1.5_PRO.schizoanalysis.txt): A specialized engine designed for performing schizoanalysis on specific texts or concepts. Use with the XML output of the primary engine or with your own texts / problem statements.
- [GEMINI-1.5_PRO.execution_engine.txt](GEMINI-1.5_PRO.execution_engine.txt): A specialized secondary engine that processes the output from the primary engine to generate further insights and analysis. Use with the XML output of the primary engine.

## How do I use it?

With the Gemini API or with Google AI Studio. Make sure to put the prompts into
the "System Instructions" box. All work here has *only* been done with the
Gemini 1.5 Pro Experimental 0827 (2024) model. Using any other model, your
results may vary.

## Important statement on scope

These engines are not one-shot instant solution machines; they are a catalyst
for creative disruption. It doesn't provide final answers, it is not going to
instantly solve hunger or create peace in the entire world, but it can help
you break free from conventional thinking, discover unexpected connections,
and generate novel ideas for addressing complex challenges. The prompts generate
conceptual entropy — schizoanalytically, a surge of unpredictable ideas,
connections, and lines of flight that can break you out of stagnant
thought patterns.

By feeding your concepts, questions, or problems into the engine, you'll
receive a blast of interpretations, unexpected juxtapositions, and
thought-provoking challenges. This deliberate injection of entropy can
destabilize your assumptions, spark new insights, and propel your thinking
in entirely new directions.

These prompts are not just a *tool*, but are a *process*, for those who
dare to think differently, to embrace the chaos, and to explore the
uncharted territories of thought.

## Research & Papers

- (2024-09-07): "[Beyond Linearity: A Schizoanalytic Approach to Emergence in Social Systems, Catalyzed by Large Language Models](papers/00_beyond_linearity/README.md)"

## Call to Action

This project is an ongoing exploration, and we invite you to join the conversation.

- Explore the code and the documentation.
- Run the engines on your own texts or concepts.
  - Saw some interesting results you want to share? Feel free to submit them as a test case.
- Share your feedback, insights, and criticisms.
- Contribute to the project through pull requests or issues.

## Implementation Details

A difference with this implementation is that the 1st stage is a lot more
"verbose" about its output and tries to generate output for all the tags where
it can. I find it to be far more useful this way, rather than in many cases
keeping the tags "within" as SuperPrompt does for Claude.

Notes on settings:

- Consider increasing output length.
- I've mostly been working with 1.1 to 1.5 temperature.
- Depending on your problem statement, you may want to experiment and find what
  works best for you, depending on the type of output that you want to see.

Additionally:

- Pay close attention to any "citation" hallucinations. This is where the LLM makes a
  "direct" citation to a URL (represented by a curly *`”`* button in the AI
  Studio UI). See our paper above for further information on how this process
  works out in practice.

  If you get this, congratulations! This means that the LLM may have just
  synthesized a novel brand-new concept integration inside its latent-space
  representation, or, otherwise found an interesting direct link in its
  vector store.

  My suggestion: do *not* dismiss it as "just" noise. Explore *much* further
  *and* deeper.
