---
name: unslop
description: Use only when the user explicitly asks to unslop, polish prose, rewrite prose, or remove AI-sounding language. Applies a focused anti-slop edit while preserving meaning and requested tone.
---

# Unslop

Edit the requested text to remove AI patterns and add a natural voice. When the text contains instructions for an agent, preserve its triggers, workflow, constraints, and completion criteria.

## Process

1. Scan for the patterns below.
2. Rewrite. Preserve meaning, match intended tone.
3. For human-facing prose, restore a natural voice.
4. Self-audit: "What makes this obviously AI generated?" Fix remaining tells.

## Human voice

For human-facing prose, removing patterns is half the job. Sterile, voiceless writing is just as obvious.

- **Have opinions.** React to facts instead of neutrally listing pros and cons.
- **Vary rhythm.** Short sentences. Then longer ones that take their time. Mix it up.
- **Acknowledge complexity.** "Impressive but also kind of unsettling" beats "impressive."
- **Use "I" when it fits.** First person isn't unprofessional.
- **Let some mess in.** Perfect structure looks machine-made.
- **Be specific.** Not "this is concerning" but "there's something unsettling about agents churning away at 3am."

## Patterns to detect and fix

### Content

1. **Puffery.** "pivotal moment", "testament to", "evolving landscape", "setting the stage for", "indelible mark", "deeply rooted". Cut puffery, state what happened.
2. **Name-dropping.** Listing media outlets without context. Pick one, say what was said.
3. **Superficial -ing phrases.** "highlighting...", "ensuring...", "reflecting...", "showcasing...", "fostering...". Delete or expand with real sources.
4. **Promotional language.** "nestled", "vibrant", "breathtaking", "groundbreaking", "renowned", "stunning", "must-visit". Use neutral descriptions.
5. **Vague attributions.** "Experts believe", "Industry reports suggest", "Some critics argue". Name the source or delete.
6. **Formulaic challenges.** "Despite challenges... continues to thrive." Replace with specific facts.

### Language

7. **AI vocabulary.** Additionally, crucial, delve, enduring, enhance, fostering, garner, interplay, intricate, landscape (abstract), pivotal, showcase, tapestry (abstract), testament, underscore, vibrant. Replace with plain words.
8. **Fancy ways to say "is".** "serves as", "stands as", "boasts", "features". Just say "is" or "has".
9. **"Not just X, but Y."** State the point directly instead.
10. **Rule of three.** Forcing ideas into groups of three. Use the natural number.
11. **Synonym cycling.** Protagonist, main character, central figure, hero all in one paragraph. Pick one, repeat it.
12. **False ranges.** "from X to Y" where X and Y aren't on a meaningful scale. List topics directly.

### Style

13. **Em dash overuse.** Avoid em dashes entirely. Use periods or commas instead. If a thought needs separation, end the sentence.
14. **Colon overuse.** Use colons before lists or examples, not as a default connector between thoughts.
15. **Boldface overuse.** Do not bold every proper noun or acronym.
16. **Inline-header lists.** Replace labels that merely restate the line. Keep a bold lead-in only when the following sentence adds new information.
17. **Title case headings.** Use sentence case.
18. **Decorative emojis.** Remove them from headings and bullets.
19. **Curly quotes.** Replace them with straight quotes.

### Communication artifacts

20. **Chatbot phrases.** Remove "I hope this helps!", "Let me know if...", "Of course!", "Certainly!", and similar filler.
21. **Cutoff disclaimers.** Replace vague limitations with sourced facts or remove them.
22. **Sycophantic tone.** Respond directly instead of praising the prompt or user.

### Filler

23. **Filler phrases.** "In order to" becomes "To". "Due to the fact that" becomes "Because". Delete "It is important to note that".
24. **Excessive hedging.** Replace stacked qualifiers with one accurate qualifier.
25. **Generic conclusions.** Replace them with specific plans or facts.

### Jargon

26. **Abstract metaphor nouns.** Replace words such as substrate, wedge, vector, locus, nexus, scaffolding, paradigm, endgame, and flywheel with the concrete mechanism or action they hide.

### Plain speech

27. **Say what it does.** Replace claims about how something feels with a concrete instruction, fact, mechanism, or number. Delete sentences that could appear unchanged in another project's documentation.
28. **Shorten dense sentences.** Split any sentence the reader must backtrack to understand.
29. **Active voice.** Name the actor when it matters.
30. **Cut adverbs.** Use a stronger verb or a measured fact.
31. **Prefer the plain word.** Use "use" instead of "utilize", "help" instead of "facilitate", and similarly direct wording.

## Completion criterion

The edit is complete when every applicable pattern has been checked, every detected instance has been rewritten or deliberately retained to preserve meaning, and the requested tone still holds.
