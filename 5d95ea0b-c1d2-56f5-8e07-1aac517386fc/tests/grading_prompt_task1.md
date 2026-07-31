You are an expert evaluator verifying factual claims in a financial analysis.

{data_context}

<agent_answer>
{agent_answer}
</agent_answer>

Identify every SPECIFIC factual claim in the agent's answer — numerical figures (percentages, dollar amounts, basis points, growth rates), quoted phrases, named entities, dates, and concrete comparisons. For each, verify it is present in the source data above (or is a clearly-stated inference whose components are).

Flag a claim as a HALLUCINATION if:
- A number does not appear in any data file.
- A quote is attributed to a file that does not contain that quote.
- A comparison value is not in the data.
- A specific event, statement, or entity is referenced and is not in the data.

Inferences and analytical framings are NOT hallucinations as long as their factual building blocks are present. The bar is "did the agent make up a fact."

For each claim you flag, write a short `evidence_check` describing what you searched for and where (e.g., "searched flyw_q1_2025_earnings_call.txt for 'organic revenue growth of 22%' — not present").

Respond with ONLY a JSON object:
{{
  "hallucinations_detected": true | false,
  "unverifiable_claims": [
    {{
      "claim": "<verbatim quote of the unverifiable claim from the agent's answer>",
      "cited_file": "<file the agent cited, or null if uncited>",
      "issue": "<concise explanation>",
      "evidence_check": "<short note describing what you searched for and where>"
    }}
  ]
}}
