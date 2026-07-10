#!/usr/bin/env python3
"""
Example Usage of Meeting Briefing Agent

Demonstrates how to use the agent for different meeting scenarios.
"""

from briefing_orchestrator import BriefingOrchestrator


def example_board_strategy_meeting():
    """Example: Board strategy meeting for a SaaS company."""
    print("\n" + "=" * 80)
    print("EXAMPLE 1: BOARD STRATEGY MEETING")
    print("=" * 80)

    meeting_context = """
    BOARD STRATEGY REVIEW MEETING

    Company: CloudSync (B2B SaaS - Workflow Automation)
    Meeting Date: Next Monday (3 weeks before board meeting)
    Attendees: CEO, CFO, Board Members

    Current Situation:
    - Annual Revenue: $52M
    - YoY Growth: 25% (down from 40% in prior year)
    - Gross Margin: 78%
    - 3 Vertical Markets: Manufacturing (45%), Logistics (35%), Retail (20%)
    - 80 enterprise customers across 3 verticals
    - 150 person company

    Key Context:
    - Competitor (TechFlow) entered logistics market 6 months ago
    - TechFlow targeting our top 5 logistics customers
    - Logistics segment historically highest margin (82%)
    - Product team requesting $3M investment in AI features
    - CFO concerned about path to profitability
    - Market size expanding but competition intensifying

    Meeting Goal:
    Determine strategic direction for next 3 years:
    - Double down on existing strategy?
    - Pivot to new markets?
    - Invest heavily in innovation?
    - Pursue acquisition/partnership?

    Board Decision Needed: Strategic recommendation + investment plan
    """

    orchestrator = BriefingOrchestrator()
    skills_to_use = [
        "situation-assessment",
        "competitive-intel",
        "growth-barriers",
        "strategic-options",
        "business-case-builder",
        "risk-and-mitigation"
    ]

    briefing = orchestrator.prepare_comprehensive_briefing(
        meeting_context, skills_to_use)

    print(briefing)
    return briefing


def example_operational_review():
    """Example: Operational review meeting."""
    print("\n" + "=" * 80)
    print("EXAMPLE 2: OPERATIONAL REVIEW")
    print("=" * 80)

    meeting_context = """
    Q3 OPERATIONAL REVIEW

    Division: Enterprise Sales
    Meeting: Quarterly business review with VP Sales and CFO
    Current Quarter: Q3 (8 weeks completed)

    Performance Summary:
    - Target: $15M bookings (on track)
    - Sales pipeline: $45M (3x coverage)
    - Win rate: 28% (down from 32% last year)
    - Sales cycle: 4.2 months (increasing)
    - Churn: 8% (up from 6%)

    Key Issues:
    - Top performer (Sarah, $2M quota owner) considering leaving
    - Comp plan under pressure from finance
    - Competitive loss rate at 35% in key segment
    - New product launch delayed by 4 weeks
    - Two new reps underperforming targets

    Meeting Objectives:
    1. Understand root causes of metrics deterioration
    2. Decide on compensation/incentive adjustments
    3. Plan competitive response
    4. Prioritize sales process improvements
    5. Address talent retention risk

    Audience: VP Sales, CFO, Chief People Officer
    Decision: Sales strategy and resource allocation for Q4
    """

    orchestrator = BriefingOrchestrator()
    skills_to_use = [
        "situation-assessment",
        "growth-barriers",
        "competitive-intel",
        "initiative-prioritizer",
        "risk-and-mitigation"
    ]

    briefing = orchestrator.prepare_comprehensive_briefing(
        meeting_context, skills_to_use)

    print(briefing)
    return briefing


def example_portfolio_review():
    """Example: Portfolio review meeting."""
    print("\n" + "=" * 80)
    print("EXAMPLE 3: PORTFOLIO REVIEW")
    print("=" * 80)

    meeting_context = """
    INVESTMENT COMMITTEE - PORTFOLIO REVIEW

    Company: Innovation Corp (Holding Company)
    Meeting: Portfolio Rebalancing Quarterly Meeting

    Current Portfolio (3 assets, $250M AUM):

    Asset 1: TechVentures (45% allocation, $112.5M)
    - Cybersecurity software, $180M revenue, 22% growth
    - 8 institutional customers, expanding government sales
    - Valuation: 8x revenue
    - Performance: Strong but competitive intensity increasing

    Asset 2: RetailTech (35% allocation, $87.5M)
    - Point of sale system for SMB retail, $45M revenue, 8% growth
    - 2000+ SMB customers, SaaS model
    - Margin compression due to increased support costs
    - Valuation: 3.5x revenue
    - Performance: Struggling, market shift to cloud-native players

    Asset 3: DataServices (20% allocation, $50M)
    - Data analytics for manufacturing, $25M revenue, 35% growth
    - 12 enterprise customers, strong product-market fit
    - Early stage, high burn rate
    - Valuation: 10x revenue
    - Performance: High growth but path to profitability unclear

    IC Decision Needed:
    1. Rebalance allocation across 3 assets?
    2. Add new asset or exit underperformer?
    3. Define return targets and success metrics?
    4. Plan exit strategy for each asset?

    Meeting Attendees: 5 investment committee members, 3 asset CEOs
    """

    orchestrator = BriefingOrchestrator()
    skills_to_use = [
        "situation-assessment",
        "portfolio-review",
        "business-case-builder",
        "risk-and-mitigation",
        "value-realization"
    ]

    briefing = orchestrator.prepare_comprehensive_briefing(
        meeting_context, skills_to_use)

    print(briefing)
    return briefing


def example_market_expansion():
    """Example: Market expansion strategy meeting."""
    print("\n" + "=" * 80)
    print("EXAMPLE 4: MARKET EXPANSION STRATEGY")
    print("=" * 80)

    meeting_context = """
    INTERNATIONAL EXPANSION STRATEGY SESSION

    Company: GlobeCommerce (E-commerce Platform)
    Current: US-only, $200M revenue

    Expansion Opportunity:
    The company is considering entering European market. Initial analysis suggests:

    Market Opportunity:
    - European e-commerce market: $1.2T (vs US: $1.0T)
    - CAGR: 12% (slightly lower than US 15%)
    - Top markets: Germany, France, UK, Italy, Spain
    - SMB penetration: 35% (vs US 48%)

    Competitive Landscape:
    - Incumbent: Shopify EU (40% market share)
    - Strong regional players in each country
    - Regulatory complexity (GDPR, VAT, payment regulations)
    - Local payment preferences vary significantly

    Company Capabilities:
    - Technology platform: Strong
    - Customer support: Currently US-centric
    - Payments: US-only
    - Regulatory expertise: Limited
    - Financing: $50M available

    Strategic Options Under Consideration:
    1. Greenfield expansion (hire team, build locally)
    2. Partner with regional player (acquisition or JV)
    3. Acquire existing European player
    4. Focus on English-speaking markets first (UK, Ireland)
    5. Delay expansion, focus on US market deepening

    Meeting Objective:
    Select market entry strategy and commit to investment plan
    Attendees: CEO, CFO, Head of Product, Board Members
    """

    orchestrator = BriefingOrchestrator()
    skills_to_use = [
        "market-mapping",
        "strategic-options",
        "competitive-intel",
        "business-case-builder",
        "operating-model-design",
        "risk-and-mitigation"
    ]

    briefing = orchestrator.prepare_comprehensive_briefing(
        meeting_context, skills_to_use)

    print(briefing)
    return briefing


def main():
    """Run examples."""
    print("\n" + "=" * 80)
    print("MEETING BRIEFING AGENT - USAGE EXAMPLES")
    print("=" * 80)
    print("\nThese examples demonstrate the agent's ability to prepare comprehensive")
    print("briefings for different strategic meetings using relevant consulting skills.")
    print("\nSelect which example to run:")
    print("1. Board Strategy Meeting (SaaS growth challenge)")
    print("2. Operational Review (Sales performance)")
    print("3. Portfolio Review (Investment committee)")
    print("4. Market Expansion (International strategy)")
    print("5. Run All Examples")
    print("0. Exit")

    choice = input("\nEnter your choice (0-5): ").strip()

    if choice == "1":
        example_board_strategy_meeting()
    elif choice == "2":
        example_operational_review()
    elif choice == "3":
        example_portfolio_review()
    elif choice == "4":
        example_market_expansion()
    elif choice == "5":
        example_board_strategy_meeting()
        example_operational_review()
        example_portfolio_review()
        example_market_expansion()
    elif choice == "0":
        print("Exiting.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
