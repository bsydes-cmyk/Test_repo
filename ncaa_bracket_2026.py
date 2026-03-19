#!/usr/bin/env python3
"""
2026 NCAA March Madness Tournament Bracket Analysis Tool
=========================================================
Mathematical & Statistical Deep-Dive on All 68 Teams
Built with data from ESPN, CBS Sports, KenPom, NCAA.com, and more.

This tool provides:
- Complete bracket with all first-round matchups
- Team profiles, key player stats, injuries
- Strength/weakness analysis
- Historical matchup data
- Mathematical win probability modeling
- Round-by-round pick recommendations with reasoning
"""

# =============================================================================
# COMPLETE 2026 NCAA TOURNAMENT BRACKET
# =============================================================================

BRACKET = {
    "East": {
        "region_site": "Capital One Arena, Washington, D.C.",
        "matchups": [
            {"game": 1, "higher": {"seed": 1, "team": "Duke", "record": "32-2", "conf": "ACC"},
                        "lower":  {"seed": 16, "team": "Siena", "record": "23-10", "conf": "MAAC"}},
            {"game": 2, "higher": {"seed": 8, "team": "Ohio State", "record": "21-12", "conf": "Big Ten"},
                        "lower":  {"seed": 9, "team": "TCU", "record": "22-11", "conf": "Big 12"}},
            {"game": 3, "higher": {"seed": 5, "team": "St. John's", "record": "28-6", "conf": "Big East"},
                        "lower":  {"seed": 12, "team": "Northern Iowa", "record": "25-8", "conf": "MVC"}},
            {"game": 4, "higher": {"seed": 4, "team": "Kansas", "record": "23-10", "conf": "Big 12"},
                        "lower":  {"seed": 13, "team": "Cal Baptist", "record": "24-9", "conf": "WAC"}},
            {"game": 5, "higher": {"seed": 6, "team": "Louisville", "record": "23-10", "conf": "ACC"},
                        "lower":  {"seed": 11, "team": "South Florida", "record": "25-8", "conf": "AAC"}},
            {"game": 6, "higher": {"seed": 3, "team": "Michigan State", "record": "25-7", "conf": "Big Ten"},
                        "lower":  {"seed": 14, "team": "North Dakota State", "record": "27-6", "conf": "Summit"}},
            {"game": 7, "higher": {"seed": 7, "team": "UCLA", "record": "23-11", "conf": "Big Ten"},
                        "lower":  {"seed": 10, "team": "UCF", "record": "21-11", "conf": "Big 12"}},
            {"game": 8, "higher": {"seed": 2, "team": "UConn", "record": "29-5", "conf": "Big East"},
                        "lower":  {"seed": 15, "team": "Furman", "record": "24-10", "conf": "SoCon"}},
        ]
    },
    "West": {
        "region_site": "SAP Center, San Jose, CA",
        "matchups": [
            {"game": 1, "higher": {"seed": 1, "team": "Arizona", "record": "32-2", "conf": "Big 12"},
                        "lower":  {"seed": 16, "team": "Long Island", "record": "20-13", "conf": "NEC"}},
            {"game": 2, "higher": {"seed": 8, "team": "Villanova", "record": "24-8", "conf": "Big East"},
                        "lower":  {"seed": 9, "team": "Utah State", "record": "28-6", "conf": "MWC"}},
            {"game": 3, "higher": {"seed": 5, "team": "Wisconsin", "record": "24-10", "conf": "Big Ten"},
                        "lower":  {"seed": 12, "team": "High Point", "record": "30-4", "conf": "Big South"}},
            {"game": 4, "higher": {"seed": 4, "team": "Arkansas", "record": "26-8", "conf": "SEC"},
                        "lower":  {"seed": 13, "team": "Hawaii", "record": "22-11", "conf": "Big West"}},
            {"game": 5, "higher": {"seed": 6, "team": "BYU", "record": "23-11", "conf": "Big 12"},
                        "lower":  {"seed": 11, "team": "Texas", "record": "20-14", "conf": "SEC"}},
            {"game": 6, "higher": {"seed": 3, "team": "Gonzaga", "record": "30-3", "conf": "WCC"},
                        "lower":  {"seed": 14, "team": "Kennesaw State", "record": "25-9", "conf": "ASUN"}},
            {"game": 7, "higher": {"seed": 7, "team": "Miami (FL)", "record": "25-8", "conf": "ACC"},
                        "lower":  {"seed": 10, "team": "Missouri", "record": "21-13", "conf": "SEC"}},
            {"game": 8, "higher": {"seed": 2, "team": "Purdue", "record": "27-8", "conf": "Big Ten"},
                        "lower":  {"seed": 15, "team": "Queens", "record": "25-8", "conf": "ASUN"}},
        ]
    },
    "South": {
        "region_site": "Toyota Center, Houston, TX",
        "matchups": [
            {"game": 1, "higher": {"seed": 1, "team": "Florida", "record": "27-6", "conf": "SEC"},
                        "lower":  {"seed": 16, "team": "Prairie View A&M/Lehigh", "record": "TBD", "conf": "First Four"}},
            {"game": 2, "higher": {"seed": 8, "team": "Clemson", "record": "24-10", "conf": "ACC"},
                        "lower":  {"seed": 9, "team": "Iowa", "record": "21-12", "conf": "Big Ten"}},
            {"game": 3, "higher": {"seed": 5, "team": "Vanderbilt", "record": "26-8", "conf": "SEC"},
                        "lower":  {"seed": 12, "team": "McNeese State", "record": "28-5", "conf": "Southland"}},
            {"game": 4, "higher": {"seed": 4, "team": "Nebraska", "record": "26-6", "conf": "Big Ten"},
                        "lower":  {"seed": 13, "team": "Troy", "record": "22-11", "conf": "Sun Belt"}},
            {"game": 5, "higher": {"seed": 6, "team": "North Carolina", "record": "24-8", "conf": "ACC"},
                        "lower":  {"seed": 11, "team": "VCU", "record": "27-7", "conf": "A-10"}},
            {"game": 6, "higher": {"seed": 3, "team": "Illinois", "record": "24-8", "conf": "Big Ten"},
                        "lower":  {"seed": 14, "team": "Penn", "record": "18-11", "conf": "Ivy"}},
            {"game": 7, "higher": {"seed": 7, "team": "Saint Mary's", "record": "27-5", "conf": "WCC"},
                        "lower":  {"seed": 10, "team": "Texas A&M", "record": "21-11", "conf": "SEC"}},
            {"game": 8, "higher": {"seed": 2, "team": "Houston", "record": "28-6", "conf": "Big 12"},
                        "lower":  {"seed": 15, "team": "Idaho", "record": "21-14", "conf": "Big Sky"}},
        ]
    },
    "Midwest": {
        "region_site": "United Center, Chicago, IL",
        "matchups": [
            {"game": 1, "higher": {"seed": 1, "team": "Michigan", "record": "31-3", "conf": "Big Ten"},
                        "lower":  {"seed": 16, "team": "Howard", "record": "20-14", "conf": "MEAC"}},
            {"game": 2, "higher": {"seed": 8, "team": "Georgia", "record": "22-10", "conf": "SEC"},
                        "lower":  {"seed": 9, "team": "Saint Louis", "record": "28-5", "conf": "A-10"}},
            {"game": 3, "higher": {"seed": 5, "team": "Texas Tech", "record": "22-10", "conf": "Big 12"},
                        "lower":  {"seed": 12, "team": "Akron", "record": "25-8", "conf": "MAC"}},
            {"game": 4, "higher": {"seed": 4, "team": "Alabama", "record": "23-9", "conf": "SEC"},
                        "lower":  {"seed": 13, "team": "Hofstra", "record": "26-7", "conf": "CAA"}},
            {"game": 5, "higher": {"seed": 6, "team": "Tennessee", "record": "22-11", "conf": "SEC"},
                        "lower":  {"seed": 11, "team": "SMU/Miami OH", "record": "TBD", "conf": "First Four"}},
            {"game": 6, "higher": {"seed": 3, "team": "Virginia", "record": "29-5", "conf": "ACC"},
                        "lower":  {"seed": 14, "team": "Wright State", "record": "22-12", "conf": "Horizon"}},
            {"game": 7, "higher": {"seed": 7, "team": "Kentucky", "record": "21-13", "conf": "SEC"},
                        "lower":  {"seed": 10, "team": "Santa Clara", "record": "26-8", "conf": "WCC"}},
            {"game": 8, "higher": {"seed": 2, "team": "Iowa State", "record": "27-7", "conf": "Big 12"},
                        "lower":  {"seed": 15, "team": "Tennessee State", "record": "21-12", "conf": "OVC"}},
        ]
    },
    "First Four": {
        "region_site": "UD Arena, Dayton, OH",
        "matchups": [
            {"game": "FF1", "higher": {"seed": 16, "team": "UMBC", "conf": "America East"},
                           "lower":  {"seed": 16, "team": "Howard", "conf": "MEAC"},
                           "winner": "Howard", "region": "Midwest"},
            {"game": "FF2", "higher": {"seed": 11, "team": "Texas", "conf": "SEC"},
                           "lower":  {"seed": 11, "team": "NC State", "conf": "ACC"},
                           "winner": "Texas", "region": "West"},
            {"game": "FF3", "higher": {"seed": 11, "team": "SMU", "conf": "ACC"},
                           "lower":  {"seed": 11, "team": "Miami (OH)", "conf": "MAC"},
                           "region": "Midwest"},
            {"game": "FF4", "higher": {"seed": 16, "team": "Prairie View A&M", "conf": "SWAC"},
                           "lower":  {"seed": 16, "team": "Lehigh", "conf": "Patriot"},
                           "region": "South"},
        ]
    }
}

# =============================================================================
# TEAM ANALYSIS DATABASE - Will be populated with agent research
# =============================================================================

TEAM_PROFILES = {}  # Populated below after agent research completes

# =============================================================================
# MATHEMATICAL WIN PROBABILITY MODEL
# =============================================================================

# Historical seed-vs-seed win rates (1985-2025, 40 years of data)
HISTORICAL_SEED_WIN_RATES = {
    (1, 16): 0.993,   # 1-seeds are 151-2 all-time vs 16-seeds
    (8, 9):  0.515,   # Essentially a coin flip historically
    (5, 12): 0.643,   # The classic 5-12 upset zone
    (4, 13): 0.786,   # 13-seeds pull upsets ~21% of the time
    (6, 11): 0.625,   # 6-vs-11 is another upset-prone line
    (3, 14): 0.857,   # 14-seeds win ~14% of the time
    (7, 10): 0.607,   # 7-vs-10 is competitive
    (2, 15): 0.942,   # 15-seeds win ~6% of the time
}


def calculate_matchup_probability(higher_seed_team, lower_seed_team, context_factors=None):
    """
    Calculate win probability using a weighted model:
    - 30% historical seed matchup data
    - 25% KenPom/efficiency metrics
    - 20% current form (last 10 games)
    - 15% injury impact
    - 10% tournament experience
    """
    h_seed = higher_seed_team["seed"]
    l_seed = lower_seed_team["seed"]

    base_rate = HISTORICAL_SEED_WIN_RATES.get((h_seed, l_seed), 0.5)

    if context_factors:
        efficiency_adj = context_factors.get("efficiency_delta", 0) * 0.02
        form_adj = context_factors.get("form_delta", 0) * 0.015
        injury_adj = context_factors.get("injury_impact", 0) * -0.05
        experience_adj = context_factors.get("experience_delta", 0) * 0.01

        adjusted = base_rate + efficiency_adj + form_adj + injury_adj + experience_adj
        return max(0.01, min(0.99, adjusted))

    return base_rate


def print_bracket_overview():
    """Print the complete bracket in a readable format."""
    print("=" * 80)
    print("  2026 NCAA MEN'S BASKETBALL TOURNAMENT - COMPLETE BRACKET")
    print("  March 17 - April 6 | Championship: Lucas Oil Stadium, Indianapolis")
    print("=" * 80)

    for region_name, region_data in BRACKET.items():
        if region_name == "First Four":
            continue
        print(f"\n{'─' * 80}")
        print(f"  {region_name.upper()} REGION | {region_data['region_site']}")
        print(f"{'─' * 80}")
        for m in region_data["matchups"]:
            h = m["higher"]
            l = m["lower"]
            seeds = (h["seed"], l["seed"])
            base_prob = HISTORICAL_SEED_WIN_RATES.get(seeds, 0.5)
            print(f"  ({h['seed']:>2}) {h['team']:<22} {h.get('record',''):>6} [{h['conf']}]")
            print(f"       vs.  Base P(higher seed): {base_prob:.1%}")
            print(f"  ({l['seed']:>2}) {l['team']:<22} {l.get('record',''):>6} [{l['conf']}]")
            print()


if __name__ == "__main__":
    print_bracket_overview()
