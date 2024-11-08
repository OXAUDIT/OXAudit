

---

![OXAUDIT Logo](https://cdn.prod.website-files.com/670b2bd0fc4e2e91ce443ddd/670e5dc91b9df286f6674b15_RECTANGLE.png)

# OXAUDIT: The Smart Contract Static Analyzer

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> **OXAUDIT** is a Solidity static analysis tool written in Python. It offers a suite of vulnerability detectors, insightful contract details, and a flexible API for custom analyses. OXAUDIT helps developers identify vulnerabilities, improve code quality, and streamline the development of secure smart contracts.

---

## 🌟 Features

- **Comprehensive Vulnerability Detection**: Detects common vulnerabilities in Solidity code with minimal false positives.
- **Accurate Issue Location**: Pinpoints exact locations of issues in the source code.
- **Seamless CI Integration**: Easily integrates with CI/CD pipelines to automate code analysis.
- **Detailed Contract Analysis**: Offers in-depth information on contracts through built-in printers.
- **Customizable API**: Allows for the development of new detectors and analyses.
- **Supports Multiple Solidity Versions**: Analyzes code from Solidity version >= 0.4.
- **Optimized Performance**: Executes analysis in under a second per contract.
- **GitHub Code Scanning**: Direct integration with GitHub's code scanning.

---

## 📦 Installation

OXAUDIT can be installed via Pip, Git, or Docker.

### Using Pip

```bash
python3 -m pip install oxaudit
```

### Using Git

```bash
git clone https://github.com/oxaudit/oxaudit.git && cd oxaudit
python3 -m pip install .
```

### Using Docker

```bash
docker pull oxaudit/oxaudit
docker run -it -v /home/share:/share oxaudit/oxaudit
```

---

## ⚙️ Usage

To analyze a project with dependencies:

```bash
oxaudit .
```

For single files without dependencies:

```bash
oxaudit path/to/your/contract.sol
```

---

## 🔄 Integration

To integrate **OXAUDIT** with GitHub Actions, add this to your GitHub Actions workflow:

```yaml
- name: Run OXAUDIT
  uses: oxaudit/oxaudit-action@main
```

To generate a Markdown report:

```bash
oxaudit [target] --report markdown
```

---

## 🔍 Detectors

OXAUDIT includes a comprehensive set of detectors for common vulnerabilities, including:

| #   | Detector                  | Description                                              | Impact  | Confidence |
|-----|----------------------------|----------------------------------------------------------|---------|------------|
| 1   | `uninitialized-storage`    | Detects uninitialized storage usage                      | High    | High       |
| 2   | `reentrancy`               | Detects reentrancy vulnerabilities                       | High    | High       |
| 3   | `unprotected-functions`    | Identifies unprotected functions                         | Medium  | Medium     |
| 4   | `low-level-calls`          | Flags low-level calls usage                              | Low     | Medium     |
| 5   | `integer-overflow`         | Detects potential integer overflows                      | High    | High       |
| 6   | `missing-zero-check`       | Identifies missing zero address validation               | Medium  | High       |
| 7   | `arbitrary-send`           | Flags functions that send Ether to arbitrary destinations| High    | Medium     |
| 8   | `shadowed-state-variables` | Detects state variables shadowing                        | Medium  | High       |
| 9   | `timestamp-dependence`     | Flags risky block.timestamp usage                        | Medium  | Medium     |
| 10  | `tx-origin-auth`           | Detects risky tx.origin-based authentication             | High    | Medium     |
| 11  | `costly-loop`              | Flags loops with costly operations                       | Medium  | Medium     |
| 12  | `assert-state-change`      | Detects assert statements causing state changes          | Low     | High       |
| 13  | `unchecked-send`           | Identifies unchecked sends                               | High    | Medium     |
| 14  | `unauthorized-selfdestruct`| Detects potential unauthorized selfdestruct calls        | High    | High       |
| 15  | `floating-pragmas`         | Detects floating pragmas for Solidity versions           | Low     | High       |

For a full list of detectors, refer to the **[Detectors Documentation](https://docs.oxaudit.com/basics/markdown)**.

---

## 🖨️ Printers

OXAUDIT provides several printers for quick and in-depth reviews.

### Quick Review Printers

- `human-summary`: Prints a human-readable summary of the contract.
- `loc`: Counts lines of code (LOC), source lines of code (SLOC), and comments.

### In-Depth Review Printers

- `call-graph`: Exports the call graph of the contract.
- `cfg`: Exports the Control Flow Graph (CFG).

To run a printer:

```bash
oxaudit --print [printer-name]
```

---

## 🛠️ Tools

OXAUDIT includes several auxiliary tools:

- `oxaudit-check-upgradeability`: Review upgradeable contract safety.
- `oxaudit-read-storage`: Reads storage values from contracts.
- `oxaudit-interface`: Generates an interface for a contract.

For more details, refer to the **[Tool Documentation](https://docs.oxaudit.com/basics/markdown)**.

---

## 💬 Getting Help

For questions and support, visit our **[OXAUDIT Slack channel](https://docs.oxaudit.com/)**.

- **Detector Documentation**: How to write new analyses.
- **Printer Documentation**: Available printers and their usage.
- **API Documentation**: Methods and objects for custom analyses.
- **Intermediate Representation (IR) Documentation**: The IR used in OXAUDIT.

---

## 📋 FAQ

- **How do I exclude certain files?**  
  Use `--exclude` to ignore specific files or directories.

- **Troubleshooting compilation issues?**  
  If compilation fails, ensure all dependencies are available. Try `oxaudit .` from the main project directory.

---

## 📜 License

OXAUDIT is licensed under the **MIT License**.

---

