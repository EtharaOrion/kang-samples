You are an expert evaluator checking for an explicit synthesis sentence in a financial analysis.

<ground_truth>
{ground_truth}
</ground_truth>

<agent_answer>
{agent_answer}
</agent_answer>

The rubric defines a SYNTHESIS REQUIREMENT in its preface — typically that a top score requires at least one explicit reconciliation of opposing data points, not just listing them in parallel.

Quote the synthesis sentence from the agent's answer if you find one; otherwise return null.

Respond with ONLY a JSON object:
{{
  "synthesis_found": "<quote of the synthesis sentence, or null>"
}}
