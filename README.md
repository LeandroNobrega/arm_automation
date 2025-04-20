This project contains a Python function that classifies packages in a robotic automation factory based on their **volume**, **dimensions**, and **mass**.

The packages are dispatched into different stacks: `STANDARD`, `SPECIAL`, or `REJECTED` based on specific criteria.

Sort packages into the correct stack using the following logic:

- A package is **bulky** if:
  - Its **volume** (`width × height × length`) is **≥ 1,000,000 cm³**, OR
  - Any **dimension** is **≥ 150 cm**
- A package is **heavy** if its **mass is ≥ 20 kg**

### Stack Rules:
| Category   | Description                                |
|------------|--------------------------------------------|
| STANDARD   | Not bulky and not heavy                    |
| SPECIAL    | Bulky **or** heavy (but not both)          |
| REJECTED   | Bulky **and** heavy                        |

---

## Execution example

```
python -m main 50 50 50 10
```
Result:
Package parameters: Width 50.0, Height 50.0, Length 50.0, Mass 10.0
Package classification: STANDARD

---

## Tests

```
pytest sort_package/tests.py
```
