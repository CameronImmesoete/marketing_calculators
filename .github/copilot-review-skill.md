# Code Review Standards

> Base review standards: [CameronImmesoete/.github/.github/copilot-review-skill.md@1f79bfb](https://github.com/CameronImmesoete/.github/blob/1f79bfb3e9eee277d05ecdd3332220204cb0f38b/.github/copilot-review-skill.md)

## Repository-Specific Review Criteria

### Marketing Formula Correctness
- Verify CLV calculation uses correct discount rate formula
- Verify CAC includes all acquisition cost components
- Verify conjoint analysis regression matches standard part-worth utility model
- Verify NPS calculation correctly buckets promoters (9-10), passives (7-8), detractors (0-6)
- Check all percentage calculations handle the 0-1 vs 0-100 scale consistently

### Calculator Edge Cases
- Zero revenue, zero customers, 100% churn rate
- Negative values where economically meaningful vs where they should be rejected
- Division by zero in all ratio calculations
- Empty or single-element input arrays for conjoint analysis
