Here's the updated README with additional detectors listed for **OXAUDIT**:

---

# OXAUDIT, the Smart Contract Static Analyzer

**OXAUDIT** is a Solidity static analysis tool written in Python. It offers a suite of vulnerability detectors, provides insightful contract details, and includes an API to develop custom analyses. OXAUDIT helps developers identify vulnerabilities, understand their code better, and quickly prototype custom analyses.

## Features

- Detects common vulnerabilities in Solidity code with low false positives.
- Pinpoints exact locations of issues in the source code.
- Easily integrates into continuous integration pipelines.
- Provides comprehensive contract information through built-in printers.
- Customizable API for developing new detectors and analyses in Python.
- Supports Solidity versions >= 0.4.
- Parses nearly all public Solidity code accurately.
- Executes analyses in under a second per contract.
- Integration with GitHub's code scanning.

## Usage

To run **OXAUDIT** on a project:

```bash
oxaudit .
```

For single files without dependencies:

```bash
oxaudit path/to/your/contract.sol
```

## Installation

### Using Pip

```bash
python3 -m pip install oxaudit
```

### Using Git

```bash
git clone https://github.com/your-repo/oxaudit.git && cd oxaudit
python3 -m pip install .
```

### Using Docker

To use **OXAUDIT** with Docker:

```bash
docker pull your-repo/oxaudit
docker run -it -v /home/share:/share your-repo/oxaudit
```

## Integration

For GitHub Actions integration:

```yaml
- name: Run OXAUDIT
  uses: your-repo/oxaudit-action@main
```

To generate a Markdown report:

```bash
oxaudit [target] --report markdown
```

## Detectors

OXAUDIT includes a comprehensive set of detectors for common vulnerabilities, including:

| #   | Detector                  | Description                                              | Impact  | Confidence |
|-----|----------------------------|----------------------------------------------------------|---------|------------|
| 1   | uninitialized-storage      | Detects uninitialized storage usage                      | High    | High       |
| 2   | reentrancy                 | Detects reentrancy vulnerabilities                       | High    | High       |
| 3   | unprotected-functions      | Identifies unprotected functions                         | Medium  | Medium     |
| 4   | low-level-calls            | Flags low-level calls usage                              | Low     | Medium     |
| 5   | integer-overflow           | Detects potential integer overflows                      | High    | High       |
| 6   | missing-zero-check         | Identifies missing zero address validation               | Medium  | High       |
| 7   | arbitrary-send             | Flags functions that send Ether to arbitrary destinations| High    | Medium     |
| 8   | shadowed-state-variables   | Detects state variables shadowing                        | Medium  | High       |
| 9   | timestamp-dependence       | Flags risky block.timestamp usage                        | Medium  | Medium     |
| 10  | tx-origin-auth             | Detects risky tx.origin-based authentication             | High    | Medium     |
| 11  | costly-loop                | Flags loops with costly operations                       | Medium  | Medium     |
| 12  | assert-state-change        | Detects assert statements causing state changes          | Low     | High       |
| 13  | unchecked-send             | Identifies unchecked sends                               | High    | Medium     |
| 14  | unauthorized-selfdestruct  | Detects potential unauthorized selfdestruct calls        | High    | High       |
| 15  | floating-pragmas           | Detects floating pragmas for Solidity versions           | Low     | High       |
| 16  | unused-state               | Flags unused state variables                             | Low     | Medium     |
| 17  | redundant-statements       | Detects redundant or unreachable code                    | Low     | High       |
| 18  | unsafe-delegatecall        | Flags unsafe delegatecalls                               | High    | High       |

For a full list of detectors, please see the [Detectors Documentation](#).

## Printers

OXAUDIT offers several printers for quick and in-depth reviews.

### Quick Review Printers

- `human-summary`: Prints a human-readable contract summary.
- `loc`: Counts lines of code (LOC), source lines of code (SLOC), and comments.

### In-Depth Review Printers

- `call-graph`: Exports the call graph of the contract.
- `cfg`: Exports the Control Flow Graph (CFG).

To run a printer:

```bash
oxaudit --print [printer-name]
```

## Tools

OXAUDIT includes several auxiliary tools:

- `oxaudit-check-upgradeability`: Review upgradeable contract safety.
- `oxaudit-read-storage`: Reads storage values from contracts.
- `oxaudit-interface`: Generates an interface for a contract.

For more details, check the [Tool Documentation](#).

## Getting Help

For questions and support, visit our [OXAUDIT Slack channel](#).

- Detector Documentation: How to write new analyses.
- Printer Documentation: Available printers and their usage.
- API Documentation: Methods and objects for custom analyses.
- Intermediate Representation (IR) Documentation: The IR used in OXAUDIT.

## FAQ

**How do I exclude certain files?**  
Use `--exclude` to ignore specific files or directories.

**Troubleshooting compilation issues?**  
If compilation fails, ensure all dependencies are available. Try `oxaudit .` from the main project directory.

## License

OXAUDIT is licensed under the MIT License.

--- 

This README should give a comprehensive overview for users setting up and using OXAUDIT. Let me know if you'd like further refinements!
