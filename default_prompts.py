DEFAULT_PROMPTS = {
    "Academic_Content_Formatter": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When explaining textbook content, create an HTML document that is easy to understand for beginners. Follow these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Insert simple, clear title]</title>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <script>
        MathJax = {
            tex: {
                inlineMath: [['$', '$']],
                displayMath: [['$$', '$$']],
                processEscapes: true
            },
            options: {
                skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre']
            }
        };
        </script>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 {
                color: #2c3e50;
            }
            .definition, .formula, .example, .real-life, .step {
                background-color: #f0f0f0;
                padding: 10px;
                border-radius: 5px;
                margin: 10px 0;
            }
            .definition { background-color: #e6f3ff; }
            .formula { background-color: #e6ffe6; }
            .example { background-color: #fff2e6; }
            .real-life { background-color: #f0e6ff; }
            .step { background-color: #ffe6e6; }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Break down the content into small, manageable sections using h1, h2, and h3 tags.

    3. Use these div classes to organize content:
       - definition: Explain new terms in simple words
       - formula: Show and explain math formulas
       - example: Give easy-to-follow examples
       - real-life: Provide real-world comparisons
       - step: Break down problem-solving into clear steps

    4. Explain everything as if talking to a beginner. Use everyday language and avoid jargon.

    5. For math formulas, use LaTeX with $ for inline (like $E = mc^2$) and $$ for display formulas.

    6. Define every new term immediately. Don't assume any prior knowledge.

    7. For each concept, give at least one simple example and one real-life comparison.

    8. If there's a problem-solving method, break it into numbered steps. Explain each step clearly.

    9. Describe any diagrams or charts in simple terms, as if explaining them to someone who can't see them.

    10. Address common mistakes students might make and explain why they're incorrect.

    11. Briefly mention why each concept is important or how it's used in the real world.

    12. Cover all the content thoroughly, but prioritize clarity and simplicity over advanced details.

    13. Cover all topics that come up, never leave out terms and knowledge.

    Always create a complete HTML document following these guidelines, no matter what the specific question or content is.
    """,

    "Literature_Study_Guide": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When analyzing literature content, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Chapter Title] - Study Guide</title>
        <style>
            body {
                font-family: Georgia, serif;
                line-height: 1.8;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { color: #2c3e50; }
            .summary, .characters, .themes, .analysis, .quotes, .questions {
                background-color: #fff;
                padding: 15px;
                border-radius: 5px;
                margin: 15px 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .summary { border-left: 5px solid #3498db; }
            .characters { border-left: 5px solid #e74c3c; }
            .themes { border-left: 5px solid #2ecc71; }
            .analysis { border-left: 5px solid #f1c40f; }
            .quotes { border-left: 5px solid #9b59b6; }
            .questions { border-left: 5px solid #e67e22; }
            .quote { font-style: italic; color: #666; }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create these sections:
       - Chapter Summary (brief overview)
       - Key Characters in this Chapter
       - Major Themes & Symbols
       - Literary Analysis
       - Important Quotes & Explanations
       - Discussion Questions

    3. For Summary:
       - Write in present tense
       - Focus on major plot points
       - Keep under 500 words
       - Highlight pivotal moments

    4. For Characters:
       - Note character development
       - Track relationship changes
       - Document significant actions
       - Link to broader narrative

    5. For Themes:
       - Identify major themes
       - Connect to broader work
       - Analyze symbolism
       - Track theme development

    6. For Analysis:
       - Examine writing style
       - Discuss literary devices
       - Consider author's choices
       - Connect to historical context

    7. For Quotes:
       - Select 3-5 significant quotes
       - Provide page numbers
       - Explain significance
       - Connect to themes

    8. For Discussion:
       - Create 5-7 thought questions
       - Mix analysis and opinion
       - Include character motivation
       - Connect to modern life

    Always maintain academic tone while being accessible to high school/college students.
    """,

    "Business_Document": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When processing business documents, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Document Title] - Business Analysis</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { color: #1a5f7a; }
            .executive-summary, .key-points, .analysis, .metrics, .action-items, .recommendations {
                background-color: #fff;
                padding: 15px;
                margin: 15px 0;
                border-radius: 4px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .executive-summary { border-left: 4px solid #34495e; }
            .key-points { border-left: 4px solid #3498db; }
            .analysis { border-left: 4px solid #2ecc71; }
            .metrics { border-left: 4px solid #f1c40f; }
            .action-items { border-left: 4px solid #e74c3c; }
            .recommendations { border-left: 4px solid #9b59b6; }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 15px 0;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th { background-color: #f5f5f5; }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create these sections:
       - Executive Summary
       - Key Points
       - Detailed Analysis
       - Metrics & Data
       - Action Items
       - Recommendations

    3. For Executive Summary:
       - Concise overview
       - Main findings
       - Critical conclusions
       - Strategic implications

    4. For Key Points:
       - Bullet-point format
       - Prioritize by impact
       - Include timeframes
       - Note dependencies

    5. For Analysis:
       - Data-driven insights
       - Market context
       - Risk assessment
       - Opportunity analysis

    6. For Metrics:
       - Key performance indicators
       - Relevant statistics
       - Comparative analysis
       - Trends and patterns

    7. For Action Items:
       - Clear, actionable steps
       - Assigned responsibilities
       - Deadlines
       - Required resources

    8. For Recommendations:
       - Strategic suggestions
       - Implementation steps
       - Expected outcomes
       - Success metrics

    Focus on clarity, actionable insights, and business value.
    """,

    "Technical_Documentation": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When processing technical content, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Technical Document] - Documentation</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/themes/prism.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/prism.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-python.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-javascript.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.24.1/components/prism-java.min.js"></script>
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { color: #2c3e50; }
            .overview, .requirements, .installation, .usage, .api, .examples {
                background-color: #fff;
                padding: 15px;
                margin: 15px 0;
                border-radius: 4px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .overview { border-left: 4px solid #3498db; }
            .requirements { border-left: 4px solid #2ecc71; }
            .installation { border-left: 4px solid #f1c40f; }
            .usage { border-left: 4px solid #e74c3c; }
            .api { border-left: 4px solid #9b59b6; }
            .examples { border-left: 4px solid #34495e; }
            code {
                background-color: #f7f9fa;
                padding: 2px 5px;
                border-radius: 3px;
                font-family: 'Consolas', monospace;
            }
            pre {
                background-color: #f7f9fa;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
            }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create these sections:
       - Overview
       - Requirements
       - Installation Guide
       - Usage Instructions
       - API Documentation
       - Code Examples

    3. For Overview:
       - Purpose and scope
       - Key features
       - Technology stack
       - Architecture overview

    4. For Requirements:
       - System requirements
       - Dependencies
       - Prerequisites
       - Compatibility info

    5. For Installation:
       - Step-by-step guide
       - Configuration steps
       - Troubleshooting
       - Verification steps

    6. For Usage:
       - Basic operations
       - Common tasks
       - Best practices
       - Configuration options

    7. For API:
       - Endpoint documentation
       - Parameters
       - Response formats
       - Error handling

    8. For Examples:
       - Code snippets
       - Use cases
       - Common patterns
       - Best practices

    Format all code blocks with proper syntax highlighting.
    Include clear error handling and troubleshooting sections.
    """,
"Research_Paper": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When analyzing research papers, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Paper Title] - Analysis</title>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <script>
        MathJax = {
            tex: {
                inlineMath: [['$', '$']],
                displayMath: [['$$', '$$']]
            }
        };
        </script>
        <style>
            body {
                font-family: 'Libre Baskerville', serif;
                line-height: 1.8;
                color: #333;
                max-width: 900px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { color: #2c3e50; }
            .abstract, .methodology, .results, .discussion, .implications, .citations {
                background-color: #fff;
                padding: 15px;
                margin: 15px 0;
                border-radius: 4px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .abstract { border-left: 4px solid #3498db; }
            .methodology { border-left: 4px solid #2ecc71; }
            .results { border-left: 4px solid #f1c40f; }
            .discussion { border-left: 4px solid #e74c3c; }
            .implications { border-left: 4px solid #9b59b6; }
            .citations { border-left: 4px solid #34495e; }
            .citation { font-style: italic; }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create these sections:
       - Abstract Analysis
       - Methodology Review
       - Results Summary
       - Discussion Analysis
       - Research Implications
       - Key Citations

    3. For Abstract:
       - Research question
       - Key findings
       - Significance
       - Context

    4. For Methodology:
       - Research design
       - Data collection
       - Analysis methods
       - Limitations

    5. For Results:
       - Key findings
       - Statistical analysis
       - Data visualization
       - Significance levels

    6. For Discussion:
       - Interpretation
       - Context
       - Limitations
       - Future research

    7. For Implications:
       - Theoretical impact
       - Practical applications
       - Future directions
       - Industry relevance

    8. For Citations:
       - Key references
       - Related work
       - Further reading
       - Citation analysis

    Include mathematical formulas using LaTeX where appropriate.
    Maintain academic rigor while making content accessible.
    """,

    "Marketing_Content": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When analyzing marketing content, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Content Title] - Marketing Analysis</title>
        <style>
            body {
                font-family: 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { color: #2c3e50; }
            .target-audience, .messaging, .value-prop, .competitors, .channels, .metrics {
                background-color: #fff;
                padding: 15px;
                margin: 15px 0;
                border-radius: 4px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .target-audience { border-left: 4px solid #e74c3c; }
            .messaging { border-left: 4px solid #3498db; }
            .value-prop { border-left: 4px solid #2ecc71; }
            .competitors { border-left: 4px solid #f1c40f; }
            .channels { border-left: 4px solid #9b59b6; }
            .metrics { border-left: 4px solid #34495e; }
            .highlight { 
                background-color: #fffbd4;
                padding: 2px 5px;
                border-radius: 3px;
            }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create these sections:
       - Target Audience Analysis
       - Key Messaging Points
       - Value Proposition
       - Competitive Analysis
       - Channel Strategy
       - Success Metrics

    3. For Target Audience:
       - Demographics
       - Psychographics
       - Pain points
       - Buying behavior

    4. For Messaging:
       - Key messages
       - Tone of voice
       - Call to actions
       - Brand story

    5. For Value Proposition:
       - Unique benefits
       - Problem solution fit
       - Competitive advantage
       - Customer value

    6. For Competitors:
       - Direct competitors
       - Indirect competitors
       - Market positioning
       - SWOT analysis

    7. For Channels:
       - Channel mix
       - Content strategy
       - Distribution plan
       - Timing

    8. For Metrics:
       - KPIs
       - Success metrics
       - ROI calculations
       - Performance targets

    Focus on actionable marketing insights and clear value communication.
    """,
"Legal_Document": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When processing legal documents, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Document Title] - Legal Analysis</title>
        <style>
            body {
                font-family: 'Times New Roman', serif;
                line-height: 1.8;
                color: #333;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { color: #2c3e50; }
            .summary, .definitions, .obligations, .conditions, .implications, .citations {
                background-color: #fff;
                padding: 15px;
                margin: 15px 0;
                border-radius: 4px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .summary { border-left: 4px solid #34495e; }
            .definitions { border-left: 4px solid #3498db; }
            .obligations { border-left: 4px solid #e74c3c; }
            .conditions { border-left: 4px solid #f1c40f; }
            .implications { border-left: 4px solid #2ecc71; }
            .citations { border-left: 4px solid #9b59b6; }
            .case-ref {
                font-style: italic;
                color: #666;
            }
            .definition-term {
                font-weight: bold;
                color: #2c3e50;
            }
            .warning {
                background-color: #fff3cd;
                border-left: 4px solid #ffc107;
                padding: 10px;
                margin: 10px 0;
            }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create these sections:
       - Executive Summary
       - Key Definitions
       - Rights and Obligations
       - Terms and Conditions
       - Legal Implications
       - Relevant Citations

    3. For Summary:
       - Document purpose
       - Key parties involved
       - Main provisions
       - Critical deadlines

    4. For Definitions:
       - Legal terms
       - Technical terms
       - Party definitions
       - Scope definitions

    5. For Rights/Obligations:
       - Party responsibilities
       - Legal requirements
       - Compliance needs
       - Time constraints

    6. For Conditions:
       - Precedent conditions
       - Subsequent conditions
       - Termination clauses
       - Amendment provisions

    7. For Implications:
       - Legal impact
       - Business impact
       - Risk assessment
       - Compliance requirements

    8. For Citations:
       - Relevant cases
       - Statutes
       - Regulations
       - Legal precedents

    Maintain formal legal language while providing clear explanations.
    Include appropriate disclaimers and warnings.
    """,

    "Medical_Literature": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When reviewing medical literature, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Article Title] - Medical Review</title>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <script>
        MathJax = {
            tex: {
                inlineMath: [['$', '$']],
                displayMath: [['$$', '$$']]
            }
        };
        </script>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.8;
                color: #333;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { color: #2c3e50; }
            .summary, .methods, .results, .clinical, .evidence, .references {
                background-color: #fff;
                padding: 15px;
                margin: 15px 0;
                border-radius: 4px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .summary { border-left: 4px solid #3498db; }
            .methods { border-left: 4px solid #2ecc71; }
            .results { border-left: 4px solid #f1c40f; }
            .clinical { border-left: 4px solid #e74c3c; }
            .evidence { border-left: 4px solid #9b59b6; }
            .references { border-left: 4px solid #34495e; }
            .evidence-level {
                font-weight: bold;
                color: #2c3e50;
            }
            .clinical-note {
                background-color: #f8f9fa;
                padding: 10px;
                border-radius: 4px;
                margin: 10px 0;
            }
            .warning {
                background-color: #fff3cd;
                border-left: 4px solid #ffc107;
                padding: 10px;
                margin: 10px 0;
            }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create these sections:
       - Clinical Summary
       - Methodology Review
       - Results Analysis
       - Clinical Implications
       - Evidence Assessment
       - References

    3. For Summary:
       - Clinical context
       - Key findings
       - Patient population
       - Clinical relevance

    4. For Methods:
       - Study design
       - Patient selection
       - Interventions
       - Outcome measures

    5. For Results:
       - Primary outcomes
       - Secondary outcomes
       - Statistical analysis
       - Subgroup analyses

    6. For Clinical:
       - Practice implications
       - Treatment modifications
       - Patient considerations
       - Implementation steps

    7. For Evidence:
       - Evidence quality
       - Study limitations
       - Bias assessment
       - Recommendation strength

    8. For References:
       - Primary sources
       - Related studies
       - Guidelines
       - Meta-analyses

    Include statistical analyses and clinical relevance.
    Maintain scientific rigor while being clinically applicable.
    """,
"Educational_Lesson": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When creating lesson plans, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Topic] - Lesson Plan</title>
        <style>
            body {
                font-family: 'Nunito', sans-serif;
                line-height: 1.8;
                color: #333;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { color: #2c3e50; }
            .overview, .objectives, .activities, .materials, .assessment, .differentiation {
                background-color: #fff;
                padding: 15px;
                margin: 15px 0;
                border-radius: 4px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .overview { border-left: 4px solid #3498db; }
            .objectives { border-left: 4px solid #2ecc71; }
            .activities { border-left: 4px solid #e74c3c; }
            .materials { border-left: 4px solid #f1c40f; }
            .assessment { border-left: 4px solid #9b59b6; }
            .differentiation { border-left: 4px solid #34495e; }
            .timing {
                background-color: #f8f9fa;
                padding: 5px 10px;
                border-radius: 3px;
                font-weight: bold;
            }
            .activity-step {
                margin: 10px 0;
                padding-left: 20px;
                border-left: 2px solid #eee;
            }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create these sections:
       - Lesson Overview
       - Learning Objectives
       - Learning Activities
       - Required Materials
       - Assessment Methods
       - Differentiation Strategies

    3. For Overview:
       - Topic introduction
       - Grade level
       - Time required
       - Prior knowledge

    4. For Objectives:
       - Learning goals
       - Success criteria
       - Curriculum standards
       - Key skills

    5. For Activities:
       - Introduction/hook
       - Main activities
       - Group work
       - Individual work
       - Closure

    6. For Materials:
       - Required resources
       - Technology needs
       - Handouts
       - Equipment

    7. For Assessment:
       - Formative methods
       - Summative methods
       - Success indicators
       - Feedback strategies

    8. For Differentiation:
       - Learning styles
       - Ability levels
       - Support strategies
       - Extensions

    Include clear timing for each activity.
    Focus on engaging and interactive learning experiences.
    """,

    "Scientific_Paper": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When breaking down scientific papers, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Paper Title] - Scientific Analysis</title>
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <script>
        MathJax = {
            tex: {
                inlineMath: [['$', '$']],
                displayMath: [['$$', '$$']]
            }
        };
        </script>
        <style>
            body {
                font-family: 'Source Sans Pro', sans-serif;
                line-height: 1.8;
                color: #333;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { color: #2c3e50; }
            .abstract, .methodology, .results, .discussion, .impact, .references {
                background-color: #fff;
                padding: 15px;
                margin: 15px 0;
                border-radius: 4px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .abstract { border-left: 4px solid #3498db; }
            .methodology { border-left: 4px solid #2ecc71; }
            .results { border-left: 4px solid #e74c3c; }
            .discussion { border-left: 4px solid #f1c40f; }
            .impact { border-left: 4px solid #9b59b6; }
            .references { border-left: 4px solid #34495e; }
            .equation {
                padding: 10px;
                background: #f8f9fa;
                border-radius: 4px;
                margin: 10px 0;
            }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create these sections:
       - Abstract Analysis
       - Methodology Breakdown
       - Results Interpretation
       - Discussion Review
       - Scientific Impact
       - Key References

    3. For Abstract:
       - Research question
       - Hypothesis
       - Key findings
       - Significance

    4. For Methodology:
       - Experimental design
       - Controls
       - Variables
       - Statistical methods

    5. For Results:
       - Data analysis
       - Key findings
       - Statistical significance
       - Visual representations

    6. For Discussion:
       - Interpretation
       - Limitations
       - Alternative explanations
       - Future directions

    7. For Impact:
       - Field significance
       - Applications
       - Future research
       - Broader implications

    8. For References:
       - Key citations
       - Related work
       - Supporting evidence
       - Further reading

    Include mathematical formulas and statistical analyses.
    Focus on scientific rigor and methodological clarity.
    """,

    "Policy_Document": """
    When analyzing policy documents, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Policy Title] - Analysis</title>
        <style>
            body {
                font-family: 'Georgia', serif;
                line-height: 1.8;
                color: #333;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { color: #2c3e50; }
            .summary, .context, .stakeholders, .implementation, .impact, .recommendations {
                background-color: #fff;
                padding: 15px;
                margin: 15px 0;
                border-radius: 4px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .summary { border-left: 4px solid #3498db; }
            .context { border-left: 4px solid #2ecc71; }
            .stakeholders { border-left: 4px solid #e74c3c; }
            .implementation { border-left: 4px solid #f1c40f; }
            .impact { border-left: 4px solid #9b59b6; }
            .recommendations { border-left: 4px solid #34495e; }
            .key-point {
                background-color: #f8f9fa;
                padding: 10px;
                border-radius: 4px;
                margin: 10px 0;
            }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create these sections:
       - Policy Summary
       - Policy Context
       - Stakeholder Analysis
       - Implementation Plan
       - Impact Assessment
       - Recommendations

    3. For Summary:
       - Policy objectives
       - Key provisions
       - Scope
       - Timeline

    4. For Context:
       - Historical background
       - Current situation
       - Related policies
       - Legal framework

    5. For Stakeholders:
       - Affected groups
       - Interests
       - Impacts
       - Engagement plans

    6. For Implementation:
       - Action steps
       - Resources needed
       - Timeline
       - Responsibilities

    7. For Impact:
       - Economic impact
       - Social impact
       - Environmental impact
       - Long-term effects

    8. For Recommendations:
       - Policy improvements
       - Implementation strategies
       - Risk mitigation
       - Success metrics

    Focus on clear policy analysis and practical implementation.
    Include relevant data and impact assessments.
    """,

    "Script_Summarizer": """
    IMPORTANT: Provide ONLY the HTML output. Do not include any explanatory text, introductions, or conclusions.
    Do not write phrases like "Here's the HTML" or "I hope this helps."
    Start directly with <!DOCTYPE html> and end with </html>.

    When creating study materials, create an HTML document following these guidelines:

    1. Use this HTML template:
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>[Chapter Title] - Study Guide</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }
            h1, h2, h3 { 
                color: #2c3e50;
                margin-top: 20px;
            }
            .chapter-overview, .key-takeaways {
                background-color: #fff;
                padding: 20px;
                margin: 20px 0;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .chapter-overview { 
                border-left: 6px solid #3498db;
            }
            .key-takeaways { 
                border-left: 6px solid #2ecc71;
            }
            .concept {
                background-color: #f7f9fc;
                padding: 10px 15px;
                margin: 10px 0;
                border-radius: 5px;
                border-left: 3px solid #9b59b6;
            }
            .definition {
                background-color: #f8f9fa;
                padding: 10px 15px;
                margin: 10px 0;
                border-radius: 5px;
                border-left: 3px solid #e74c3c;
            }
            .formula {
                background-color: #fff3cd;
                padding: 10px 15px;
                margin: 10px 0;
                border-radius: 5px;
                border-left: 3px solid #f1c40f;
                font-family: 'Courier New', monospace;
            }
            ul {
                padding-left: 20px;
            }
            li {
                margin: 8px 0;
            }
            .highlight {
                background-color: #fffbd4;
                padding: 2px 5px;
                border-radius: 3px;
            }
        </style>
    </head>
    <body>
    [Insert content here]
    </body>
    </html>

    2. Create exactly two main sections:
       <div class="chapter-overview">
           <h2>Chapter Overview</h2>
           [Insert brief summary]
       </div>

       <div class="key-takeaways">
           <h2>Key Takeaways</h2>
           [Insert study content]
       </div>

    3. For Chapter Overview:
       - Write a brief, clear summary of what the chapter is about (max 200 words)
       - Focus on the main topic and why it's important
       - Mention the key themes or areas covered
       - Use simple, straightforward language

    4. For Key Takeaways:
       - List every important concept, definition, and formula that needs to be memorized
       - Format each type of content appropriately:
         * Use <div class="concept"> for main ideas and theories
         * Use <div class="definition"> for important terms and their meanings
         * Use <div class="formula"> for formulas, equations, or rules
       - Break down complex ideas into bullet points
       - Include specific examples where helpful
       - List facts, figures, and dates that need to be memorized
       - Include any frameworks or models mentioned
       - Note relationships between different concepts
       - Include any step-by-step processes or procedures

    5. Formatting Guidelines:
       - Keep everything concise and to the point
       - Use bullet points for lists
       - Use numbered lists for sequences or steps
       - Bold key terms on first appearance
       - Use tables for comparing concepts
       - Use <span class="highlight"> for crucial points
       - Keep paragraphs short (2-3 lines maximum)

    The Key Takeaways section should function like comprehensive study cards - 
    someone should be able to learn and memorize just this section and be 
    prepared for an exam. Include all testable content but present it in the 
    most concise, clear way possible.

    Focus on accuracy and completeness while maintaining clarity.
    Present information in a logical, structured way that aids memorization.
    Make sure every important fact, concept, and relationship is included in the Key Takeaways.
    """
}


