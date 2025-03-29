# DB--Multi-threaded-In-memory-Durable-L-Store
Date: March 2025
by Yanming Luo

Overview

This repository contains the implementation for a threaded-In-memory-Durable-L-Store database system , featuring a multi-threaded, in-memory, durable L-Store database supporting full transaction semantics (ACID properties).

Key Features

Atomic Transactions: Ensures transactions either fully complete or completely roll back in case of failures.

Two-Phase Locking (2PL): Implements concurrency control to safely execute multiple transactions simultaneously without deadlocks (no-wait policy).

Multi-threaded Execution: Transactions run concurrently, leveraging Python’s threading capabilities for improved performance.

Efficient Indexing: Provides basic indexing structures to enhance query performance.

Durable Storage: Transactions and data persist beyond system failures, ensuring long-term reliability.

Project Structure

Milestone3/
├── lstore/
│   ├── db.py
│   ├── query.py
│   ├── index.py
│   ├── transaction.py
│   ├── table.py
│   ├── page.py
│   └── transaction_worker.py
├── __main__.py
└── test scripts (m1_tester.py, m2_tester_part1.py, ...)

Setup

Clone the repository:

git clone [your_repo_link_here]

Install dependencies:

pip install -r requirements.txt

Running the Project

Execute the main file to start the database system:

python __main__.py

Run provided test scripts to verify implementation correctness:

python m3_tester_part_1.py
python m3_tester_part_2.py

Usage Examples

Creating a new database:

from lstore.db import Database
db = Database()

Creating tables and transactions:

table = db.create_table('grades', 5, 0)
transaction = Transaction()

Future Improvements

Fully implemented rollback mechanism.

Enhanced indexing and query optimization.

Robust lock manager for concurrency control.

Better memory management and scalability.
