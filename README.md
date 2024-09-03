This is a prompt originally based on SuperPrompt for Claude and now adapted to
Gemini. Additional features have been added and it is a 2-stage pipeline. The
original SuperPrompt has been folded into the 1st stage and the 2nd stage is an
execution engine that iterates on the 1st stage.

A difference with this implementation is that the 1st stage is a lot more
"verbose" about its output and tries to generate output for all the tags where
it can. I find it to be far more useful this way, rather than in many cases
keeping the tags "within" as SuperPrompt does for Claude.
