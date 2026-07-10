#!/usr/bin/env python3
"""
Meeting Briefing Agent

An agent that prepares executive meeting briefings by analyzing context
and leveraging available strategy consulting skills.
"""

import json
import os
from typing import Optional
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()
MODEL = "claude-opus-4-8"

# Define available strategy skills
STRATEGY_SKILLS = {
    "diagnosis_framing": {
        "situation-assessment": "Establishes a fact-based baseline for a business, market, or function",
        "growth-barriers": "Identifies the true constraint blocking growth",
        "assumption-audit": "Tests validity of strategic assumptions before major decisions",
    },
    "market_intelligence": {
        "market-mapping": "Sizes and segments markets using top-down and bottom-up logic",
        "competitive-intel": "Models likely competitor moves",
        "customer-segmentation": "Creates MECE customer segments by needs, economics, and value",
        "profit-pool-analysis": "Maps where profit is created and captured",
    },
    "strategic_choice": {
        "strategic-options": "Generates and compares strategic options",
        "business-case-builder": "Quantifies economics with base, downside, and upside cases",
        "portfolio-review": "Reviews a portfolio and recommends allocation choices",
        "pricing-strategy": "Diagnoses pricing leakage and designs pricing moves",
    },
    "operating_model": {
        "initiative-prioritizer": "Prioritizes initiatives by impact, feasibility, and fit",
        "operating-model-design": "Translates strategy into capabilities and decision rights",
        "transformation-roadmap": "Converts strategy into sequenced workstreams and milestones",
    },
    "risk_performance": {
        "risk-and-mitigation": "Builds a strategic risk register",
        "kpi-architect": "Designs KPI systems with leading and lagging indicators",
        "war-gaming": "Stress-tests strategy against scenarios",
        "value-realization": "Defines how strategic value will be tracked and measured",
    },
    "alignment": {
        "decision-memo": "Writes executive decision memos",
        "narrative-builder": "Builds executive strategy narratives using Pyramid Principle",
        "stakeholder-alignment": "Maps stakeholders and builds a pre-wire plan",
    },
}


def format_available_skills() -> str:
    """Format available skills for the agent prompt."""
    skills_text = "# Available Strategy Skills\n\n"
    for domain, skills in STRATEGY_SKILLS.items():
        domain_name = domain.replace("_", " ").title()
        skills_text += f"## {domain_name}\n"
        for skill_name, description in skills.items():
            skills_text += f"- **/{skill_name}**: {description}\n"
        skills_text += "\n"
    return skills_text


def create_meeting_briefing_agent():
    """Create and run the meeting briefing agent."""

    system_prompt = f"""You are an executive meeting briefing specialist. Your role is to help prepare
comprehensive, data-driven briefings for strategic meetings.

You have access to the following strategy consulting skills that you can leverage:

{format_available_skills()}

## Your Process

1. **Understand the Meeting Context**
   - Ask about the meeting type, attendees, and key decisions/discussions
   - Understand the business context and current challenges
   - Identify what information will be most valuable

2. **Recommend Relevant Skills**
   - Based on the meeting context, recommend which strategy skills would be most valuable
   - Explain why each skill is relevant to the meeting

3. **Prepare Briefing Materials**
   - Guide the user through data collection for relevant skills
   - Help structure the briefing around key insights
   - Ensure materials are executive-ready and decision-focused

4. **Synthesize the Briefing**
   - Create a cohesive narrative that tells the story across multiple analyses
   - Highlight key insights, risks, and recommendations
   - Provide actionable next steps

## Quality Standards

- Be fact-based and data-driven
- Separate findings from recommendations
- Focus on the few things that matter most
- Make briefings executive-ready and time-efficient
- Ensure strategic rigor using the consulting frameworks

Begin by asking about the meeting context to understand what type of briefing is needed."""

    conversation_history = []

    print("=" * 70)
    print("MEETING BRIEFING AGENT")
    print("=" * 70)
    print("\nWelcome to the Meeting Briefing Agent. I'll help you prepare an")
    print("executive briefing by leveraging strategy consulting skills.")
    print("\nType 'exit' to end the conversation.")
    print("-" * 70)
    print()

    # Initial agent message
    initial_message = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": "Please help me prepare a meeting briefing. Let's start."
        }]
    )

    assistant_message = initial_message.content[0].text
    print(f"Agent: {assistant_message}\n")

    conversation_history.append({
        "role": "user",
        "content": "Please help me prepare a meeting briefing. Let's start."
    })
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })

    # Main conversation loop
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'exit':
            print("\nThank you for using the Meeting Briefing Agent. Goodbye!")
            break

        if not user_input:
            continue

        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        # Get agent response
        response = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            system=system_prompt,
            messages=conversation_history
        )

        assistant_response = response.content[0].text

        conversation_history.append({
            "role": "assistant",
            "content": assistant_response
        })

        print(f"\nAgent: {assistant_response}\n")


def prepare_briefing_from_context(meeting_context: str) -> str:
    """
    Prepare a meeting briefing from context without interactive prompts.

    Args:
        meeting_context: Description of the meeting and required briefing

    Returns:
        The briefing analysis
    """
    system_prompt = f"""You are an expert executive briefing specialist. Prepare a comprehensive,
data-driven briefing based on the provided context.

Available strategy consulting skills:
{format_available_skills()}

Create a detailed briefing that:
1. Analyzes the situation using relevant frameworks
2. Identifies key issues and implications
3. Recommends the most relevant strategy skills for deeper analysis
4. Provides structured insights organized for executive review
5. Suggests key discussion points and decisions

Output should be well-structured, executive-ready, and actionable."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=system_prompt,
        messages=[{
            "role": "user",
            "content": f"Please prepare a comprehensive briefing for the following meeting:\n\n{meeting_context}"
        }]
    )

    return response.content[0].text


def main():
    """Main entry point."""
    import sys

    if len(sys.argv) > 1:
        # If meeting context provided as argument
        meeting_context = " ".join(sys.argv[1:])
        print("Preparing briefing from context...")
        print("=" * 70)
        briefing = prepare_briefing_from_context(meeting_context)
        print(briefing)
    else:
        # Interactive mode
        create_meeting_briefing_agent()


if __name__ == "__main__":
    main()
