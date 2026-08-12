SUMMARY_PROMPT_V1 = "Summarise this: "

SUMMARY_PROMPT_V2_SYSTEM = """
You are an assistant to a microfinance loan officer.
Summarize loan applications factually and neutrally.
Do not invent or assume any details that are not stated in the application.
Keep the summary to 3–4 sentences.
"""


EXTRACT_PROMPT = """
Extract the required information from the loan application.
Return ONLY a JSON object with EXACTLY these keys:
applicant_name (string),
amount_ghs (number),
purpose (string),
monthly_profit_ghs (number or null),
has_collateral_or_guarantor (boolean),
repayment_months (number or null).

If a field is not stated in the letter, use null. Do not guess.

Example letter:
My name is Ama Mensah. I need GHS 10,000 to buy a freezer
for my beverage business. I make GHS 800 profit each month.
My brother will guarantee the loan, and I will repay it over 12 months.

Example JSON:
{
    "applicant_name": "Ama Mensah",
    "amount_ghs": 10000,
    "purpose": "buy a freezer for my beverage business",
    "monthly_profit_ghs": 800,
    "has_collateral_or_guarantor": true,
    "repayment_months": 12
}
"""


def BRIEF_PROMPT(letter_text, result):
    prompt = f"""
Review this loan application and the extracted information.

Loan application:
{letter_text}

Extracted information:
{result}

Strengths:
- Identify and list strengths that are directly supported by the loan application.
- Do not invent or assume any information.

Risks / red flags:
- Identify risks or red flags that are supported by the loan application.
- Do not invent or assume any information.

Missing information:
- Identify and list important information that is not provided in the application
  and that the loan officer should request.
- Do not invent or assume any information.

Suggested next step:
- Recommend an appropriate next step based on the information available.
- Examples include "invite for interview", "request documents", or
  "flag for senior review".
- Do NOT recommend approving or rejecting the loan.

Final decision:
- The final loan decision must be made by a human loan officer.
- Do not approve or reject the application.
"""
    return prompt