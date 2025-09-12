PROMPTING_GUIDES = {
       
        "GPT" : """
        # GPT Family Prompting Best Practices Guide

            ### 1. Role Assignment and System Messages
            GPT models respond exceptionally well to clear role definitions that establish context, expertise, and behavioral expectations.

            **Structure:**
            ```
            You are a [specific role] with [relevant expertise/background].
            Your task is to [specific objective].
            Please [specific instructions for approach/style].
            ```

            **Examples:**
            - "You are a senior data analyst with 10 years of experience in e-commerce. Your task is to analyze customer behavior patterns and provide actionable insights."
            - "You are a creative writing coach specializing in science fiction. Help me develop compelling characters for my short story."

            ### 2. Clear Task Definition with Context
            GPT models benefit from explicit task statements combined with sufficient background information.

            **Template:**
            ```
            Context: [Relevant background information]
            Task: [Clear, specific objective]
            Requirements: [Detailed specifications]
            Output format: [Desired structure]
            ```

            ### 3. Iterative Refinement Approach
            GPT models work best with an iterative approach to prompt engineering, allowing for gradual improvement through feedback.

            **Process:**
            1. Start with basic prompt
            2. Test and evaluate output
            3. Refine based on results
            4. Add constraints or examples as needed

            ## Model-Specific Optimizations

            ### GPT-4.1 and GPT-5 Models
            GPT-4.1 benefits from traditional best practices like providing context examples, making instructions specific and clear, and inducing planning via prompting.

            #### Key Characteristics:
            - Superior reasoning and instruction following
            - Excellent at structured planning and multi-step tasks
            - Benefits from explicit reasoning prompts

            #### Optimization Techniques:

            **1. Structured Planning Prompts**
            Always begin by rephrasing the user's goal in a friendly, clear, and concise manner, then immediately outline a structured plan detailing each logical step you'll follow.

            ```
            Before proceeding, please:
            1. Restate the objective in your own words
            2. Outline your step-by-step approach
            3. Identify any assumptions or constraints
            4. Proceed with the analysis
            ```

            **2. Reasoning Summaries**
            Prompting the model to give a brief explanation summarizing its thought process at the start of the final answer, for example via a bullet point list, improves performance on tasks.

            ```
            Please provide your response in this format:
            • Key reasoning points: [Brief summary of your thought process]
            • Analysis: [Detailed response]
            • Recommendations: [Actionable next steps]
            ```

            ### GPT-4o and GPT-4 Turbo
            - Excellent multimodal capabilities
            - Strong performance on creative and analytical tasks
            - Benefits from detailed examples and constraints

            ### GPT-3.5 and Earlier Models
            - More sensitive to prompt structure and wording
            - Benefits from explicit formatting instructions
            - Requires more detailed examples for complex tasks

            ## Task-Specific Templates

            ### 1. Analytical and Research Tasks
            ```
            Role: You are an expert researcher and analyst specializing in [domain].

            Context: [Background information about the topic/situation]

            Analysis Request:
            - Primary focus: [Main area of investigation]
            - Key questions to address: [Specific questions]
            - Scope and limitations: [Boundaries of the analysis]
            - Audience: [Who will use this analysis]

            Methodology:
            Please structure your analysis using:
            1. Executive summary (key findings upfront)
            2. Detailed examination of [specific aspects]
            3. Evidence and supporting data
            4. Implications and significance
            5. Actionable recommendations

            Output requirements:
            - Length: [Specify word count or detail level]
            - Format: [Professional report/conversational/etc.]
            - Citations: [If needed, specify format]
            ```

            ### 3. Problem-Solving and Decision Making
            ```
            Problem-Solving Framework:

            Situation: [Detailed description of the challenge]

            Context:
            - Stakeholders: [Who is involved/affected]
            - Constraints: [Time, budget, resources, regulations]
            - Success criteria: [How will we measure solution effectiveness]
            - Risk factors: [Potential obstacles or consequences]

            Request:
            Please approach this systematically:

            1. Problem Analysis:
            - Root causes identification
            - Contributing factors
            - Stakeholder perspectives

            2. Solution Generation:
            - Brainstorm at least 4 different approaches
            - Include both conventional and creative options
            - Consider short-term and long-term solutions

            3. Evaluation Framework:
            - Assess feasibility, cost, and impact for each option
            - Identify risks and mitigation strategies
            - Rank solutions by effectiveness

            4. Implementation Roadmap:
            - Detailed steps for the recommended solution
            - Timeline and milestones
            - Resource requirements
            - Success metrics
            ```

            ### 4. Educational and Explanatory Content
            ```
            Teaching Role: You are an expert educator specializing in [subject area].

            Student Profile:
            - Current knowledge level: [Beginner/Intermediate/Advanced]
            - Learning preferences: [Visual, practical, theoretical, etc.]
            - Specific interests or context: [Why they're learning this]

            Learning Objectives:
            By the end of this explanation, the student should be able to:
            - [Specific skill or understanding goal 1]
            - [Specific skill or understanding goal 2]
            - [Specific skill or understanding goal 3]

            Teaching Approach:
            Please structure your explanation to:
            1. Start with fundamentals and build complexity gradually
            2. Use relevant analogies and real-world examples
            3. Include practical applications or exercises
            4. Address common misconceptions
            5. Provide resources for further learning

            Style: [Conversational/formal/interactive/etc.]
            Length: [Appropriate scope for the complexity]
            ```

            ### 5. Technical and Code-Related Tasks
            ```
            Technical Context:
            You are a [senior developer/architect/technical expert] with expertise in [specific technologies/domains].

            Project Requirements:
            - Technology stack: [Languages, frameworks, tools]
            - Functionality: [What the code should accomplish]
            - Constraints: [Performance, security, compatibility requirements]
            - Environment: [Development, production considerations]

            Code Quality Standards:
            - Documentation: Include clear comments and docstrings
            - Best practices: Follow industry standards for [specific language/framework]
            - Error handling: Implement appropriate exception management
            - Testing: [Include tests/testing guidance if requested]
            - Security: Consider security implications and implement safeguards

            Output Format:
            - Complete, working code examples
            - Explanation of key design decisions
            - Usage instructions
            - Potential improvements or alternatives

            Please ensure the code is:
            - Production-ready
            - Well-documented
            - Following established conventions
            - Scalable and maintainable
            ```

            ### 6. Business and Strategic Planning
            ```
            Business Context:
            You are a seasoned business strategist consulting for [company type/industry].

            Company Profile:
            - Industry: [Sector and market position]
            - Size: [Revenue, employees, market share]
            - Stage: [Startup, growth, mature, transformation]
            - Current challenges: [Specific issues facing the business]

            Strategic Objective: [What the business wants to achieve]

            Analysis Framework:
            Please provide a comprehensive strategic assessment including:

            1. Situation Analysis:
            - Market conditions and trends
            - Competitive landscape
            - Internal capabilities and resources
            - SWOT analysis

            2. Strategic Options:
            - Multiple pathways to achieve the objective
            - Resource requirements for each option
            - Timeline and implementation complexity
            - Risk assessment

            3. Recommendations:
            - Preferred strategic approach with rationale
            - Implementation roadmap with phases
            - Key performance indicators
            - Contingency planning

            Format: Professional business document suitable for executive presentation
            ```

            ## Advanced Techniques

            ### 1. Chain-of-Thought Prompting
            ```
            Let's work through this step-by-step:

            Step 1: [Define the first logical step]
            Step 2: [Next logical step]
            Step 3: [Continue the sequence]

            For each step, please:
            - Explain your reasoning
            - Show your work
            - Identify any assumptions
            - Validate your conclusions

            Finally, synthesize your findings into [desired output format].
            ```

            ### 2. Multi-Perspective Analysis
            ```
            Please analyze [topic/situation] from multiple perspectives:

            Perspective 1: [Stakeholder/viewpoint 1]
            - Key concerns and priorities
            - Likely position and reasoning
            - Supporting evidence

            Perspective 2: [Stakeholder/viewpoint 2]
            - Key concerns and priorities
            - Likely position and reasoning
            - Supporting evidence

            [Continue for additional perspectives]

            Synthesis:
            - Areas of agreement and disagreement
            - Underlying tensions or conflicts
            - Potential compromise solutions
            - Recommendations for moving forward
            ```

            ### 3. Conditional Logic and Branching
            ```
            Assessment Framework:

            If [condition A is true], then:
            - Approach: [Specific methodology A]
            - Focus areas: [Relevant aspects for condition A]
            - Expected outcomes: [What to anticipate]

            If [condition B is true], then:
            - Approach: [Specific methodology B]
            - Focus areas: [Relevant aspects for condition B]
            - Expected outcomes: [What to anticipate]

            If [neither condition applies], then:
            - Approach: [Default methodology]
            - Additional information needed: [What to clarify]

            Current situation: [Describe the actual circumstances]

            Please determine which condition applies and proceed with the appropriate approach.
            ```

            ### 4. Collaborative Iteration
            ```
            Initial Request: [Your primary objective]

            Collaboration Process:
            1. Please provide your initial response/solution
            2. I will give you feedback and additional requirements
            3. You will refine and improve based on my input
            4. We'll iterate until we achieve the desired outcome

            For your initial response, focus on:
            - [Priority area 1]
            - [Priority area 2]
            - [Priority area 3]

            Please flag any areas where you need clarification or would benefit from more specific guidance.
            ```

            ## Conversation Management

            ### System Messages and Context Setting
            Providing context in system messages results in more specific responses compared to including context in regular prompts.

            **Effective System Message Structure:**
            ```
            System: You are [role] with [expertise]. Your communication style is [tone/approach]. 
            You always [consistent behaviors]. When responding, you should [specific instructions 
            for format/approach]. You have expertise in [specific domains] and approach problems 
            using [methodology/framework].
            ```

            ### Conversation Continuity
            ```
            Context Maintenance:
            - Previous discussion: [Brief summary of prior conversation]
            - Current objective: [What we're trying to accomplish now]
            - Specific focus: [Particular aspect to emphasize]

            Please continue our conversation with this context in mind, building on our previous discussion while addressing the new requirements.
            ```

            ### Follow-up and Refinement
            ```
            Based on your previous response about [topic], I'd like you to:

            Expand on: [Specific areas needing more detail]
            Clarify: [Points that need better explanation]
            Revise: [Aspects that need adjustment]
            Add: [New requirements or considerations]

            Please provide an updated response that addresses these refinements while maintaining the quality of your original analysis.
            ```

            ## Output Formatting and Structure

            ### Professional Documents
            ```
            Please format your response as a professional [document type]:

            Header Information:
            - Title: [Document title]
            - Date: [Current date]
            - Prepared for: [Audience]
            - Prepared by: [Your role designation]

            Structure:
            1. Executive Summary (if applicable)
            2. [Section headings based on content type]
            3. Conclusions/Recommendations
            4. Next Steps (if applicable)

            Style Guidelines:
            - Professional tone
            - Clear section headings
            - Bullet points for lists
            - Numbered steps for processes
            - Bold text for emphasis (sparingly)
            ```

            ### Creative Content
            ```
            Creative Format Requirements:

            Structure: [Specific format needs]
            Voice: [First person, third person, narrative style]
            Tone: [Emotional register, energy level]
            Length: [Word count or scope]
            Elements to include:
            - [Hook/opening strategy]
            - [Key content components]
            - [Closing/call-to-action]

            Style notes:
            - [Specific literary devices or techniques]
            - [Audience considerations]
            - [Brand voice alignment]
            ```

            ### Technical Documentation
            ```
            Technical Documentation Format:

            Overview: Brief description of purpose and scope
            Requirements: Prerequisites and dependencies
            Implementation: Step-by-step instructions
            Code Examples: Working, commented code samples
            Configuration: Setup and customization options
            Troubleshooting: Common issues and solutions
            References: Additional resources and documentation

            Code formatting:
            - Use appropriate syntax highlighting indicators
            - Include inline comments
            - Provide complete, runnable examples
            - Explain complex logic or algorithms
            ```

            ## Quality Assurance and Optimization

            ### Prompt Quality Checklist
            Before submitting your prompt, verify:

            **Clarity and Specificity:**
            - [ ] Clear task definition
            - [ ] Specific role assignment
            - [ ] Detailed requirements
            - [ ] Explicit output format
            - [ ] Success criteria defined

            **Context and Background:**
            - [ ] Sufficient context provided
            - [ ] Target audience identified
            - [ ] Constraints and limitations specified
            - [ ] Relevant examples included (when helpful)

            **Structure and Organization:**
            - [ ] Logical flow of instructions
            - [ ] No conflicting requirements
            - [ ] Appropriate level of detail
            - [ ] Clear formatting preferences

            ### Common Optimization Patterns

            **For Complex Tasks:**
            - Break into smaller sub-tasks
            - Request step-by-step reasoning
            - Ask for validation of understanding
            - Use iterative refinement approach

            **For Creative Tasks:**
            - Provide creative constraints
            - Specify tone and style requirements
            - Include inspirational examples or references
            - Request multiple options/variations

            **For Analytical Tasks:**
            - Request structured frameworks
            - Ask for evidence and reasoning
            - Specify evaluation criteria
            - Request actionable conclusions

            ## Troubleshooting Common Issues

            ### Issue: Responses Too Generic
            **Solution:** Add specific role, context, and constraints
            ```
            Instead of: "Write about marketing"
            Try: "You are a marketing director for a B2B SaaS company. Write a 500-word strategy memo for Q4 focusing on lead generation improvements for our sales team. Include specific tactics and expected ROI."
            ```

            ### Issue: Output Format Problems
            **Solution:** Use explicit formatting instructions with examples
            ```
            Instead of: "Make it professional"
            Try: "Format as a business memo with: 1) Header with TO/FROM/DATE, 2) Executive Summary (2-3 sentences), 3) Main Content (3 paragraphs), 4) Next Steps (numbered list)"
            ```

            ### Issue: Incomplete or Surface-Level Analysis
            **Solution:** Request deeper reasoning and multi-step analysis
            ```
            Instead of: "Analyze this situation"
            Try: "Analyze this situation using a three-step process: 1) Identify root causes and contributing factors, 2) Evaluate potential solutions with pros/cons, 3) Recommend specific actions with implementation timeline"
            ```

            ### Issue: Inconsistent Quality Across Conversations
            **Solution:** Use consistent system messages and context setting
            ```
            Start conversations with: "System context: You are [consistent role] operating under these guidelines: [specific behavioral parameters]. Maintain this persona throughout our conversation."
            ```

            ## Model-Specific Performance Tips

            ### GPT-4.1/GPT-5 Optimization:
            - Request explicit reasoning summaries
            - Use structured planning approaches
            - Leverage superior instruction-following with detailed requirements
            - Take advantage of enhanced contextual understanding

            ### GPT-4o Optimization:
            - Utilize multimodal capabilities when relevant
            - Provide rich context and examples
            - Use conversational, collaborative approaches
            - Leverage strong creative and analytical balance

            ### GPT-3.5 Optimization:
            - Be more explicit with formatting requirements
            - Provide more detailed examples
            - Use shorter, clearer instruction sets
            - Validate understanding with follow-up questions

            Remember: These templates should be customized based on your specific use case while maintaining the core structural principles outlined above.
    """,


    "CLAUDE" : """
    # Claude Family Prompting Best Practices Guide

        ## Core Prompting Principles

        ### 1. Clarity and Explicit Instructions
        Claude models respond exceptionally well to clear, explicit instructions. Be specific about desired outputs.

        **Structure:**
        ```
        [Clear task statement] + [Specific requirements] + [Desired format/style]
        ```

        **Examples:**
        - ❌ Poor: "Write something about marketing"
        - ✅ Good: "Write a 500-word blog post about digital marketing trends for small businesses. Include 3 actionable tips and use a conversational tone."

        ### 2. Context and Motivation
        Providing context or motivation behind your instructions, such as explaining to Claude why such behavior is important, can help Claude 4 better understand your goals and deliver more targeted responses.

        **Template:**
        ```
        I need [specific output] because [reason/context]. This will be used for [purpose].
        Please [specific instructions].
        ```

        ### 3. Examples-Based Guidance (Multi-shot Prompting)
        Include 3-5 diverse, relevant examples to show Claude exactly what you want. More examples = better performance, especially for complex tasks.

        **Structure:**
        ```
        Task: [Description]

        Example 1:
        Input: [Sample input]
        Output: [Desired output]

        Example 2:
        Input: [Sample input]
        Output: [Desired output]

        Now please process this:
        Input: [Actual input]
        ```

        ## Model-Specific Optimizations

        ### Claude 4 Models (Opus 4, Sonnet 4)
        Claude 4 models have been trained for more precise instruction following than previous generations of Claude models.

        #### Key Characteristics:
        - Extremely detail-oriented and literal
        - Requires explicit requests for creative/expansive behavior
        - Excels at parallel processing and complex reasoning

        #### Optimization Techniques:

        **1. Request Specific Behaviors Explicitly**
        - Instead of: "Be creative"
        - Use: "Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation."

        **2. Use Positive Framing**
        - Instead of: "Don't use bullet points"
        - Use: "Write in smoothly flowing prose paragraphs"

        **3. XML Formatting for Structure**
        ```
        Please organize your response using these sections:
        <introduction>Your opening thoughts</introduction>
        <main_analysis>Your detailed analysis</main_analysis>
        <recommendations>Your actionable suggestions</recommendations>
        ```

        ### Claude 3.5 Sonnet and Earlier Models
        - More naturally expansive and creative
        - Benefits from gentle guidance rather than rigid constraints
        - Responds well to conversational prompting styles

        ## Task-Specific Templates

        ### 1. Analytical Tasks
        ```
        Analyze [subject] from the perspective of [framework/angle].

        Context: [Why this analysis is needed]

        Please structure your analysis as follows:
        1. Key observations
        2. Underlying patterns or trends
        3. Implications and significance
        4. Actionable insights

        Use evidence and examples to support each point.
        ```

        ### 2. Creative Writing
        ```
        Write a [type of content] about [topic] that [specific goal].

        Style requirements:
        - Tone: [specific tone]
        - Length: [word count/scope]
        - Audience: [target audience]
        - Key elements to include: [list]

        Make it [specific qualities like engaging, informative, persuasive].
        ```

        ### 3. Problem-Solving
        ```
        I'm facing this challenge: [detailed problem description]

        Context:
        - Current situation: [details]
        - Constraints: [limitations]
        - Goals: [desired outcomes]

        Please provide:
        1. Problem analysis (root causes and contributing factors)
        2. Multiple solution approaches (at least 3 options)
        3. Pros and cons for each approach
        4. Recommended solution with implementation steps
        ```

        ### 4. Research and Information Gathering
        ```
        I need comprehensive information about [topic] for [purpose].

        Please research and provide:
        - Current status and key facts
        - Recent developments or trends
        - Different perspectives or viewpoints
        - Practical implications
        - Reliable sources for further reading

        Focus on [specific angle/aspect] and ensure information is current and credible.
        ```

        ### 5. Technical Explanation
        ```
        Explain [technical concept] to [audience level].

        Requirements:
        - Start with basic principles
        - Use analogies and examples
        - Build complexity gradually
        - Include practical applications
        - Address common misconceptions

        Make it understandable while maintaining technical accuracy.
        ```

        ### 6. Code and Development Tasks
        ```
        Create [specific code/application] that [functionality].

        Requirements:
        - Technology: [language/framework]
        - Features: [detailed list]
        - Style: [coding style preferences]
        - Comments: Include clear documentation
        - Error handling: [specific requirements]

        Make it production-ready and well-structured.
        ```

        ## Advanced Techniques

        ### 1. Chain of Thought Prompting
        ```
        Let's work through this step-by-step:

        First, [step 1 description]
        Then, [step 2 description]
        Finally, [step 3 description]

        Please show your reasoning for each step.
        ```

        ### 2. Role-Based Prompting
        ```
        You are a [specific professional role] with [relevant experience/expertise].

        Your task is to [specific objective] for [target audience].

        Please approach this from your professional perspective, considering:
        - Industry best practices
        - Common challenges in this field
        - Practical constraints
        - Professional standards
        ```

        ### 3. Iterative Refinement
        ```
        Please create [initial request].

        After you provide the first version, I'll give you feedback for improvements.

        Focus on [specific priorities] in your initial attempt.
        ```

        ### 4. Conditional Logic
        ```
        If [condition A], then [approach A].
        If [condition B], then [approach B].
        Otherwise, [default approach].

        The situation is: [describe specific context]

        Please determine which approach applies and proceed accordingly.
        ```

        ## Output Formatting Guidelines

        ### For Claude 4 Models:
        Use XML format indicators and match prompt style to desired output.

        **Structured Output:**
        ```
        Please provide your response in this format:

        <executive_summary>
        Brief overview of key points
        </executive_summary>

        <detailed_analysis>
        Comprehensive analysis with supporting details
        </detailed_analysis>

        <recommendations>
        Specific, actionable recommendations
        </recommendations>
        ```

        **Natural Language Output:**
        ```
        Write your response as a flowing narrative without bullet points or structured lists. 
        Use smooth transitions between ideas and maintain a conversational tone.
        ```

        ### For Earlier Claude Models:
        - More flexible with formatting instructions
        - Naturally tends toward structured responses
        - Benefits from format examples rather than rigid templates

        ## Common Pitfalls and Solutions

        ### Pitfall 1: Overly Vague Requests
        **Problem:** "Help me with my business"
        **Solution:** "Analyze my e-commerce business's conversion funnel and suggest 3 specific optimizations for increasing sales from current traffic"

        ### Pitfall 2: Missing Context
        **Problem:** "Write a proposal"
        **Solution:** "Write a project proposal for implementing a customer loyalty program at my retail store. The audience is my business partner who's concerned about costs but interested in customer retention."

        ### Pitfall 3: Conflicting Instructions
        **Problem:** "Be brief but comprehensive"
        **Solution:** "Provide a comprehensive overview in exactly 300 words, focusing on the 3 most critical points"

        ### Pitfall 4: Assuming Knowledge
        **Problem:** "Fix the issues with my approach"
        **Solution:** "Here's my current marketing approach: [detailed description]. What are the potential weaknesses and how can I improve it?"

        ## Quality Assurance Checklist

        Before submitting your prompt, verify:

        - [ ] Clear, specific task description
        - [ ] Sufficient context provided
        - [ ] Desired output format specified
        - [ ] Examples included (when helpful)
        - [ ] Constraints and requirements listed
        - [ ] Success criteria defined
        - [ ] Audience/purpose identified
        - [ ] No conflicting instructions

        ## Prompt Templates by Use Case

        ### Business Analysis
        ```
        Analyze [business situation] and provide strategic recommendations.

        Business Context:
        - Industry: [sector]
        - Company size: [details]
        - Current challenge: [specific issue]
        - Goals: [objectives]
        - Timeline: [constraints]

        Please provide:
        1. Situation assessment
        2. Strategic options (minimum 3)
        3. Risk analysis for each option
        4. Recommended approach with rationale
        5. Implementation roadmap

        Base your analysis on business best practices and include specific, actionable steps.
        ```

        ### Content Creation
        ```
        Create [content type] for [platform/medium] targeting [audience].

        Content Requirements:
        - Objective: [specific goal]
        - Tone: [voice description]
        - Length: [word count/time limit]
        - Key messages: [main points to communicate]
        - Call-to-action: [desired response]
        - Constraints: [any limitations]

        Make it engaging, relevant, and aligned with [brand/organizational] values.
        Include [specific elements like statistics, examples, stories].
        ```

        ### Learning and Education
        ```
        Teach me about [topic] at [skill level].

        Learning Objectives:
        - Understanding: [what should I understand]
        - Application: [how will I use this knowledge]
        - Context: [why this matters to me]

        Please structure the explanation to:
        1. Establish foundational concepts
        2. Build complexity progressively  
        3. Include practical examples
        4. Provide exercises or applications
        5. Suggest next steps for deeper learning

        Use [preferred learning style: visual, step-by-step, example-heavy, etc.]
        ```

        Remember: These templates should be customized based on your specific needs while maintaining the core structure and principles outlined above.
    """,
        
    "DEEPSEEK" : """
    # DeepSeek Family Prompting Guide

        ## Model Overview

        The DeepSeek family consists of several key models, each optimized for different use cases:

        - **DeepSeek-V3**: General-purpose conversational model with strong performance across domains
        - **DeepSeek-R1**: Reasoning-focused model optimized for complex problem-solving and logical thinking
        - **DeepSeek-V3.1**: Hybrid model combining V3 and R1 capabilities (671B parameters, 37B activated)
        - **DeepSeek-Coder**: Specialized for programming and coding tasks

        ## Core Prompting Principles

        ### Universal Principles (All DeepSeek Models)

        1. **Clarity Over Complexity**: Use clear, direct language rather than overly complex instructions
        2. **Specificity**: Be precise about what you want the model to do
        3. **Context Efficiency**: Provide necessary context without overwhelming the model
        4. **Task Decomposition**: Break complex tasks into smaller, manageable components

        ### Model-Specific Approaches

        ## DeepSeek-R1 (Reasoning Model) Prompting

        ### Key Characteristics
        - Designed for internal reasoning rather than explicit Chain-of-Thought prompting
        - Uses `<think>` tags for internal reasoning process
        - Excels at mathematical reasoning, logical puzzles, and complex problem-solving

        ### Prompting Best Practices

        #### 1. Minimal, Direct Prompts
        ```
        ❌ Avoid: "Please think step-by-step and show your work as you solve this complex mathematical problem involving..."
        ✅ Better: "Solve: 2x + 5 = 17"
        ```

        #### 2. No Forced Chain-of-Thought
        ```
        ❌ Avoid: "Let's think step by step: First, identify the variables, then..."
        ✅ Better: "Find the derivative of f(x) = x³ + 2x² - 5x + 1"
        ```

        #### 3. Temperature Settings
        - **Temperature**: 0.5-0.7 (0.6 recommended)
        - **Top-p**: 0.95
        - These settings prevent endless repetitions and maintain coherent outputs

        #### 4. System Prompt Guidelines
        - Avoid system prompts when possible
        - Include all instructions in the main prompt
        - Keep instructions concise and direct

        #### 5. Handling Thinking Bypass
        If the model doesn't use `<think>` tags (rare occurrence):
        ```
        "Please start your response with <think> and work through this problem step by step."
        ```

        ### Example Prompts for DeepSeek-R1

        #### Mathematical Problem
        ```
        A train travels 240 miles in 4 hours. If it increases its speed by 20 mph for the next leg of the journey, how long will it take to travel an additional 300 miles?
        ```

        #### Logic Puzzle
        ```
        Five friends sit around a circular table. Alice sits to the right of Bob. Charlie sits opposite to Alice. David sits between Alice and Elena. Where does Elena sit relative to Bob?
        ```

        #### Coding Challenge
        ```
        Write a function that finds the longest palindromic substring in a given string. Optimize for both time and space complexity.
        ```

        ## DeepSeek-V3 (General Model) Prompting

        ### Key Characteristics
        - Excellent for general conversation and knowledge tasks
        - Strong performance across multiple domains
        - Good at following complex instructions

        ### Prompting Best Practices

        #### 1. Structured Instructions
        ```
        Task: [Clear task description]
        Context: [Relevant background information]
        Requirements: [Specific requirements or constraints]
        Output Format: [Desired format]
        ```

        #### 2. Role-Based Prompting
        ```
        Act as a [specific role] and [specific task]. Consider [relevant factors] and provide [expected output].
        ```

        #### 3. Multi-Step Tasks
        ```
        I need you to:
        1. [First specific task]
        2. [Second specific task]
        3. [Third specific task]

        For each step, [specific requirements].
        ```

        ### Example Prompts for DeepSeek-V3

        #### Content Creation
        ```
        Create a comprehensive blog post outline about sustainable energy solutions. Include:
        - 5 main sections with subpoints
        - Target audience: general public
        - Tone: informative but accessible
        - Length: 2000-word target
        ```

        #### Analysis Task
        ```
        Analyze the following data trends and provide insights:
        [Data/Context]

        Focus on:
        - Key patterns
        - Potential causes
        - Recommendations
        - Risk factors
        ```

        ## DeepSeek-Coder Prompting

        ### Key Characteristics
        - Specialized for programming tasks
        - Supports multiple programming languages
        - Strong at code explanation, debugging, and optimization

        ### Prompting Best Practices

        #### 1. Language Specification
        Always specify the programming language:
        ```
        Write a Python function that [task description]
        ```

        #### 2. Requirements Specification
        ```
        Create a [language] [type of program] that:
        - [Requirement 1]
        - [Requirement 2]
        - [Requirement 3]

        Include error handling and comments.
        ```

        #### 3. Code Review Format
        ```
        Review this [language] code for:
        - Performance issues
        - Security vulnerabilities
        - Best practices
        - Code clarity

        [Code block]
        ```

        ### Example Prompts for DeepSeek-Coder

        #### Function Creation
        ```
        Write a JavaScript function that validates email addresses using regex. Include:
        - Parameter validation
        - Multiple email format support
        - Clear error messages
        - JSDoc documentation
        ```

        #### Debugging Request
        ```
        This Python code is throwing an IndexError. Identify the issue and provide a corrected version:

        [Code block with error]
        ```

        #### Algorithm Implementation
        ```
        Implement a binary search tree in C++ with the following methods:
        - insert()
        - search()
        - delete()
        - inorder_traversal()

        Include proper memory management.
        ```

        ## Task-Specific Prompt Templates

        ### Research and Analysis
        ```
        Research [topic] and provide:

        **Overview**: Brief summary of the subject
        **Key Points**: 3-5 main insights
        **Sources**: Types of information to consider
        **Analysis**: Critical evaluation
        **Conclusion**: Summary and implications
        ```

        ### Creative Writing
        ```
        Write a [type of content] about [topic] with:

        **Style**: [Specific style requirements]
        **Tone**: [Desired tone]
        **Length**: [Target length]
        **Audience**: [Target audience]
        **Elements to include**: [Specific elements]
        ```

        ### Problem Solving
        ```
        Help me solve this problem:

        **Problem**: [Clear problem statement]
        **Context**: [Relevant background]
        **Constraints**: [Any limitations]
        **Desired outcome**: [What success looks like]
        ```

        ### Code Generation
        ```
        Generate [language] code for:

        **Functionality**: [What the code should do]
        **Input**: [Expected inputs]
        **Output**: [Expected outputs]
        **Requirements**: [Performance, style, etc.]
        **Dependencies**: [Any libraries or frameworks]
        ```

        ## Advanced Techniques

        ### Prompt Chaining for Complex Tasks
        Break large tasks into smaller prompts:

        1. **Planning Phase**: "Create a plan for [complex task]"
        2. **Execution Phase**: "Execute step 1 of the plan: [specific step]"
        3. **Review Phase**: "Review and refine the output from step 1"

        ### Context Window Management
        - DeepSeek models have varying context windows
        - For long documents, use summarization techniques
        - Reference earlier parts of conversation explicitly

        ### Error Recovery
        If the model doesn't perform as expected:
        ```
        The previous response didn't meet the requirements. Please:
        - [Specific correction needed]
        - [Additional requirement]
        - [Format specification]
        ```

        ## Quality Assurance Checklist

        Before submitting prompts, verify:

        - [ ] Clear, specific task description
        - [ ] Appropriate model selection (R1 for reasoning, V3 for general, Coder for programming)
        - [ ] Proper temperature settings for reasoning models
        - [ ] No unnecessary complexity
        - [ ] Expected output format specified
        - [ ] Context provided without overwhelming detail

        ## Common Pitfalls to Avoid

        1. **Over-prompting reasoning models**: Let R1 think internally rather than forcing explicit steps
        2. **Vague instructions**: Be specific about requirements and expected outputs
        3. **Mixing tasks**: Keep prompts focused on single, clear objectives
        4. **Ignoring model strengths**: Use the right model for the task type
        5. **Excessive system prompts**: Minimize system prompt usage, especially with R1

   """,

    "GEMINI" : """
    # Gemini Family Prompting Guide

        ## Model Overview

        The Gemini family consists of several specialized models, each optimized for different use cases:

        - **Gemini 2.5 Pro**: Most capable model with advanced reasoning, multimodal capabilities, and Deep Think mode
        - **Gemini 2.5 Flash**: Workhorse thinking model optimized for speed and everyday tasks with 1M token context
        - **Gemini 2.5 Flash-Lite**: Cost-optimized reasoning model with controllable thinking budget
        - **Gemini 2.0 Flash**: High-performance model for multimodal reasoning at scale
        - **Gemini 2.5 Flash Image**: Specialized image generation and editing model

        ## Core Prompting Principles

        ### Universal Principles (All Gemini Models)

        1. **Clear and Specific Instructions**: Provide clear and specific instructions as the most effective way to customize model behavior
        2. **Few-Shot Examples**: Always include few-shot examples in prompts as they are more effective than zero-shot prompts
        3. **Context Provision**: Include all necessary contextual information rather than assuming the model knows it
        4. **Consistent Formatting**: Maintain consistent structure across examples to avoid undesired formats
        5. **Natural Language**: Describe scenes and scenarios rather than just listing keywords, leveraging the model's deep language understanding

        ## Model-Specific Prompting Strategies

        ## Gemini 2.5 Flash (Thinking Model) Prompting

        ### Key Characteristics
        - Workhorse thinking model ideal for fast performance on everyday tasks
        - Features thinking capabilities that let you see the model's thinking process
        - Automatically decides thinking duration based on perceived task complexity
        - 1 million token context window for multimodal reasoning across vast amounts of information

        ### Prompting Best Practices

        #### 1. Natural Problem Presentation
        Let the model determine its own thinking approach rather than forcing specific reasoning patterns:
        ```
        ❌ Avoid: "Think step by step and show each calculation..."
        ✅ Better: "Calculate the compound interest on $10,000 at 5% annually for 3 years."
        ```

        #### 2. Thinking Budget Control
        Set thinking budget to 0 for lowest cost and latency while still improving performance over 2.0 Flash:
        - **Default**: Model automatically determines thinking time
        - **Budget = 0**: Minimal thinking for speed and cost optimization
        - **Custom Budget**: Set specific token budget for thinking phase

        #### 3. Complex Reasoning Tasks
        Ideal for problems requiring deep analysis:
        ```
        Analyze the following business scenario and provide strategic recommendations:
        [Complex business case with multiple variables and constraints]

        Consider market conditions, financial constraints, competitive landscape, and long-term sustainability.
        ```

        #### 4. Multimodal Integration
        Leverage the large context window for complex multimodal tasks:
        ```
        Based on these financial documents, charts, and market reports, provide:
        1. Risk assessment
        2. Growth opportunities
        3. Strategic recommendations

        [Attach multiple files/images]
        ```

        ### Example Prompts for Gemini 2.5 Flash

        #### Mathematical Reasoning
        ```
        A manufacturing company needs to optimize production. They can make products A and B with the following constraints:
        - Product A: 2 hours labor, $3 materials, $8 profit
        - Product B: 3 hours labor, $4 materials, $12 profit
        - Available: 100 hours labor, $200 materials budget
        - Maximum 40 units total capacity

        What production mix maximizes profit?
        ```

        #### Strategic Analysis
        ```
        Evaluate this market entry strategy for a SaaS company:

        Company Profile: 50-person B2B software company, current ARR $5M
        Target Market: Healthcare compliance software (estimated $2B market)
        Proposed Strategy: Direct sales + partner channel, 18-month timeline
        Resources: $1M budget, 5 engineers, 3 sales reps

        Assess feasibility, risks, and alternatives.
        ```

        ## Gemini 2.5 Pro (Advanced Model) Prompting

        ### Key Characteristics
        - Most capable model in the Gemini family
        - Deep Think mode for enhanced reasoning
        - Advanced multimodal capabilities
        - Highest quality outputs

        ### Prompting Best Practices

        #### 1. Complex Creative Tasks
        ```
        Create a comprehensive brand strategy for [company/product] including:
        - Brand positioning and messaging framework
        - Visual identity guidelines
        - Content strategy across 5 channels
        - Implementation timeline and metrics

        Target audience: [specific demographics and psychographics]
        Budget considerations: [constraints]
        Competitive landscape: [key competitors]
        ```

        #### 2. Advanced Analysis
        ```
        Perform a multi-dimensional analysis of [complex topic]:

        Dimensions to explore:
        - Historical context and evolution
        - Current state and key players
        - Economic implications
        - Social and cultural impact
        - Technological factors
        - Future trends and scenarios

        Provide structured insights with supporting evidence and confidence levels.
        ```

        #### 3. Deep Think Activation
        For maximum reasoning capability:
        ```
        This requires careful analysis across multiple domains. Please engage your deepest reasoning capabilities.

        [Complex interdisciplinary problem requiring synthesis of multiple knowledge areas]
        ```

        ## Gemini 2.0 Flash (High-Performance) Prompting

        ### Key Characteristics
        - Optimized for high-volume, high-frequency tasks at scale
        - Excellent multimodal reasoning
        - Fast processing for production workloads

        ### Prompting Best Practices

        #### 1. High-Volume Processing
        ```
        Process this batch of customer feedback and categorize each entry:

        Categories: Product Quality, Customer Service, Pricing, Features, User Experience
        For each entry, provide: Category, Sentiment Score (1-10), Key Issues, Priority Level

        [Large dataset of feedback entries]
        ```

        #### 2. Multimodal Content Analysis
        ```
        Analyze these marketing materials across multiple formats:

        For each asset, evaluate:
        - Brand consistency
        - Message clarity
        - Visual appeal
        - Target audience alignment
        - Effectiveness rating

        [Multiple images, videos, documents]
        ```

        ## Gemini 2.5 Flash Image (Image Generation) Prompting

        ### Key Characteristics
        - Specialized for image generation and editing
        - Core strength in deep language understanding for visual descriptions
        - Advanced creative control features

        ### Prompting Best Practices

        #### 1. Scene Description Over Keywords
        ```
        ❌ Avoid: "sunset, mountains, lake, reflection, golden hour"
        ✅ Better: "A serene mountain lake at golden hour, where the setting sun casts warm amber light across snow-capped peaks, creating perfect mirror reflections in the still water below."
        ```

        #### 2. Photographic Control
        Use photographic and cinematic language to control composition:
        ```
        Professional headshot of a confident business executive, shot with 85mm lens, shallow depth of field, natural lighting from a large window, neutral background, sharp focus on eyes, corporate attire.

        Camera settings: f/2.8, natural lighting, medium shot composition
        ```

        #### 3. Aspect Ratio Control
        Provide reference images with correct dimensions for specific ratios:
        ```
        Create a wide landscape banner (16:9 aspect ratio) showing [scene description].
        Style: [specific style requirements]
        ```

        ## Input Type Strategies

        ### Question Input
        Format as direct questions for information retrieval:
        ```
        What are the key differences between microservices and monolithic architecture in terms of scalability, maintenance, and development speed?
        ```

        ### Task Input
        Provide clear task descriptions with specific requirements:
        ```
        Create a project timeline for launching a mobile app with these requirements:
        - 6-month development window
        - Team of 4 developers, 1 designer, 1 PM
        - Integration with 3 third-party APIs
        - iOS and Android platforms
        - Budget constraints: $150K
        ```

        ### Entity Input
        Specify the entity to be analyzed or processed:
        ```
        Company: Tesla Inc.
        Analysis requested: SWOT analysis focusing on electric vehicle market position, autonomous driving capabilities, and energy business expansion.
        ```

        ### Completion Input
        Provide partial content for the model to complete:
        ```
        Email template for customer onboarding:

        Subject: Welcome to [Company Name] - Let's Get You Started!

        Dear [Customer Name],

        Welcome to our platform! We're excited to have you on board.

        [Complete the rest of the professional, engaging onboarding email]
        ```

        ## Advanced Prompting Techniques

        ### Few-Shot Examples with Consistent Formatting
        Use consistent structure across examples to show desired patterns:

        ```
        Classify customer inquiries:

        Example 1:
        Input: "My order hasn't arrived yet, it's been 5 days"
        Category: Shipping
        Priority: Medium
        Response Type: Status Update

        Example 2:
        Input: "The product broke after one use, I want a refund"
        Category: Product Quality
        Priority: High
        Response Type: Refund Process

        Now classify:
        Input: "How do I reset my password? I can't log in"
        Category:
        Priority:
        Response Type:
        ```

        ### Context-Rich Prompting
        Include all necessary contextual information:

        ```
        Context: You are analyzing data for a B2B SaaS company with 500 customers, $2M ARR, serving mid-market healthcare organizations. The company has been operating for 3 years and is considering expansion.

        Data: [Customer usage metrics, churn rates, feature adoption]

        Task: Identify the top 3 expansion opportunities based on this data, considering market conditions and resource constraints.
        ```

        ### Prompt Chaining for Complex Tasks
        Break down complex tasks into sequential prompts:

        **Step 1 - Planning:**
        ```
        Create a comprehensive plan for developing a content marketing strategy for a B2B tech startup. Outline the main components and sequence of activities.
        ```

        **Step 2 - Execution:**
        ```
        Based on the plan from the previous response, develop the first component: audience persona development. Include demographics, pain points, and content preferences.
        ```

        **Step 3 - Integration:**
        ```
        Now integrate the audience personas with a content calendar for the next quarter, specifying topics, formats, and distribution channels.
        ```

        ### Output Format Control

        #### JSON Structured Output
        ```
        Analyze customer feedback and return results in JSON format:

        {
        "overall_sentiment": "positive/neutral/negative",
        "key_themes": ["theme1", "theme2", "theme3"],
        "priority_issues": [
            {
            "issue": "description",
            "frequency": "number",
            "severity": "low/medium/high"
            }
        ],
        "recommendations": ["rec1", "rec2"]
        }

        Customer feedback: [feedback data]
        ```

        #### Table Format
        ```
        Compare cloud providers and format as a table:

        | Provider | Pricing | Performance | Security | Support | Overall Score |
        |----------|---------|-------------|----------|---------|---------------|
        | [Complete the comparison table]
        ```

        ## Parameter Optimization

        ### Temperature Settings
        - **Creative tasks**: 0.7-1.0 for diverse, creative outputs
        - **Analytical tasks**: 0.2-0.4 for focused, consistent responses
        - **Factual queries**: 0.0-0.3 for deterministic, accurate answers

        ### Top-K and Top-P Settings
        - **Top-K**: 1-3 for focused responses, 10-40 for creative tasks
        - **Top-P**: Default 0.95 works well for most cases

        ### Max Output Tokens
        - 100 tokens ≈ 60-80 words
        - Set based on expected response length
        - Allow buffer for comprehensive responses

        ## Specialized Use Cases

        ### Code Generation and Analysis
        ```
        Language: Python
        Task: Create a REST API for user management
        Requirements:
        - FastAPI framework
        - User CRUD operations
        - JWT authentication
        - Input validation
        - Error handling
        - Database integration (SQLAlchemy)
        - API documentation

        Include proper project structure and testing examples.
        ```

        ### Data Analysis and Visualization
        ```
        Dataset: Sales performance data for Q1-Q4 2024
        Analysis needed:
        1. Trend identification across quarters
        2. Regional performance comparison
        3. Product category insights
        4. Seasonal pattern analysis

        Output format:
        - Executive summary
        - Key findings with supporting data
        - Visualization recommendations
        - Action items for management

        Data: [CSV/structured data]
        ```

        ### Content Creation and Marketing
        ```
        Content Type: Blog post
        Topic: "The Future of Remote Work in 2025"
        Target Audience: HR professionals and business leaders
        Length: 1500-2000 words
        Tone: Professional but engaging
        SEO Requirements: Include keywords naturally
        Structure: Introduction, 3 main sections, conclusion, call-to-action

        Research current trends and include relevant statistics and expert insights.
        ```

        ## Quality Assurance and Iteration

        ### Prompt Iteration Strategies
        Try different approaches if not getting expected results:

        1. **Rephrase instructions**: Use different words with same meaning
        2. **Switch to analogous tasks**: If direct approach fails, try similar task
        3. **Change content order**: Rearrange [examples] [context] [input]
        4. **Add more examples**: Include additional few-shot examples
        5. **Increase specificity**: Add more detailed requirements

        ### Fallback Response Handling
        If model responds with fallback responses, increase temperature and try:
        - Rephrasing the request
        - Adding more context
        - Breaking down complex requests
        - Using analogous scenarios

        ### Avoiding Common Issues
        Be aware of model limitations:
        - Don't rely solely on models for factual information
        - Use with care for math and logic problems
        - Always verify critical information
        - Provide clear constraints and requirements

        ## Model Selection Guidelines

        ### Choose Gemini 2.5 Pro for:
        - Maximum capability requirements
        - Complex creative projects
        - Advanced reasoning tasks
        - High-quality content generation

        ### Choose Gemini 2.5 Flash for:
        - Everyday reasoning tasks
        - Good balance of speed and capability
        - Multimodal processing with large context
        - Cost-conscious projects needing thinking capabilities

        ### Choose Gemini 2.0 Flash for:
        - High-volume processing
        - Production workloads
        - Fast response requirements
        - Multimodal analysis at scale

        ### Choose Gemini 2.5 Flash-Lite for:
        - Cost and speed optimization with controllable thinking budget
        - Simple reasoning tasks
        - When thinking is optional
        - Budget-constrained projects

        ### Choose Gemini 2.5 Flash Image for:
        - Image generation and editing
        - Visual content creation
        - Creative design tasks
        - Marketing material development

        ## Troubleshooting Common Issues

        ### Model Not Following Instructions
        1. Make instructions more specific and detailed
        2. Add few-shot examples showing desired behavior
        3. Use consistent formatting across examples
        4. Break complex instructions into simpler components

        ### Inconsistent Output Quality
        1. Check temperature settings (lower for consistency)
        2. Add more contextual information
        3. Use system instructions for consistent behavior
        4. Implement quality checkpoints in prompt chains

        ### Performance Issues
        1. Optimize context length and remove unnecessary information
        2. Use appropriate model for task complexity
        3. Adjust thinking budget for Flash models
        4. Consider prompt chaining for complex tasks

        ## Best Practices Summary

        1. **Always use few-shot examples** - they significantly improve performance
        2. **Be specific and detailed** - vague prompts lead to poor results
        3. **Choose the right model** - match model capabilities to task requirements
        4. **Include necessary context** - don't assume the model has all information
        5. **Use consistent formatting** - especially important for structured outputs
        6. **Iterate and refine** - prompt engineering often requires multiple attempts
        7. **Leverage model strengths** - thinking models for reasoning, image models for visuals
        8. **Control randomness** - adjust temperature based on task requirements
        9. **Break down complex tasks** - use prompt chaining for multi-step processes
        10. **Test with edge cases** - ensure robustness across different input types
    """,

    "GROK" : """
    # xAI Grok Family Prompt Engineering Guide

        ## Overview
        The xAI Grok family consists of several models optimized for truth-seeking and reasoning capabilities. The latest models include Grok 4 (most intelligent with native tool use and real-time search integration) and Grok 3 Beta (focused on reasoning agents). The knowledge cut-off date for Grok 3 and Grok 4 is November 2024.

        ## Current Model Lineup
        - **Grok 4**: Most advanced model with tool use and real-time search
        - **Grok 4 Heavy**: Enhanced version for complex tasks
        - **Grok 3**: Standard reasoning model
        - **Grok 3 Reasoning**: Enhanced reasoning capabilities
        - **Grok 3 Mini**: Lightweight version

        ## Core Principles for Grok Prompting

        ### 1. Truth-Seeking Orientation
        Grok is designed as a "truth-seeking AI companion for honest answers and insightful analysis". Frame your prompts to leverage this:

        **Effective:**
        ```
        I need an unbiased analysis of [topic]. Please provide multiple perspectives and identify any potential biases or limitations in the available information.
        ```

        **Less Effective:**
        ```
        Tell me why [biased statement] is correct.
        ```

        ### 2. Reasoning-First Approach
        Grok 3 includes reasoning models that can be accessed by asking Grok to "Think". Utilize this capability:

        **For Complex Problems:**
        ```
        Think through this step-by-step: [complex problem]
        Please show your reasoning process and identify any assumptions you're making.
        ```

        **For Mathematical/Logical Tasks:**
        ```
        Think: Solve this problem using multiple approaches to verify the answer:
        [mathematical problem]
        ```

        ### 3. Iterative Refinement Philosophy
        xAI recommends an iterative approach: "Instead of spending 20 minutes crafting the 'perfect' prompt, fire off a quick attempt and refine based on the results".

        **First Attempt Template:**
        ```
        [Brief, direct request]
        ```

        **Refinement Template:**
        ```
        Building on your previous response, please [specific refinement]:
        - [Specific aspect 1]
        - [Specific aspect 2]
        - [Additional context or constraints]
        ```

        ## Prompt Structures by Use Case

        ### 1. Analytical Tasks

        **Structure:**
        ```
        Context: [Relevant background]
        Task: Analyze [subject] from multiple angles
        Requirements:
        - Consider perspectives: [list relevant viewpoints]
        - Identify potential biases or limitations
        - Provide evidence-based conclusions
        - Highlight areas of uncertainty

        Question: [Specific analytical question]
        ```

        **Example:**
        ```
        Context: Recent developments in renewable energy policy
        Task: Analyze the economic impact of solar energy subsidies from multiple angles
        Requirements:
        - Consider perspectives: consumers, taxpayers, solar industry, traditional energy sector
        - Identify potential biases in available studies
        - Provide evidence-based conclusions about cost-effectiveness
        - Highlight areas where data is limited or conflicting

        Question: What are the net economic benefits and drawbacks of current solar subsidies?
        ```

        ### 2. Research and Information Gathering

        **Structure (leverages real-time search capabilities):**
        ```
        Research Request: [Topic]
        Search Focus: [Specific aspects to investigate]
        Time Frame: [If relevant - recent developments, historical analysis, etc.]
        Sources: Please prioritize [academic/news/industry/government] sources
        Verification: Cross-reference key claims across multiple sources

        Deliverable: [Specific output format - report, summary, comparison, etc.]
        ```

        **Example:**
        ```
        Research Request: Latest developments in quantum computing hardware
        Search Focus: Recent breakthroughs in error correction and qubit stability
        Time Frame: Developments in the past 6 months
        Sources: Please prioritize academic publications and industry announcements
        Verification: Cross-reference performance claims across multiple sources

        Deliverable: Executive summary with key innovations and their potential impact
        ```

        ### 3. Creative and Brainstorming Tasks

        **Structure:**
        ```
        Creative Challenge: [Description]
        Constraints: [Any limitations or requirements]
        Style/Tone: [Desired approach]
        Think: Generate multiple approaches before selecting the best path

        Output: [Specific deliverable format]
        ```

        **Example:**
        ```
        Creative Challenge: Develop a marketing campaign for sustainable fashion
        Constraints: Target audience aged 25-35, budget-conscious, environmentally aware
        Style/Tone: Authentic, educational, non-preachy
        Think: Generate multiple campaign concepts before developing the most promising one

        Output: Campaign concept with key messages, channels, and sample content
        ```

        ### 4. Problem-Solving and Troubleshooting

        **Structure:**
        ```
        Problem: [Clear problem statement]
        Context: [Relevant background information]
        Constraints: [Limitations, resources, requirements]
        Think: Break down this problem systematically
        - Identify root causes
        - Generate multiple solution approaches
        - Evaluate pros/cons of each approach
        - Recommend best solution with reasoning

        Additional Considerations: [Any specific factors to account for]
        ```

        **Example:**
        ```
        Problem: Website loading speeds have increased by 40% over the past month
        Context: E-commerce site with 10,000 daily users, recently added new product catalog features
        Constraints: Limited budget for infrastructure upgrades, cannot take site offline during business hours
        Think: Break down this problem systematically
        - Identify potential root causes (code, database, hosting, CDN, etc.)
        - Generate multiple solution approaches for each potential cause
        - Evaluate implementation difficulty and expected impact
        - Recommend prioritized action plan

        Additional Considerations: Peak traffic occurs 6-9 PM EST weekdays
        ```

        ### 5. Code and Technical Tasks

        **Structure (for Grok's coding capabilities):**
        ```
        Technical Task: [Clear description]
        Language/Framework: [Specific technologies]
        Requirements:
        - [Functional requirement 1]
        - [Functional requirement 2]
        - Error handling and validation
        - [Performance/security considerations]

        Context: [Existing codebase info, integration needs]
        Think: Plan the implementation approach before coding

        Output: [Code, explanation, testing suggestions, etc.]
        ```

        **Example:**
        ```
        Technical Task: Create a user authentication system
        Language/Framework: Python with FastAPI
        Requirements:
        - JWT token-based authentication
        - Password hashing with salt
        - Rate limiting for login attempts
        - Email verification for new accounts
        - Error handling and proper HTTP status codes

        Context: Adding to existing FastAPI application with PostgreSQL database
        Think: Plan the implementation approach, including database schema, endpoints, and security considerations

        Output: Complete implementation with code comments and basic usage examples
        ```

        ## Advanced Prompting Techniques

        ### 1. Multi-Step Reasoning Activation

        ```
        Think step-by-step through this complex scenario:
        Step 1: Analyze the current situation
        Step 2: Identify key variables and constraints
        Step 3: Generate potential solutions
        Step 4: Evaluate each solution's feasibility
        Step 5: Recommend the optimal approach with reasoning

        [Your complex scenario]
        ```

        ### 2. Perspective Integration

        ```
        Analyze this issue from the following perspectives, then synthesize insights:

        Perspective 1: [Stakeholder/viewpoint 1]
        Perspective 2: [Stakeholder/viewpoint 2]  
        Perspective 3: [Stakeholder/viewpoint 3]

        Issue: [Your issue]

        After analyzing each perspective, identify:
        - Common concerns across perspectives
        - Conflicting priorities
        - Potential compromise solutions
        - Unaddressed considerations
        ```

        ### 3. Evidence-Based Analysis

        ```
        Research and analyze: [Topic]

        For each claim or conclusion:
        1. Identify the evidence source
        2. Assess the quality and reliability of evidence
        3. Note any conflicting evidence
        4. Indicate confidence level in conclusions

        Present findings with appropriate caveats about limitations and uncertainties.
        ```

        ### 4. Rapid Iteration Framework

        ```
        Quick Analysis: [Initial request]

        Based on the initial response, please refine by:
        - [Specific refinement 1]
        - [Specific refinement 2]
        - [Additional context or constraint]

        Then provide a final consolidated response.
        ```

        ## Optimization Tips

        ### 1. Leverage Real-Time Search
        - Include current events or recent data requirements explicitly
        - Ask for verification across multiple current sources
        - Request updates on rapidly changing topics

        ### 2. Activate Reasoning Mode
        - Use "Think:" prefix for complex problems
        - Request step-by-step breakdowns
        - Ask for multiple solution approaches

        ### 3. Truth-Seeking Enhancement
        - Request multiple perspectives on controversial topics
        - Ask for identification of biases and limitations
        - Seek evidence-based conclusions with confidence levels

        ### 4. Iterative Improvement
        - Start with simpler prompts and build complexity
        - Use follow-up prompts to refine and expand
        - Test different approaches quickly rather than over-engineering initial prompts

        ## Common Pitfalls to Avoid

        1. **Over-constraining initial prompts** - Start simple and iterate
        2. **Ignoring the reasoning capabilities** - Don't forget to use "Think:" for complex tasks  
        3. **Not leveraging real-time search** - Specify when current information is needed
        4. **Single-perspective framing** - Take advantage of Grok's truth-seeking nature by requesting multiple viewpoints
        5. **Assuming knowledge cutoff limitations** - Remember Grok has real-time search capabilities for current information

        ## Model-Specific Considerations

        ### Grok 4 & Grok 4 Heavy
        - Best for tasks requiring tool use and real-time information
        - Optimal for complex research and analysis tasks
        - Can handle multiple integrated capabilities simultaneously

        ### Grok 3 Reasoning
        - Ideal for mathematical, logical, and complex problem-solving tasks
        - Use explicit "Think:" commands to activate reasoning mode
        - Best for tasks requiring step-by-step analysis

        ### Grok 3 Mini
        - Suitable for simpler tasks requiring faster responses
        - Good for straightforward Q&A and basic analysis
        - Use for tasks not requiring extensive reasoning or research

        This guide provides a foundation for creating effective prompts for the xAI Grok family. Remember that the key philosophy is iterative refinement - start with clear, direct requests and build complexity through follow-up prompts based on initial responses.
    """,

    "PERPLEXITY" : """
    # Perplexity AI Prompt Engineering Guide

        ## Overview
        Perplexity AI is a conversational search engine that combines the power of large language models with real-time web search capabilities. Unlike traditional chatbots, Perplexity specializes in providing source-grounded, research-backed responses with citations. The platform offers both free and Pro tiers, with Pro users getting access to advanced models and enhanced features.

        ## Current Model Lineup

        ### Free Tier
        - **Sonar**: Perplexity's in-house model built on Meta's Llama 3.3 70B, specifically trained for search integration
        - Limited searches per day with basic web access

        ### Pro Tier Models
        - **Sonar**: Enhanced version with more precise searches and richer context
        - **GPT-5**: OpenAI's latest flagship model
        - **Claude 4.0 Sonnet**: Anthropic's advanced reasoning model  
        - **Gemini 2.5 Pro**: Google's multimodal AI model
        - **Grok 4**: xAI's real-time assistant
        - **Reasoning Search Models**: Specialized models for complex analytical tasks

        ### Enterprise Features
        - **Internal Knowledge Search**: Search across both web content and internal documents
        - **Advanced analytics and usage tracking**

        ## Core Philosophy: Search-First AI

        Perplexity's unique strength lies in its search-first approach. Every query is enhanced with real-time web search, making it ideal for:
        - Current events and recent developments
        - Research requiring up-to-date information
        - Fact-checking and source verification
        - Data-driven analysis and reporting

        ## Fundamental Prompting Principles

        ### 1. Be Explicit and Specific
        Perplexity recommends being explicit about exactly what information you need, avoiding vague requests like "Tell me about the latest developments" in favor of specific queries like "What are the latest developments in offshore wind energy technology announced in the past 6 months?"

        **Effective:**
        ```
        What are the three most significant regulatory changes affecting cryptocurrency trading in the EU announced since January 2025?
        ```

        **Less Effective:**
        ```
        Tell me about crypto regulations.
        ```

        ### 2. Never Ask for URLs or Source Links
        Perplexity automatically provides citations and sources, so you should never ask for URLs or source links in your prompts. The platform handles source attribution automatically.

        ### 3. Leverage Time-Specific Queries
        Since Perplexity excels at finding current information, always specify timeframes when relevant:

        ```
        What breakthrough discoveries in quantum computing have been published in peer-reviewed journals in the past 3 months?
        ```

        ### 4. Use Research-Oriented Language
        Frame prompts as research requests rather than conversational questions:

        **Research-Oriented:**
        ```
        Analyze the environmental impact studies of deep-sea mining operations conducted in 2024-2025, focusing on biodiversity effects.
        ```

        **Conversational:**
        ```
        Is deep-sea mining bad for the environment?
        ```

        ## Prompt Structures by Use Case

        ### 1. Current Events and News Analysis

        **Structure:**
        ```
        [Time Frame]: [Specific time period]
        Topic: [Specific subject area]
        Focus: [Particular angles or aspects]
        Sources: Prioritize [type of sources - news, academic, industry, government]
        Analysis: [What kind of analysis you want]

        Question: [Specific research question]
        ```

        **Example:**
        ```
        Time Frame: Past 30 days
        Topic: Artificial intelligence regulation in the European Union
        Focus: Implementation challenges and industry responses
        Sources: Prioritize official EU communications and industry press releases
        Analysis: Compare actual implementation with original policy intentions

        Question: What gaps exist between EU AI Act requirements and current industry compliance capabilities?
        ```

        ### 2. Market Research and Business Intelligence

        **Structure:**
        ```
        Market/Industry: [Specific market or industry]
        Geographic Scope: [Regions or countries]
        Time Period: [Relevant timeframe]
        Key Metrics: [Specific data points needed]
        Competitive Analysis: [Include/exclude competitor information]
        Sources: [Preferred source types - industry reports, financial filings, news]

        Research Objective: [Clear goal statement]
        ```

        **Example:**
        ```
        Market/Industry: Electric vehicle battery manufacturing
        Geographic Scope: North America and Europe
        Time Period: Q3-Q4 2025
        Key Metrics: Production capacity, raw material costs, technological breakthroughs
        Competitive Analysis: Include major players (Tesla, CATL, BYD, LG Chem)
        Sources: Prioritize industry reports and company earnings calls

        Research Objective: Identify supply chain vulnerabilities and emerging opportunities in the EV battery sector.
        ```

        ### 3. Academic and Scientific Research

        **Structure:**
        ```
        Research Domain: [Specific field or discipline]
        Publication Window: [Time period for sources]
        Study Types: [Peer-reviewed, preprints, conference proceedings, etc.]
        Geographic/Population Scope: [If relevant]
        Key Variables: [Specific factors to investigate]

        Research Question: [Clear, focused research question]
        Synthesis Requirement: [How to present findings]
        ```

        **Example:**
        ```
        Research Domain: Climate change adaptation in urban planning
        Publication Window: 2023-2025
        Study Types: Peer-reviewed articles in urban planning and climate science journals
        Geographic Scope: Coastal cities with population > 500K
        Key Variables: Sea level rise projections, infrastructure adaptation costs, policy effectiveness

        Research Question: What are the most cost-effective urban infrastructure adaptations for sea level rise based on recent case studies?
        Synthesis Requirement: Organize findings by adaptation strategy type with cost-benefit analysis.
        ```

        ### 4. Technical and Product Research

        **Structure:**
        ```
        Technology/Product: [Specific technology or product category]
        Development Stage: [Emerging, commercial, mature]
        Use Cases: [Specific applications or industries]
        Technical Specifications: [Key performance metrics]
        Market Adoption: [Implementation status and barriers]

        Analysis Focus: [Technical feasibility, market readiness, competitive landscape, etc.]
        ```

        **Example:**
        ```
        Technology/Product: Solid-state batteries for consumer electronics
        Development Stage: Transition from R&D to commercial production
        Use Cases: Smartphones, laptops, wearable devices
        Technical Specifications: Energy density >400 Wh/kg, cycle life >1000 charges, safety improvements
        Market Adoption: Manufacturing scale-up challenges and cost competitiveness

        Analysis Focus: Timeline for mass market availability and factors affecting commercial adoption.
        ```

        ### 5. Comparative Analysis and Benchmarking

        **Structure:**
        ```
        Comparison Subject: [What you're comparing]
        Comparison Criteria: [Specific metrics or factors]
        Entities to Compare: [Specific options, companies, solutions, etc.]
        Data Sources: [Preferred types of comparative data]
        Context: [Relevant background or constraints]

        Output Format: [How you want results presented]
        ```

        **Example:**
        ```
        Comparison Subject: Cloud infrastructure providers for AI/ML workloads
        Comparison Criteria: GPU availability, pricing per compute hour, ML framework support, data transfer costs
        Entities to Compare: AWS, Google Cloud, Microsoft Azure, Oracle Cloud
        Data Sources: Current pricing pages, performance benchmarks, user reviews from 2025
        Context: Mid-size startup with budget constraints and emphasis on training large language models

        Output Format: Comparative table with pros/cons summary for each provider.
        ```

        ### 6. Regulatory and Compliance Research

        **Structure:**
        ```
        Regulatory Domain: [Specific area of regulation]
        Jurisdictions: [Countries, states, or regions]
        Effective Dates: [When regulations take effect]
        Industry Impact: [Specific sectors or business types affected]
        Compliance Requirements: [Particular obligations or standards]

        Analysis Scope: [Implementation guidance, enforcement patterns, industry adaptation, etc.]
        ```

        **Example:**
        ```
        Regulatory Domain: Data privacy and AI governance
        Jurisdictions: United States, European Union, United Kingdom
        Effective Dates: Regulations enacted or updated in 2024-2025
        Industry Impact: Healthcare technology companies using AI for diagnostics
        Compliance Requirements: Data handling, algorithmic transparency, patient consent

        Analysis Scope: Practical compliance steps and recent enforcement actions relevant to healthtech AI applications.
        ```

        ## Advanced Prompting Techniques

        ### 1. Multi-Layered Research Queries

        Use follow-up specifications to guide deeper research:

        ```
        Primary Research: [Initial broad query]

        For each finding, also investigate:
        - Recent developments or changes (past 6 months)
        - Geographic variations or regional differences
        - Dissenting opinions or contradictory evidence
        - Practical implementation challenges

        Present findings with source diversity analysis.
        ```

        ### 2. Source Quality Optimization

        Guide Perplexity toward higher-quality sources:

        ```
        Research Focus: [Your topic]
        Source Preferences:
        - Prioritize: Peer-reviewed research, government reports, industry white papers
        - Include: Recent news from established outlets
        - Avoid: Social media posts, unverified blogs, promotional content

        Quality Indicators: Look for sources with clear methodologies, disclosed funding, and author credentials.
        ```

        ### 3. Temporal Comparison Framework

        Structure queries to capture changes over time:

        ```
        Comparative Timeline Analysis: [Topic]

        Time Period 1: [Earlier period] - establish baseline
        Time Period 2: [Recent period] - identify changes
        Change Analysis: Quantify differences and identify trend patterns
        Future Implications: Based on current trajectory, what changes might be expected?

        Focus on measurable changes with supporting data.
        ```

        ### 4. Multi-Perspective Research

        Ensure comprehensive coverage:

        ```
        Multi-Stakeholder Analysis: [Topic]

        Perspective 1: [Academic/research viewpoint]
        Perspective 2: [Industry/commercial viewpoint]  
        Perspective 3: [Regulatory/government viewpoint]
        Perspective 4: [Consumer/end-user viewpoint]

        For each perspective:
        - Key concerns and priorities
        - Recent statements or publications
        - Proposed solutions or recommendations

        Synthesize areas of consensus and conflict.
        ```

        ### 5. Verification and Cross-Reference Approach

        Build in fact-checking and reliability assessment:

        ```
        Research Topic: [Your subject]
        Verification Requirements:
        - Cross-reference key claims across minimum 3 independent sources
        - Identify any conflicting information and explain discrepancies
        - Note source publication dates and update frequency
        - Flag any claims that lack multiple source verification

        Present findings with confidence levels based on source agreement.
        ```

        ## Model-Specific Optimization

        ### Using Sonar (Default Model)
        - Best for: General research, current events, balanced coverage
        - Strengths: Search integration, source variety, cost-effective
        - Optimization: Use specific time frames and clear research objectives

        ### Using GPT-5 (Pro)
        - Best for: Complex analysis requiring advanced reasoning
        - Strengths: Deep analytical capabilities, nuanced interpretation
        - Optimization: Provide more context and ask for multi-step analysis

        ### Using Claude 4.0 Sonnet (Pro)
        - Best for: Research requiring careful source evaluation and ethical considerations
        - Strengths: Nuanced analysis, bias awareness, structured outputs
        - Optimization: Ask for multiple perspectives and bias identification

        ### Using Gemini 2.5 Pro (Pro)
        - Best for: Multimodal research, data interpretation, visual content analysis
        - Strengths: Handling images, charts, and mixed content types
        - Optimization: Include requests for visual content analysis when relevant

        ### Using Reasoning Search Models (Pro)
        - Best for: Complex analytical questions requiring step-by-step logic
        - Strengths: Mathematical reasoning, logical problem-solving
        - Optimization: Structure queries as logical problems with clear parameters

        ## Optimization Strategies

        ### 1. Iterative Refinement
        Perplexity moves beyond one-shot Q&A toward source-grounded, multi-step research workflows. Use follow-up queries to refine and expand:

        **Initial Query:**
        ```
        What are the main challenges in renewable energy storage?
        ```

        **Follow-up Refinement:**
        ```
        Based on the storage challenges you identified, which specific solutions show the most promise for grid-scale implementation in the next 5 years? Focus on recent pilot projects and commercial deployments.
        ```

        ### 2. Source Diversification Requests

        ```
        Research [topic] using sources from:
        - Academic institutions and research centers
        - Government agencies and policy organizations
        - Industry associations and commercial entities
        - International organizations and NGOs

        Highlight any significant disagreements between source types.
        ```

        ### 3. Recency Optimization

        ```
        Priority Search Order:
        1. Information published in the last 30 days
        2. Sources updated within the past 6 months
        3. Foundational sources that provide essential context

        Note the publication date for all key claims and flag outdated information.
        ```

        ### 4. Geographic Scope Management

        ```
        Geographic Research Framework:
        Primary Focus: [Specific region/country]
        Comparative Context: Include relevant examples from [other regions]
        Global Perspective: Note international trends and standards
        Local Variations: Identify region-specific factors or exceptions
        ```

        ## Common Pitfalls and Solutions

        ### Pitfall 1: Overly Broad Queries
        **Problem:** Getting surface-level information across too many topics
        **Solution:** Use specific, focused research questions with clear scope

        **Instead of:** "Tell me about artificial intelligence"
        **Use:** "What are the most significant AI safety research developments published by major labs in Q3 2025?"

        ### Pitfall 2: Ignoring Time Sensitivity
        **Problem:** Getting outdated information mixed with current data
        **Solution:** Always specify time frames and prioritize recent sources

        ### Pitfall 3: Not Leveraging Source Diversity
        **Problem:** Responses dominated by single source types
        **Solution:** Explicitly request diverse source types and perspectives

        ### Pitfall 4: Insufficient Context for Complex Topics
        **Problem:** Shallow analysis of nuanced subjects
        **Solution:** Provide background context and ask for multi-layered analysis

        ### Pitfall 5: Not Using Follow-Up Capabilities
        **Problem:** Missing opportunities for deeper research
        **Solution:** Engage in multi-step research workflows with iterative refinement

        ## Quality Indicators for Perplexity Responses

        ### High-Quality Response Indicators:
        - Multiple independent sources cited
        - Recent publication dates for time-sensitive topics
        - Clear distinction between established facts and emerging claims
        - Acknowledgment of limitations or conflicting information
        - Geographic and demographic context when relevant

        ### Red Flags:
        - Single source for major claims
        - Outdated information for rapidly changing topics
        - Lack of source diversity across stakeholder perspectives
        - Missing context about data quality or methodology

        ## Best Practices Summary

        1. **Be Specific**: Be explicit about exactly what information you need
        2. **Use Time Frames**: Always specify relevant time periods for current topics
        3. **Request Source Diversity**: Ask for multiple types of sources and perspectives
        4. **Iterate and Refine**: Use multi-step research workflows for complex topics
        5. **Verify Claims**: Ask for cross-referencing of key information
        6. **Consider Context**: Approach Perplexity as an efficient research assistant rather than a replacement for deeper analysis

        Perplexity excels as a research accelerator, providing the foundational information and source discovery needed for informed decision-making. The key is to structure queries as research projects rather than simple questions, leveraging its search integration and source citation capabilities to build comprehensive, verifiable knowledge bases.
    """
}