# PowerPoint Generator - Complete Examples

## Example 1: Simple Project Update

**User request**: "Create a quick deck about our Q4 progress"

**JSON structure**:
```json
{
  "title": "Q4 Progress Update",
  "subtitle": "Engineering Team",
  "author": "Ali Khatami",
  "output_file": "q4-progress.pptx",
  "slides": [
    {
      "type": "content",
      "title": "Completed This Quarter",
      "content": [
        "Shipped mobile app v2.0",
        "Reduced API latency by 45%",
        "Onboarded 3 new engineers",
        "Migrated to new infrastructure"
      ]
    },
    {
      "type": "content",
      "title": "Key Metrics",
      "content": [
        "User growth: 23% increase",
        "System uptime: 99.97%",
        "Bug resolution time: down 30%",
        "Customer satisfaction: 4.8/5"
      ]
    },
    {
      "type": "content",
      "title": "Challenges",
      "content": [
        "Database scaling took longer than expected",
        "Two security incidents required immediate attention",
        "Hiring goals not fully met"
      ]
    },
    {
      "type": "content",
      "title": "Next Quarter Priorities",
      "content": [
        "Launch analytics dashboard",
        "Complete security audit",
        "Expand team by 4 people"
      ]
    }
  ]
}
```

## Example 2: Pitch Deck Structure

**User request**: "Help me create a pitch deck for our startup"

**JSON structure**:
```json
{
  "title": "Acme AI",
  "subtitle": "Transforming Customer Support with Intelligence",
  "author": "Seed Round - January 2025",
  "output_file": "acme-pitch.pptx",
  "slides": [
    {
      "type": "content",
      "title": "The Problem",
      "content": [
        "Customer support teams overwhelmed by volume",
        "80% of questions are repetitive",
        "Average response time: 24 hours",
        "Customer frustration leads to churn"
      ]
    },
    {
      "type": "content",
      "title": "Our Solution",
      "content": [
        "AI-powered support agent",
        "Instant responses to common questions",
        "Seamless handoff to humans when needed",
        "Learns from every interaction"
      ]
    },
    {
      "type": "content",
      "title": "Market Opportunity",
      "content": [
        "$25B customer support software market",
        "Growing 18% annually",
        "10M+ support agents worldwide",
        "Early adopters seeing 60% cost savings"
      ]
    },
    {
      "type": "content",
      "title": "Traction",
      "content": [
        "15 paying customers",
        "$120K ARR",
        "500% growth last quarter",
        "Net revenue retention: 140%"
      ]
    },
    {
      "type": "content",
      "title": "Team",
      "content": [
        "CEO: 10 years in enterprise software",
        "CTO: Ex-Google AI researcher",
        "VP Eng: Built teams at Stripe and Twilio"
      ]
    },
    {
      "type": "content",
      "title": "The Ask",
      "content": [
        "Raising $2M seed round",
        "18 month runway",
        "Hiring: 3 engineers, 1 sales lead",
        "Goal: $1M ARR by end of year"
      ]
    }
  ]
}
```

## Example 3: Training Materials

**User request**: "Create training slides for new hires on our git workflow"

**JSON structure**:
```json
{
  "title": "Git Workflow Guide",
  "subtitle": "Engineering Onboarding",
  "author": "Developer Experience Team",
  "output_file": "git-training.pptx",
  "slides": [
    {
      "type": "section",
      "title": "Getting Started"
    },
    {
      "type": "content",
      "title": "Clone and Setup",
      "content": [
        "Clone the repo from GitHub",
        "Run npm install",
        "Copy .env.example to .env",
        "Start dev server with npm run dev"
      ]
    },
    {
      "type": "section",
      "title": "Daily Workflow"
    },
    {
      "type": "content",
      "title": "Creating a Feature",
      "content": [
        "Pull latest from main branch",
        "Create feature branch: feature/description",
        "Make your changes and commit frequently",
        "Push branch and open pull request"
      ]
    },
    {
      "type": "content",
      "title": "Commit Messages",
      "content": [
        "Start with verb: Add, Fix, Update, Remove",
        "Be specific and concise",
        "Reference ticket number if applicable",
        "Example: Fix login timeout issue (#342)"
      ]
    },
    {
      "type": "content",
      "title": "Pull Request Process",
      "content": [
        "Fill out PR template completely",
        "Request 2 reviewers minimum",
        "Address feedback promptly",
        "Merge after approval (squash commits)"
      ]
    },
    {
      "type": "section",
      "title": "Best Practices"
    },
    {
      "type": "content",
      "title": "Do's",
      "content": [
        "Commit early and often",
        "Write tests for new features",
        "Keep PRs under 400 lines",
        "Update documentation"
      ]
    },
    {
      "type": "content",
      "title": "Don'ts",
      "content": [
        "Never commit directly to main",
        "Don't force push shared branches",
        "Avoid mixing unrelated changes",
        "Don't commit secrets or credentials"
      ]
    }
  ]
}
```

## Example 4: Meeting Summary Deck

**Scenario**: Converting a 45-minute product meeting into slides

**JSON structure**:
```json
{
  "title": "Product Meeting Summary",
  "subtitle": "Feature Prioritization - Week of Jan 15",
  "author": "Product Team",
  "output_file": "meeting-summary.pptx",
  "slides": [
    {
      "type": "content",
      "title": "Decisions Made",
      "content": [
        "Move mobile dark mode to Q1",
        "Delay analytics v2 to Q2",
        "Green light on social sharing feature"
      ]
    },
    {
      "type": "section",
      "title": "Action Items"
    },
    {
      "type": "content",
      "title": "Design Team",
      "content": [
        "Sarah: Mock up social sharing UI by Friday",
        "Tom: User research on dark mode preferences",
        "Team: Review analytics feedback from beta users"
      ]
    },
    {
      "type": "content",
      "title": "Engineering Team",
      "content": [
        "Alex: Spike on social sharing backend (2 days)",
        "Jordan: Update Q1 roadmap doc",
        "Maria: Review mobile performance metrics"
      ]
    },
    {
      "type": "content",
      "title": "Open Questions",
      "content": [
        "Do we support all social platforms or start with 2?",
        "What's the minimum viable dark mode scope?",
        "Should analytics v2 be redesigned or enhanced?"
      ]
    },
    {
      "type": "content",
      "title": "Next Meeting",
      "content": [
        "Date: January 22, 10am",
        "Agenda: Review social sharing spike results",
        "Required: Bring competitive analysis",
        "Location: Conference Room B / Zoom"
      ]
    }
  ]
}
```

## Example 5: Data-Driven Report

**User request**: "Create slides showing our Q4 sales performance"

**JSON structure**:
```json
{
  "title": "Q4 Sales Performance",
  "subtitle": "Record Quarter for Revenue",
  "author": "Sales Team",
  "output_file": "q4-sales-report.pptx",
  "slides": [
    {
      "type": "content",
      "title": "Revenue Highlights",
      "content": [
        "Total revenue: $2.4M (+35% vs Q3)",
        "New customers: 47 (+18% vs Q3)",
        "Average deal size: $51K (+12%)",
        "Enterprise deals: 8 (largest: $280K)"
      ]
    },
    {
      "type": "content",
      "title": "Top Performers",
      "content": [
        "Jessica Chen: $680K closed, 12 deals",
        "Marcus Johnson: $520K closed, 15 deals",
        "Priya Patel: $440K closed, 8 deals"
      ]
    },
    {
      "type": "content",
      "title": "By Region",
      "content": [
        "North America: $1.4M (58% of total)",
        "Europe: $720K (30% of total)",
        "APAC: $280K (12% of total)"
      ]
    },
    {
      "type": "content",
      "title": "Product Mix",
      "content": [
        "Enterprise tier: 68% of revenue",
        "Professional tier: 24% of revenue",
        "Starter tier: 8% of revenue"
      ]
    },
    {
      "type": "content",
      "title": "Pipeline for Q1",
      "content": [
        "Qualified opportunities: $4.2M",
        "Expected close rate: 32%",
        "Projected Q1 revenue: $1.35M",
        "Top vertical: FinTech (38% of pipeline)"
      ]
    },
    {
      "type": "content",
      "title": "Challenges & Learnings",
      "content": [
        "Deal cycles 15% longer than forecast",
        "Competition intensified in mid-market",
        "Need better technical pre-sales support",
        "Contract negotiation bottleneck identified"
      ]
    }
  ]
}
```

## Code Template for Quick Generation

Use this Python snippet to quickly generate presentations:

```python
import json

# Define your presentation structure
deck = {
    "title": "Your Title Here",
    "subtitle": "Subtitle or date",
    "author": "Your name",
    "output_file": "output.pptx",
    "slides": [
        {
            "type": "content",
            "title": "Slide Title",
            "content": [
                "Point one",
                "Point two",
                "Point three"
            ]
        }
        # Add more slides...
    ]
}

# Write to file
with open('deck_data.json', 'w') as f:
    json.dump(deck, f, indent=2)

print("✓ JSON saved to deck_data.json")
print("Run: python3 ~/.pulse/skills/powerpoint-generator/scripts/run.py deck_data.json")
```

## Tips for Better Presentations

1. **Start with structure**: Plan slide titles before writing content
2. **One idea per slide**: Don't cram multiple concepts together
3. **Use section breaks**: Help audience follow along in longer decks
4. **Vary slide types**: Mix content slides with section headers
5. **End strong**: Final slide should have clear next steps or CTA
