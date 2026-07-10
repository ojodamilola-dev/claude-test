#!/usr/bin/env python3
"""
Briefing Orchestrator

Advanced agent that coordinates multiple strategy skills to prepare
comprehensive executive briefings.
"""

import json
from typing import Optional, Dict, List
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()
MODEL = "claude-opus-4-8"

# Strategy skill definitions
SKILLS_CONFIG = {
    "diagnosis": [
        "situation-assessment",
        "growth-barriers",
        "assumption-audit",
    ],
    "market": [
        "market-mapping",
        "competitive-intel",
        "customer-segmentation",
        "profit-pool-analysis",
    ],
    "strategy": [
        "strategic-options",
        "business-case-builder",
        "portfolio-review",
        "pricing-strategy",
    ],
    "execution": [
        "initiative-prioritizer",
        "operating-model-design",
        "transformation-roadmap",
    ],
    "governance": [
        "risk-and-mitigation",
        "kpi-architect",
        "war-gaming",
        "value-realization",
    ],
    "communication": [
        "decision-memo",
        "narrative-builder",
        "stakeholder-alignment",
    ],
}


class BriefingOrchestrator:
    """Orchestrates multi-skill analysis for executive briefings."""

    def __init__(self):
        self.conversation_history = []
        self.briefing_analysis = {}
        self.selected_skills = []

    def analyze_meeting_type(self, meeting_context: str) -> Dict[str, any]:
        """
        Analyze the meeting context and determine which skills to use.

        Args:
            meeting_context: Description of the meeting

        Returns:
            Dictionary with recommended skills and briefing strategy
        """
        analysis_prompt = f"""Analyze this meeting context and recommend which strategy consulting
skills would be most valuable for preparing an executive briefing.

Meeting Context:
{meeting_context}

For this meeting, identify:
1. The core strategic question or decision needed
2. Which 3-5 strategy skills are most relevant (from the available domains)
3. The order in which to conduct analysis
4. Key information needed from each skill
5. How to synthesize the findings into a cohesive briefing

Recommend skills using their skill names (e.g., 'situation-assessment', 'competitive-intel')."""

        response = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            messages=[{
                "role": "user",
                "content": analysis_prompt
            }]
        )

        analysis_text = response.content[0].text
        self.conversation_history.append({
            "role": "assistant",
            "content": analysis_text
        })

        return {"analysis": analysis_text}

    def prepare_skill_specific_briefing(self, skill_name: str,
                                       context: str) -> str:
        """
        Prepare a specific skill-based analysis.

        Args:
            skill_name: Name of the strategy skill to use
            context: Meeting/business context for the analysis

        Returns:
            Analysis output using the specific skill framework
        """
        skill_prompts = {
            "situation-assessment":
            """Conduct a situation assessment that:
1. Frames the assessment question
2. Builds a MECE current-state view
3. Identifies momentum signals
4. Highlights strategic issues
5. Lists open questions

Use a fact-based approach and separate facts from interpretations.""",

            "competitive-intel": """Analyze competitive intelligence:
1. Map key competitors and their positions
2. Model likely competitor moves
3. Identify competitive threats and opportunities
4. Assess competitive advantages
5. Recommend competitive responses""",

            "growth-barriers": """Identify growth barriers:
1. Analyze current growth trajectory
2. Diagnose what's constraining growth
3. Distinguish between barriers and headwinds
4. Prioritize barriers by impact
5. Recommend targeted interventions""",

            "business-case-builder": """Build a financial business case:
1. Define the investment/initiative
2. Create base case, downside, and upside scenarios
3. Calculate NPV and key metrics for each scenario
4. Identify key value drivers
5. Highlight risks and sensitivities""",

            "strategic-options": """Generate and compare strategic options:
1. Define the strategic question
2. Generate 3-4 distinct options
3. Evaluate each against key criteria
4. Identify tradeoffs
5. Recommend a pathway forward""",

            "risk-and-mitigation": """Build a strategic risk register:
1. Identify key strategic risks
2. Assess probability and impact
3. Evaluate current mitigation
4. Recommend additional controls
5. Establish monitoring approach""",

            "market-mapping": """Conduct market mapping:
1. Define market boundaries
2. Size total market opportunity
3. Segment the market
4. Identify underserved segments
5. Map market dynamics and trends""",
        }

        prompt = skill_prompts.get(
            skill_name,
            f"Conduct a {skill_name} analysis for the following context.")

        full_prompt = f"""{prompt}

Business Context:
{context}

Provide structured analysis that is executive-ready and actionable."""

        response = client.messages.create(
            model=MODEL,
            max_tokens=2048,
            messages=[{
                "role": "user",
                "content": full_prompt
            }]
        )

        return response.content[0].text

    def synthesize_briefing(self, analyses: Dict[str, str],
                           meeting_context: str) -> str:
        """
        Synthesize multiple skill analyses into a unified briefing.

        Args:
            analyses: Dictionary of skill_name -> analysis_output
            meeting_context: Original meeting context

        Returns:
            Synthesized executive briefing
        """
        analyses_text = "\n\n".join([
            f"## {skill}\n{analysis}"
            for skill, analysis in analyses.items()
        ])

        synthesis_prompt = f"""Synthesize the following strategy skill analyses into a unified,
executive-ready briefing for a strategic meeting.

Meeting Context:
{meeting_context}

Individual Analyses:
{analyses_text}

Create a cohesive briefing that:
1. Opens with an executive summary of key findings
2. Integrates insights across analyses into unified themes
3. Highlights critical insights and implications
4. Identifies key decisions and next steps
5. Provides a recommended pathway forward
6. Notes key risks and assumptions

Format as a professional executive briefing with clear sections."""

        response = client.messages.create(
            model=MODEL,
            max_tokens=3000,
            messages=[{
                "role": "user",
                "content": synthesis_prompt
            }]
        )

        return response.content[0].text

    def prepare_comprehensive_briefing(self, meeting_context: str,
                                      skills_to_use: Optional[List[str]] = None
                                      ) -> str:
        """
        Prepare a comprehensive briefing using multiple skills.

        Args:
            meeting_context: Description of the meeting and requirements
            skills_to_use: Optional list of specific skills to use

        Returns:
            Comprehensive executive briefing
        """
        print("\n" + "=" * 70)
        print("MEETING BRIEFING PREPARATION")
        print("=" * 70)

        # Step 1: Analyze meeting type and recommend skills
        print("\nStep 1: Analyzing meeting context...")
        analysis = self.analyze_meeting_type(meeting_context)
        print("✓ Meeting analysis complete")

        # If skills not specified, use default set
        if not skills_to_use:
            skills_to_use = [
                "situation-assessment", "competitive-intel",
                "strategic-options", "business-case-builder",
                "risk-and-mitigation"
            ]

        # Step 2: Conduct skill-specific analyses
        print(f"\nStep 2: Conducting {len(skills_to_use)} skill analyses...")
        analyses = {}
        for i, skill in enumerate(skills_to_use, 1):
            print(f"  [{i}/{len(skills_to_use)}] Running {skill}...")
            analysis_output = self.prepare_skill_specific_briefing(
                skill, meeting_context)
            analyses[skill] = analysis_output
            print(f"    ✓ Complete")

        # Step 3: Synthesize into unified briefing
        print("\nStep 3: Synthesizing analyses into executive briefing...")
        briefing = self.synthesize_briefing(analyses, meeting_context)
        print("✓ Briefing synthesis complete")

        return briefing


def main():
    """Main entry point for briefing orchestrator."""
    orchestrator = BriefingOrchestrator()

    # Example meeting context
    meeting_context = """
    Executive Strategy Review

    Company: TechCorp (B2B SaaS)
    Situation: Revenue growth has slowed from 40% to 25% YoY despite increased marketing spend.

    Meeting Goal: Determine if current strategy is working or if pivots are needed

    Key Context:
    - Main product is workflow automation software
    - Serves 3 verticals: Manufacturing, Logistics, Retail
    - Recent competitor entry in logistics (best margin segment)
    - Team asking for significant R&D investment in AI features
    - Board meeting in 3 weeks

    Required Decision: Should we maintain current strategy, pivot to adjacent markets,
    invest in product innovation, or acquire to accelerate growth?
    """

    # Prepare briefing
    briefing = orchestrator.prepare_comprehensive_briefing(meeting_context)

    print("\n" + "=" * 70)
    print("EXECUTIVE BRIEFING")
    print("=" * 70)
    print(briefing)
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
