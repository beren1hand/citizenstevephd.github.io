"""
accusation_probability.py — Calculating the probability that all of
Donald Trump's sexual misconduct accusers are simultaneously lying.

=======================================================================
DATA SOURCE
=======================================================================
Wikipedia, "Donald Trump sexual misconduct allegations"
https://en.wikipedia.org/wiki/Donald_Trump_sexual_misconduct_allegations
(accessed April 2026)

    "As of October 2024, since the 1970s, at least 28 women have
    accused Donald Trump of various acts of sexual misconduct,
    including rape, sex with minors, sexual assault, physical abuse,
    kissing and groping without consent, looking under women's skirts,
    and walking in on naked pageant contestants."

The Wikipedia article aggregates named, on-the-record accusations
from court filings, sworn depositions, and published journalism,
citing primary sources including:

  - Relman, E. (2019). "The 26 women who have accused Trump of
    sexual misconduct." Business Insider.
  - "An Exhaustive List of the Allegations Women Have Made Against
    Donald Trump." The Cut (2016, updated).
  - Osborne, L. (2020). "'It felt like tentacles': the women who
    accuse Trump of sexual misconduct." The Guardian.

Other counts:
  - Axios (Oct 2024): 27 named accusers.
  - Women's Agenda (Oct 2024): 27 named accusers.
  - Levine, B. (2019). "All the President's Women: Donald Trump and
    the Making of a Predator." — documents 43 women, including
    anonymous and off-the-record accounts.
  - Leonard, E. (2025). Substack compilation: 31 named accusers.

This script uses 28 as a conservative baseline (Wikipedia's count)
and also computes results for 26, 27, and 31.

One accuser, E. Jean Carroll, has been adjudicated:
  - Carroll v. Trump, Case No. 1:22-cv-10016 (S.D.N.Y.)
  - May 9, 2023: Federal jury found Trump liable for sexual abuse.
  - January 26, 2024: Jury awarded $83.3 million in damages.

Trump denies all allegations.

=======================================================================
FALSE REPORT RATE
=======================================================================
Lisak, D., Gardinier, L., Nicksa, S.C., & Cote, A.M. (2010).
"False Allegations of Sexual Assault: An Analysis of Ten Years of
Reported Cases." Violence Against Women, 16(12), 1318-1334.

    Reviewed 10 years of sexual assault reports at a major
    Northeastern university. Found 5.9% were classified as false.

The National Sexual Violence Resource Center (NSVRC) review:
https://www.nsvrc.org/sites/default/files/publications/2018-10/Lisak-False-Reports-Moving-beyond.pdf

    Summarizes the research literature: methodologically sound
    studies consistently find false reporting rates of 2-10%.

The FBI Uniform Crime Reports historically cited ~8% "unfounded"
rate, though "unfounded" is a broader category than "false" and
includes cases dropped for insufficient evidence.

This script uses 10% as the most generous possible estimate to
give the strongest possible benefit of the doubt.

=======================================================================
MODEL
=======================================================================
Assumption: each accusation is an independent event with probability
p_false of being fabricated.

    P(all n accusers lying) = p_false ^ n

This is a GENEROUS model. It assumes:
  - No correlation between accusers (in reality, a true predator
    creates real victims, so accusations are positively correlated
    with guilt, not independent).
  - The highest credible false-report rate (10%).
  - Only publicly named, on-the-record accusers (excluding the
    43 documented by Levine including anonymous accounts).
  - That the E. Jean Carroll civil verdict carries no weight
    (in reality, a jury already found Trump liable).

Every one of these assumptions makes the result MORE favorable
to the hypothesis that all accusers are lying.

=======================================================================
"""

from decimal import Decimal
import math


def probability_all_lying(n_accusers: int, p_false: float) -> float:
    """P(all n independent accusers are lying) = p_false ^ n"""
    return p_false ** n_accusers


def format_odds(prob: float) -> str:
    """Express a tiny probability as '1 in X'."""
    if prob == 0:
        return "effectively zero"
    one_in = 1.0 / prob
    exponent = math.floor(math.log10(one_in))
    mantissa = one_in / (10 ** exponent)
    if exponent < 6:
        return f"1 in {one_in:,.0f}"
    return f"1 in {mantissa:.2f} × 10^{exponent}"


def main():
    print("=" * 70)
    print("Probability that ALL of Trump's accusers are simultaneously lying")
    print("=" * 70)
    print()

    accuser_counts = [26, 27, 28, 31]
    false_rates = [0.02, 0.05, 0.08, 0.10]

    # Header
    print(f"{'Accusers':>10}", end="")
    for rate in false_rates:
        print(f"  {'p_false=' + f'{rate:.0%}':>18}", end="")
    print()
    print("-" * 70)

    for n in accuser_counts:
        print(f"{n:>10}", end="")
        for rate in false_rates:
            prob = probability_all_lying(n, rate)
            print(f"  {format_odds(prob):>18}", end="")
        print()

    print()
    print("-" * 70)
    print()

    # Highlight the conservative case
    n = 28
    p = 0.10
    prob = probability_all_lying(n, p)
    print(f"Conservative case: {n} accusers, {p:.0%} false-report rate")
    print(f"  P(all lying) = {p}^{n} = {prob:.2e}")
    print(f"  That is: {format_odds(prob)}")
    print()

    # For context
    print("For context:")
    print(f"  Odds of winning Powerball jackpot:    1 in 292,201,338  (10^8)")
    print(f"  Odds of being struck by lightning:    1 in 500,000      (10^6)")
    print(f"  Odds all 28 accusers are lying (10%): {format_odds(prob)}  (10^{math.floor(math.log10(1/prob))})")
    print()

    # Using Decimal for exact computation
    prob_exact = Decimal("0.10") ** 28
    print(f"Exact value (arbitrary precision):")
    print(f"  {prob_exact}")
    print(f"  = 1 in {1 / prob_exact:,.0f}")
    print()

    print("Note: this model is GENEROUS to the 'all lying' hypothesis.")
    print("A jury has already found Trump liable for sexually abusing")
    print("E. Jean Carroll. If we treat that as settled, the question")
    print("becomes the probability that the OTHER 27 are all lying:")
    prob_27 = probability_all_lying(27, 0.10)
    print(f"  P(other 27 all lying at 10%) = {format_odds(prob_27)}")


if __name__ == "__main__":
    main()
