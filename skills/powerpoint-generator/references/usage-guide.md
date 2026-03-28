# PowerPoint Generator - Usage Guide

## Overview

This skill creates clean, professional PowerPoint presentations from structured content. It handles formatting, styling, and layout automatically so you can focus on content.

## When to Use This Skill

- User asks to "create a presentation" or "make slides"
- Converting meeting notes or transcripts to a deck
- Building pitch decks, training materials, or reports
- Any request involving PowerPoint, PPTX, or slides

## Installation Requirement

The script requires `python-pptx`. If not installed:
```bash
pip install python-pptx
```

## Workflow

### Step 1: Gather Content

Ask the user for:
- Presentation title and optional subtitle
- Main topics or sections to cover
- Key points for each section
- Any specific slide requirements

If working from a transcript, extract:
- Key decisions → becomes slides
- Action items → becomes slides
- Main discussion topics → becomes section headers

### Step 2: Structure the Content

Organize into a JSON structure:

```json
{
  "title": "Q4 Product Roadmap",
  "subtitle": "Engineering Review",
  "author": "Product Team",
  "output_file": "q4-roadmap.pptx",
  "slides": [
    {
      "type": "section",
      "title": "Overview"
    },
    {
      "type": "content",
      "title": "Key Objectives",
      "content": [
        "Launch mobile app by October 15",
        "Improve API response time by 40%",
        "Ship 3 major feature updates"
      ]
    },
    {
      "type": "content",
      "title": "Timeline",
      "content": [
        "October: Mobile app launch",
        "November: Performance optimization",
        "December: Feature releases"
      ]
    }
  ]
}
```

### Step 3: Write JSON to File

Save the structure to a `.json` file in the workspace:

```python
import json
data = { ... }
with open('presentation_data.json', 'w') as f:
    json.dump(data, indent=2)
```

### Step 4: Run the Script

Execute via `run_skill` or directly:

```bash
python3 ~/.pulse/skills/powerpoint-generator/scripts/run.py presentation_data.json
```

Or pipe JSON directly:
```bash
echo '{"title":"Test","slides":[]}' | python3 script.py
```

### Step 5: Deliver Result

Tell the user:
- Where the PPTX file was saved
- How many slides were created
- Offer to adjust content or styling if needed

## Slide Types

### Title Slide (automatic)
- Uses `title`, `subtitle`, and `author` from root object
- Always created as the first slide
- Large, bold formatting

### Section Header
```json
{
  "type": "section",
  "title": "Section Name"
}
```
- Large text, used to divide presentation into parts
- No bullets or body content

### Content Slide
```json
{
  "type": "content",
  "title": "Slide Title",
  "content": [
    "First bullet point",
    "Second bullet point",
    "Third bullet point"
  ]
}
```
- Standard slide with title and bullets
- Content can be array of strings or single string
- Automatically formatted with consistent spacing

## Design Principles

The script applies professional styling automatically:
- **Typography**: SF Pro-style system fonts, clear hierarchy
- **Colors**: Neutral grays (no garish colors)
- **Spacing**: Generous whitespace, consistent padding
- **Bullets**: Clean, readable, not overcrowded
- **Sizes**: Title 32pt, body 18pt, readable from distance

## Best Practices

### Content Density
- **3-5 bullets per slide** (maximum)
- **5-7 words per bullet** (guideline)
- Split dense content into multiple slides

### Slide Count
- **10-15 slides** for a 10-minute presentation
- **20-30 slides** for a 30-minute presentation
- One key idea per slide

### Text Guidelines
- Use sentence fragments, not full sentences
- Start bullets with action verbs when possible
- Avoid jargon unless audience-appropriate
- Keep titles under 6 words

### Structure Pattern
```
1. Title slide
2. Overview/agenda (optional)
3. Section header
4. Content slides (3-5)
5. Section header
6. Content slides (3-5)
7. Closing slide (next steps, Q&A, contact)
```

## Example: Meeting Transcript to Slides

**User request**: "Turn today's standup into a presentation"

**Your process**:
1. Read the transcript
2. Extract: key updates, blockers, action items
3. Structure:
   - Title: "Daily Standup Summary - [Date]"
   - Section: "Updates"
   - Slides: one per person with their updates
   - Section: "Action Items"
   - Slide: list of todos with owners
4. Generate JSON, run script, deliver file

## Example: Topic-Based Deck

**User request**: "Create a presentation about our new API"

**Your process**:
1. Ask what to cover (or infer from context)
2. Structure:
   - Title: "API v2.0 Overview"
   - Slides: What's new, Key features, Usage examples, Migration guide
3. Generate and run

## Customization

Users can request:
- More slides on a specific topic → add content slides
- Different organization → reorder the slides array
- Less dense content → split bullets across multiple slides

For advanced styling (themes, images, charts), note that the current
script focuses on text content. Suggest manual refinement in PowerPoint
or Keynote after generation.

## Output Location

By default, saves to `presentation.pptx` in the workspace directory.
Set `output_file` in JSON to control the name and path.

## Troubleshooting

**"python-pptx not installed"**
→ Run `pip install python-pptx` in the workspace

**Script fails with JSON error**
→ Validate JSON structure (use json.dumps to ensure valid format)

**Slides look empty**
→ Check that `content` array has items and isn't empty

**Want different styling**
→ Current version uses fixed professional styling; manual refinement
   in PowerPoint needed for custom themes

## Future Enhancements

Potential additions for future versions:
- Image/logo insertion
- Chart generation from data
- Multiple theme options (light/dark, colorful/minimal)
- Speaker notes generation
- Table support for data-heavy slides
