# group11-review-testing
**Code Review and Software Testing Assignment**

- Each group splits into two subgroups: A and B
- Each subgroup: Designs 1/2 of the modules/functions + does the code review of the other subgroup

---

**What to submit for this group assignment?**

Billy, Helena, Beth

Caden, Joey

- Code files (subgroup A)
- Code Review and Software Testing Report (subgroup A)
- Code files (subgroup B)
- Code Review and Software Testing Report (subgroup B)
- Integrated code files (after merging subgroup A & subgroup B)
- Integration report (after merging subgroup A & subgroup B)
- IMPORTANT: Subgroup A does the report for subgroup B and vice versa
- Subgroups do not do their own report

---

**Code Review and Software Testing report**

- Modularity: Is the code modular? Divided into functions and classes?
- Naming: Are function names and variable names meaningful? Improvements?
- Readability: Is the code easy to read and understand?
- Comments: Are appropriate comments included? What can improve clarity?
- Unit test cases: At least 6 test cases (include edge cases)
    - Show input, code outputs, expected outputs
- Code coverage: Compute statement and branch coverage (>80%)
- Mutation analysis: Perform 2–3 mutations
    - Run test cases again
    - Show which test cases kill mutants
- No coding required for test cases (just input/output/expected output)
- Include examples for modularity, naming, readability, comments

---

**Integrated Report**

- Mention subgroup division (who is in A and B)
- Integration test cases after merging code
    - Show input, code outputs, expected outputs
- Document iterations/code changes needed to pass tests
- No coding required for test cases

---

**How does each subgroup code? (Pair Programming)**

- Driver: does the coding
- Observers: navigate code, search for bugs, do live review
- Switch roles often
- 2–3 programmers collaborate on one laptop

---

**Problem: Ticket to Ride style path planning**

- Given:
    - Set of tickets [(source, destination)]
    - Weighted directed graph (adjacency matrix)
- Output: optimal railway path such that:
    - source and destination of each ticket is connected
    - total path cost is minimized
    - no cycles in final railway network
- Goal:
    - find a path for each ticket
    - choose shortest valid path
    - if cycle forms → explore alternate paths
- Algorithms: Dijkstra + union-find