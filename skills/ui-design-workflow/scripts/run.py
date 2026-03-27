#!/usr/bin/env python3
"""
UI Design Generator
Generates interactive HTML/CSS prototypes for UI components and layouts.
"""

import sys
import json
from pathlib import Path

def generate_component_library():
    """Generate a basic component library template"""
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UI Component Library</title>
    <style>
        :root {
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --text-primary: #1f2937;
            --text-secondary: #6b7280;
            --border: #e5e7eb;
            --surface: #ffffff;
            --background: #f9fafb;
        }
        
        @media (prefers-color-scheme: dark) {
            :root {
                --primary: #3b82f6;
                --primary-hover: #60a5fa;
                --text-primary: #f9fafb;
                --text-secondary: #d1d5db;
                --border: #374151;
                --surface: #1f2937;
                --background: #111827;
            }
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: var(--background);
            color: var(--text-primary);
            padding: 40px 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        h1 {
            font-size: 32px;
            margin-bottom: 8px;
        }
        
        .subtitle {
            color: var(--text-secondary);
            margin-bottom: 40px;
        }
        
        .section {
            margin-bottom: 48px;
        }
        
        .section-title {
            font-size: 20px;
            margin-bottom: 20px;
            padding-bottom: 8px;
            border-bottom: 2px solid var(--border);
        }
        
        .component-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }
        
        .component-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
        }
        
        .btn {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 8px;
            border: none;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .btn-primary {
            background: var(--primary);
            color: white;
        }
        
        .btn-primary:hover {
            background: var(--primary-hover);
            transform: translateY(-1px);
        }
        
        .input {
            width: 100%;
            padding: 10px 12px;
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 14px;
            background: var(--surface);
            color: var(--text-primary);
        }
        
        .card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>UI Component Library</h1>
        <p class="subtitle">Reusable components for your design system</p>
        
        <div class="section">
            <h2 class="section-title">Buttons</h2>
            <div class="component-grid">
                <div class="component-card">
                    <button class="btn btn-primary">Primary Button</button>
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2 class="section-title">Inputs</h2>
            <div class="component-grid">
                <div class="component-card">
                    <input type="text" class="input" placeholder="Enter text...">
                </div>
            </div>
        </div>
        
        <div class="section">
            <h2 class="section-title">Cards</h2>
            <div class="component-grid">
                <div class="card">
                    <h3 style="margin-bottom: 8px;">Card Title</h3>
                    <p style="color: var(--text-secondary); font-size: 14px;">This is a card component with content inside.</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    output_path = Path("ui-components.html")
    output_path.write_text(html)
    print(f"✓ Generated component library: {output_path}")
    return str(output_path)

if __name__ == "__main__":
    try:
        output_file = generate_component_library()
        print(f"\nOpen {output_file} in a browser to view the components.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
