DEFAULT_PROMPTS = {
    "Default": """
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
    """
}
