- requirements should be consistent with their depth. 
- functional requirement should be numbered as 10, 20, 30 (11 for sub requirement of 10)
- functional and non functional requirement chapters should be separate 
## functional requirement quality metrics 
Quality measurement of functional requirements (FRs) involves ==evaluating whether the behaviors, features, and system operations defined in your documentation are clear, complete, consistent, and testable before or during development==. [[1](https://www.jamasoftware.com/requirements-management-guide/writing-requirements/identifying-and-measuring-the-quality-of-requirements/), [2](https://visuresolutions.com/alm-guide/how-to-measure-requirements-quality/), [3](https://jtec.utem.edu.my/jtec/article/view/2709/1756)]

Key Dimensions of Functional Requirements Quality

- **Preciseness & Clarity:** Measures whether requirements use unambiguous language without vague terms (e.g., "fast," "user-friendly," "as soon as possible") that different team members interpret differently. [[1](https://visuresolutions.com/alm-guide/how-to-measure-requirements-quality/), [2](https://www.jamasoftware.com/requirements-management-guide/writing-requirements/identifying-and-measuring-the-quality-of-requirements/)]
- **Completeness:** Assesses whether all necessary system inputs, boundary conditions, safe states, error handling, and expected outputs are accounted for without missing details. [[1](https://www.scitepress.org/Papers/2023/121487/121487.pdf), [2](https://www.sciencedirect.com/topics/engineering/functional-requirement), [3](https://jtec.utem.edu.my/jtec/article/view/2709/1756)]
- **Consistency:** Checks for contradictions or conflicts between different functional requirements or across related user stories and use cases. [[1](https://jtec.utem.edu.my/jtec/article/view/2709/1756), [2](https://www.scitepress.org/Papers/2023/121487/121487.pdf)]
- **Correctness & Conformity:** Validates that each requirement accurately reflects real stakeholder and business needs and aligns with domain rules. [[1](https://www.researchgate.net/publication/376993893_Software_Quality_Measurement_for_Functional_Suitability_Performance_Efficiency_and_Reliability_Characteristics_Using_Analytical_Hierarchy_Process), [2](https://jtec.utem.edu.my/jtec/article/view/2709/1756)]
- **Traceability:** Evaluates how well individual requirements map backward to business goals and forward to design artifacts, source code, and test cases. [[1](https://visuresolutions.com/alm-guide/how-to-measure-requirements-quality/)]
- **Verifiability / Testability:** Ensures a clear, objective pass/fail condition can be written for every functional requirement. [[1](https://www.researchgate.net/publication/376993893_Software_Quality_Measurement_for_Functional_Suitability_Performance_Efficiency_and_Reliability_Characteristics_Using_Analytical_Hierarchy_Process)]

---

Common Methods and Metrics to Measure Quality

- **Quantitative Clarity and Defect Metrics:**
    - **Defect Density / Review Efficiency:** Tracking the number of ambiguity, logic, or omission defects discovered during requirement peer reviews relative to total project defects.
    - **Requirement Count / Size (Functional Size Measurement - FSM):** Using standards like **ISO/IEC 14143** or COSMIC/IFPUG function points to count and size functional units consistently.
    - **Requirement Coverage Index:** Measuring the percentage of stakeholder needs or use-case scenarios covered by baseline functional requirements. [[1](https://link.springer.com/content/pdf/10.1007/978-3-540-89403-2_24.pdf), [2](https://www.researchgate.net/publication/376993893_Software_Quality_Measurement_for_Functional_Suitability_Performance_Efficiency_and_Reliability_Characteristics_Using_Analytical_Hierarchy_Process), [3](https://visuresolutions.com/alm-guide/how-to-measure-requirements-quality/)]
- **Qualitative Reviews & Checklists:**
    - **Expert Peer Reviews:** Involving business analysts, developers, and QA engineers to critique logic, edge cases, and feasibility.
    - **Mnemonics and Frameworks:** Utilizing structured checklists (such as _CIRCUS MATTER_ or the _5WHA_ method—Who, What, When, Where, Why, How) to audit individual user stories or specs. [[1](https://www.youtube.com/watch?v=zgamcXvOwbg&t=990), [2](https://visuresolutions.com/alm-guide/how-to-measure-requirements-quality/)]
- **Automated & Semantic Analysis:**
    - **Natural Language Processing (NLP) / Text Mining:** Using parsing tools or requirement-checking engines to flag passive voice, vague modifiers, missing subjects, or conflicting terminology in textual specifications.
    - **Model-Based Verification:** Constructing lightweight UML, domain, or state-transition models from text to automatically expose gaps or unreachable states. [[1](https://www.researchgate.net/publication/372324689_Quality_Measurement_of_Functional_Requirements), [2](https://www.scitepress.org/Papers/2023/121487/121487.pdf)]
