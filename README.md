# Meeting Briefing Agent

An intelligent agent system that prepares executive meeting briefings by leveraging 21 strategy consulting skills. The agent analyzes meeting context and uses relevant analytical frameworks to synthesize data-driven briefings.

## Overview

The Meeting Briefing Agent is built on two complementary components:

1. **meeting_briefing_agent.py** — Interactive conversational agent for exploring meeting briefing needs
2. **briefing_orchestrator.py** — Automated orchestrator that coordinates multiple strategy skills

## Architecture

### Strategy Skills Framework

The system integrates 21 consulting skills organized across 6 domains:

**Diagnosis & Framing**
- `/situation-assessment` — Current state analysis
- `/growth-barriers` — Identifies growth constraints  
- `/assumption-audit` — Tests strategic assumptions

**Market & Competitive Intelligence**
- `/market-mapping` — Market sizing and segmentation
- `/competitive-intel` — Competitive positioning
- `/customer-segmentation` — Customer need-based segments
- `/profit-pool-analysis` — Profit location and capture

**Strategic Choice & Economics**
- `/strategic-options` — Option generation and comparison
- `/business-case-builder` — Financial quantification
- `/portfolio-review` — Portfolio optimization
- `/pricing-strategy` — Pricing diagnostics

**Operating Model & Execution**
- `/initiative-prioritizer` — Impact-based prioritization
- `/operating-model-design` — Capability and decision structure
- `/transformation-roadmap` — Sequenced execution planning

**Risk, Performance & Value Governance**
- `/risk-and-mitigation` — Risk identification and control
- `/kpi-architect` — Performance measurement system
- `/war-gaming` — Strategy stress testing
- `/value-realization` — Value tracking framework

**Alignment & Executive Communication**
- `/decision-memo` — Executive decision documentation
- `/narrative-builder` — Strategic storytelling
- `/stakeholder-alignment` — Stakeholder mapping

## Installation

### Requirements
- Python 3.8+
- Anthropic API key

### Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set your API key
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Usage

### Option 1: Interactive Meeting Briefing Agent

Start an interactive conversation to explore meeting briefing needs:

```bash
python meeting_briefing_agent.py
```

The agent will:
1. Ask about your meeting context and objectives
2. Recommend relevant strategy skills
3. Guide data collection
4. Synthesize findings into a briefing

**Example interaction:**
```
Agent: Welcome! Tell me about the upcoming meeting you need to prepare for.

You: We have a board meeting next week. Revenue growth is slowing and we need to decide on our strategy.

Agent: I understand. Let me help you prepare a comprehensive briefing. 
       I recommend we start with a situation assessment...
```

### Option 2: Automated Briefing Orchestrator

Run the orchestrator for automated multi-skill analysis:

```bash
python briefing_orchestrator.py
```

This executes a complete workflow:
1. Analyzes meeting context
2. Selects optimal skills for analysis
3. Conducts parallel skill analyses  
4. Synthesizes into unified briefing

### Option 3: Command-Line Meeting Context

Prepare a briefing from command-line context:

```bash
python meeting_briefing_agent.py "We have a board meeting to discuss acquisition strategy for expanding into European markets. Current revenue is $50M, 30% growth rate, with 3 potential targets identified."
```

## How It Works

### Process Flow

```
Meeting Context
    ↓
[Meeting Analysis]
    ↓
Recommended Skills
    ↓
[Parallel Skill Analysis]
    ├─ Situation Assessment
    ├─ Competitive Intelligence
    ├─ Strategic Options
    ├─ Business Case
    └─ Risk Analysis
    ↓
[Synthesis Engine]
    ↓
Executive Briefing
```

### Key Components

#### Meeting Briefing Agent
- **Interactive mode** for exploratory discussions
- **Multi-turn conversation** with context awareness
- **Skill recommendation** based on meeting type
- **Real-time guidance** on data collection

#### Briefing Orchestrator
- **Automated skill routing** based on meeting context
- **Parallel analysis** across multiple frameworks
- **Structured synthesis** into unified briefing
- **Executive-ready formatting**

## Example: Board Strategy Meeting

**Meeting Context:**
- Company: SaaS startup, $50M revenue, 30% YoY growth
- Challenge: Growth slowing, competitor entering key segment
- Question: Should we pivot strategy, invest in innovation, or pursue acquisition?
- Audience: Board + C-suite

**Orchestrator Workflow:**

1. **Situation Assessment** → Current position, growth drivers, competitive threats
2. **Competitive Intelligence** → Competitor positioning, likely moves, market trends
3. **Growth Barriers** → Root causes of growth deceleration
4. **Strategic Options** → 3-4 distinct strategic pathways
5. **Business Case Builder** → Financial models for each option
6. **Risk & Mitigation** → Key risks, mitigation strategies

**Output:** Comprehensive briefing with executive summary, strategic options analysis, financial comparisons, and recommended path forward with key next steps.

## Development Guide

### Adding Custom Skills

To integrate additional skills:

1. Add skill definition to `STRATEGY_SKILLS` dict
2. Add skill-specific prompt to `skill_prompts` dict
3. Update domain organization

```python
STRATEGY_SKILLS["new_domain"] = {
    "new-skill": "Skill description"
}

skill_prompts["new-skill"] = """Specific analysis framework..."""
```

### Customizing Analysis

Modify the skill-specific prompts to change analysis depth:

```python
def prepare_skill_specific_briefing(self, skill_name: str, context: str) -> str:
    skill_prompts["your-skill"] = """Your custom analysis framework..."""
```

### Extending Synthesis

Enhance the briefing synthesis by modifying the synthesis_prompt:

```python
def synthesize_briefing(self, analyses: Dict[str, str], meeting_context: str) -> str:
    synthesis_prompt = """Custom synthesis approach..."""
```

## API Reference

### BriefingOrchestrator

```python
orchestrator = BriefingOrchestrator()

# Analyze meeting and get skill recommendations
analysis = orchestrator.analyze_meeting_type(meeting_context: str) -> Dict

# Run single skill analysis
output = orchestrator.prepare_skill_specific_briefing(
    skill_name: str, 
    context: str
) -> str

# Synthesize multiple analyses
briefing = orchestrator.synthesize_briefing(
    analyses: Dict[str, str],
    meeting_context: str
) -> str

# Complete workflow
full_briefing = orchestrator.prepare_comprehensive_briefing(
    meeting_context: str,
    skills_to_use: Optional[List[str]] = None
) -> str
```

## Best Practices

### For Interactive Mode
- Start with high-level meeting objectives
- Let the agent guide you through data collection
- Build briefing collaboratively
- Refine analyses through follow-up prompts

### For Orchestrator Mode
- Provide rich meeting context
- Include business metrics and background
- Specify key decisions needed
- Allow parallel processing to complete

### For Best Results
- Be specific about meeting audience and goals
- Include relevant financial/market data
- Clarify key decisions to be made
- Allow the agent to recommend skills rather than pre-selecting

## Troubleshooting

### Agent Not Making Recommendations
- Provide more detailed meeting context
- Specify what decisions need to be made
- Include current business metrics

### Synthesis Feels Disconnected
- Ensure meeting context is clear to agent
- Ask agent to explicitly map connections
- Request agent to highlight key themes

### Analysis Too Deep/Shallow
- Adjust max_tokens in agent calls
- Provide more specific constraints
- Request executive summary vs. detailed analysis

## Configuration

Default settings:
- Model: `claude-opus-4-8`
- Max tokens per response: 2048 (agent), 3000 (orchestrator)
- Default skills in orchestrator: 5 core skills

Customize in code:

```python
MODEL = "claude-opus-4-8"  # Change model
max_tokens = 2048  # Adjust response length
skills_to_use = [...]  # Specify skills
```

## Architecture Decisions

### Why Claude?
- Superior strategy analysis and reasoning
- Multi-turn conversation capability
- Structured output formatting
- Integration with consulting frameworks

### Why This Structure?
- **Agent mode** for collaborative exploration
- **Orchestrator mode** for deterministic multi-skill execution
- **Separation of concerns** for flexibility and extensibility

### Skill Organization
Organized by strategic decision-making phase:
1. Diagnose current situation
2. Understand market/competition
3. Generate and evaluate options
4. Quantify economics
5. Manage risks
6. Align stakeholders

## Future Enhancements

- Integration with real data sources (market data, financials)
- Export briefings to PowerPoint/PDF
- Template-based briefing generation
- Real-time data updates
- Stakeholder-specific briefing variants
- Historical briefing tracking and versioning

## License

Internal use only.

## Support

For questions or issues, contact the strategy technology team.
