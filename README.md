This repository includes lecture/lab materials for COM3523/6523 Software Reengineering at the University of Sheffield.

# Redistribute Responsibilities

## Agenda
- Apply reengineering patterns to redistribute responsibilities.

## Setup
We do not require any additional libraries for this week's exercise. :-)

## Check the Code
Have a look at the code:
- `Account.py`: The Account class. Currently a data container.
- `Bank.py`: The Bank class. Currently a god class (having all the responsibilities/behaviours).
- `Branch.py`: The Branch class. Currently a data container.
- `client.py`: A client program that uses the Bank class.
- `Customer.py`: The Customer class. Currently a data container.
- `Payroll.py`: The Payroll class, internally using PaySchedule.
- `PaySchedule.py`: The PaySchedule class. No need to edit this class.
- `Staff.py`: The Staff class. No need to edit this class.
- `tests/test_client.py`: A test case for the client program.

You can run the regression test case by executing the following command:
```bash
python -m unittest tests/test_client.py
```
The test case should pass.

## Task: Redistribute Responsibilities
The Bank class is currently a god class. 
We want to redistribute the responsibilities to other classes. 
Specifically, you should consider the following reengineering patterns:
- Move behaviour close to data
- Remove navigation code
- Split up god class

Note that you may need to update the client code to use the new classes.
Make sure you do not remove client's behaviours, i.e., **do not remove assertions** (just update them if needed).

After the reengineering, the regression test case should still pass.

## Mini Report

After completing the above task, push the changes to the repository and include a short report to summarise what you have done for the task. 
It is important to discuss your motivation and rationale for the changes you have made.

On the report's front page, please record below who participated in this week's exercise submissions:

- NAME (brief description of the role)
- NAME (brief description of the role)
...

**Important**: Commit the report as `mini-report.pdf` within the **root** directory.

## Resources

- Demeyer, Serge, Stéphane Ducasse, and Oscar Nierstrasz. Object-oriented reengineering patterns. Elsevier, 2002.