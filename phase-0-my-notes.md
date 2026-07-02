# Phase 0 – My Mental Model for Marketing Agents

1. Workflow vs Agent example: A fixed ad approval checklist (workflow) vs an agent that decides which tool to use (search trends, check budget, generate copy).

2. The 4 context primitives with marketing use:
   - Write: Scratchpad for campaign ideas
   - Select: Pull competitor data only when needed
   - Compress: Summarize long research into 1 paragraph
   - Isolate: Sub-agent for copy, another for visuals, another for targeting

3. Harness vs Model: The Claude Agent SDK or LangGraph gives me skills/hooks/memory — same model performs much better in a good harness.

4. Orchestrator-worker pattern: Lead agent plans the campaign and spawns 3 sub-agents (research, copy, A/B test ideas).

5. Top 3 failure modes I expect: Agent calls too many tools and costs money, forgets context, or makes up fake competitor data.

6. My personal goal: Build autonomous marketing agents that research trends, generate campaign ideas, and schedule posts for my projects (Paco store, language app, painting business etc.).

I understand the foundations and am ready for Phase 1.